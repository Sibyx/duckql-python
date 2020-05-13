import json
from abc import ABC, abstractmethod
from enum import Enum
from typing import List

from pydantic import BaseModel, root_validator

from duckql.exceptions import ParseError
from duckql.utils import json_parse


class BaseType(BaseModel, ABC):
    class Dialect(Enum):
        POSTGRESQL = 'postgresql'
        MARIADB = 'mariadb'
        MYSQL = 'mysql'

    class Config:
        json_loads = json_parse
        json_dumps = json.dumps

    @root_validator(pre=True)
    def escape_alias(cls, values):
        if 'alias' in values and values['alias'] is not None:
            values['alias'] = cls.escape(values['alias'])
        return values

    @root_validator(pre=True)
    def check_nested_aliases(cls, values):
        if 'properties' in values and str(cls) != "<class 'duckql.structures.query.Query'>":

            if any(map(lambda x: hasattr(x, 'alias') and x.alias is not None, values['properties'])):
                raise ParseError("You can't have alias inside of function!")

        # Absolutely ugly validation, I hate myself for this
        if 'property' in values:
            if isinstance(values['property'], dict):
                if 'alias' in values['property'] and values['property']['alias'] is not None:
                    raise ParseError("You can't have alias inside of function!")
            else:
                if hasattr(values['property'], 'alias') and values['property'].alias is not None:
                    raise ParseError("You can't have alias inside of function!")

        return values

    @abstractmethod
    def to_sql(self) -> str:
        pass

    def __str__(self) -> str:
        return self.to_sql()

    @staticmethod
    def escape(value: str, ignore: List[str] = None) -> str:
        insecure_chars = {
            "\0": "\\0",
            "\r": "\\r",
            "\x08": "\\b",
            "\x09": "\\t",
            "\x1a": "\\z",
            "\n": "\\n",
            "\"": "",
            "'": "",
            "\\": "\\\\",
            ';': '',
        }

        if ignore:
            # Removes ignored chars from insecure_chars dictionary
            # https://stackoverflow.com/a/30351294/4458288
            list(map(insecure_chars.__delitem__, filter(insecure_chars.__contains__, ignore)))

        value = value.translate(
            value.maketrans(insecure_chars)
        )

        to_remove = [
            '--'
        ]

        for item in to_remove:
            value = value.replace(item, '')

        return value
