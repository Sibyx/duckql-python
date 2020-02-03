from typing import Union

from pydantic.dataclasses import dataclass

from backboneql.exceptions import ParseError
from backboneql.types.functions.base import BaseFunction
from backboneql.types.properties import Property, Constant


@dataclass
class DateFormat(BaseFunction):
    property: Union[Property, Constant, BaseFunction]
    format: str
    alias: str = None

    def __post_init__(self):
        if hasattr(self.property, 'alias') and self.property.alias is not None:
            raise ParseError("You can't have alias inside of function!")

        self.format = self.escape(self.format, ['%'])

        if self.alias is not None:
            self.alias = self.escape(self.alias)

    def to_sql(self) -> str:
        sql = f"DATE_FORMAT({self.property}, '{self.format}')"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
