from typing import Union

from typing_extensions import Literal

from backboneql.base import BaseType
from backboneql.functions.base import BaseFunction
from backboneql.properties.constant import Constant
from backboneql.properties.property import Property
from backboneql.structures.interval import Interval


class DateSub(BaseType):
    obj: Literal['date_sub'] = 'date_sub'
    property: Union[Constant, Property, BaseFunction]
    interval: Interval
    alias: str = None

    def to_sql(self) -> str:
        sql = f"DATE_SUB({self.property}, {self.interval})"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
