from abc import ABC, abstractmethod
from enum import Enum
from typing import List

from pydantic.dataclasses import dataclass


@dataclass(init=False)
class BaseType(ABC):

    class Dialect(Enum):
        POSTGRESQL = 'postgresql'
        MARIADB = 'mariadb'
        MYSQL = 'mysql'

    @abstractmethod
    def to_sql(self) -> str:
        pass

    def __str__(self) -> str:
        return self.to_sql()

    @staticmethod
    def escape(value: str, ignore: List = None) -> str:
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
            "%": "\\%",
            ';': '',
        }

        if ignore:
            # Removes ignored cahrds from insecure_chars dictionary
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
