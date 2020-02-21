from typing import List, Union

from pydantic.dataclasses import dataclass

from backboneql.exceptions import ParseError
from backboneql.functions.base import BaseFunction
from backboneql.properties.property import Property
from backboneql.properties.constant import Constant


@dataclass
class Concat(BaseFunction):
    properties: List[Union[Property, BaseFunction, Constant]]
    alias: str = None

    def __post_init__(self):
        if self.alias is not None:
            self.alias = self.escape(self.alias)

        if any(map(lambda x: hasattr(x, 'alias') and x.alias is not None, self.properties)):
            raise ParseError("You can't have alias inside of function!")

    def to_sql(self) -> str:
        sql = f'CONCAT({", ".join(map(str, self.properties))})'

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
