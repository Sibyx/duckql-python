from typing import Union

from pydantic.dataclasses import dataclass

from backboneql.exceptions import ParseError
from backboneql.functions.base import BaseFunction
from backboneql.properties.property import Property
from backboneql.properties.constant import Constant


@dataclass
class Weekday(BaseFunction):
    property: Union[Property, BaseFunction, Constant]
    alias: str = None

    def __post_init__(self):
        if hasattr(self, 'alias') and self.alias is not None:
            self.alias = self.escape(self.alias)

        if hasattr(self.property, 'alias') and self.property.alias is not None:
            raise ParseError("You can't have alias inside of function!")

    def to_sql(self) -> str:
        # TODO: postgresql
        sql = f"WEEKDAY({self.property})"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
