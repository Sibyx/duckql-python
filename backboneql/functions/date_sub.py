from typing import Union

from backboneql.base import BaseType
from backboneql.functions.base import BaseFunction
from backboneql.properties.constant import Constant
from backboneql.properties.property import Property
from backboneql.structures.interval import Interval


class DateSub(BaseType):
    property: Union[Constant, Property, BaseFunction]
    interval: Interval
    alias: str = None

    def to_sql(self) -> str:
        sql = f"DATE_SUB({self.property}, {self.interval})"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
