from typing import Union

from pydantic.dataclasses import dataclass

from backboneql.exceptions import ParseError
from backboneql.types.base import BaseType
from backboneql.types.functions.base import BaseFunction
from backboneql.types.properties import Constant, Property
from backboneql.types.structures import Interval


@dataclass
class DateSub(BaseType):
    property: Union[Constant, Property, BaseFunction]
    interval: Interval
    alias: str = None

    def __post_init__(self):
        if hasattr(self.property, 'alias') and self.property.alias is not None:
            raise ParseError("You can't have alias inside of function!")

        if self.alias is not None:
            self.alias = self.escape(self.alias)

    def to_sql(self) -> str:
        sql = f"DATE_SUB({self.property}, {self.interval})"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
