from enum import Enum
from typing import Union

from pydantic.dataclasses import dataclass

from backboneql.exceptions import ParseError
from backboneql.functions.base import BaseFunction
from backboneql.properties.constant import Constant
from backboneql.properties.property import Property
from backboneql.structures.interval import Interval


@dataclass
class Extract(BaseFunction):
    class Unit(Enum):
        CENTURY = 'century'
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

    property: Union[Constant, Property, BaseFunction, Interval]
    unit: Unit
    alias: str = None

    def __post_init__(self):
        if hasattr(self, 'alias') and self.alias is not None:
            self.alias = self.escape(self.alias)

        if hasattr(self.property, 'alias') and self.property.alias is not None:
            raise ParseError("You can't have alias inside of function!")

    def to_sql(self) -> str:
        sql = f"EXTRACT({self.unit.value.upper()} FROM {self.property})"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
