from enum import Enum
from typing import Union

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..functions.base import BaseFunction
from ..properties.constant import Constant
from ..properties.property import Property
from ..structures.cast_operator import CastOperator
from ..structures.interval import Interval


class Extract(BaseFunction):
    class Unit(Enum):
        CENTURY = 'century'
        DAY = 'day'
        DECADE = 'decade'
        DOW = 'dow'
        DOY = 'doy'
        EPOCH = 'epoch'
        HOUR = 'hour'
        ISODOW = 'isodow'
        ISOYEAR = 'isoyear'
        MICROSECONDS = 'microseconds'
        MILLENNIUM = 'millennium'
        MILLISECONDS = 'milliseconds'
        MINUTE = 'minute'
        MONTH = 'month'
        QUARTER = 'quarter'
        SECOND = 'second'
        TIMEZONE = 'timezone'
        TIMEZONE_HOUR = 'timezone_hour'
        TIMEZONE_MINUTE = 'timezone_minute'
        WEEK = 'week'
        YEAR = 'year'

    obj: Literal['functions.Extract'] = 'functions.Extract'
    property: Union[Constant, Property, BaseFunction, Interval, CastOperator]
    unit: Unit
    alias: str = None

    def to_sql(self) -> str:
        sql = f"EXTRACT({self.unit.value.upper()} FROM {self.property})"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
