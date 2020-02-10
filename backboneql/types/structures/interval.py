from enum import Enum

from pydantic.dataclasses import dataclass

from backboneql.types.base import BaseType


@dataclass
class Interval(BaseType):
    class Unit(Enum):
        MICROSECOND = "microsecond"
        SECOND = "second"
        MINUTE = "minute"
        HOUR = "hour"
        DAY = "day"
        WEEK = "week"
        MONTH = "month"
        QUARTER = "quarter"
        YEAR = "year"
        SECOND_MICROSECOND = "second_microsecond"
        MINUTE_MICROSECOND = "minute_microsecond"
        MINUTE_SECOND = "minute_second"
        HOUR_MICROSECOND = "hour_microsecond"
        HOUR_SECOND = "hour_second"
        HOUR_MINUTE = "hour_minute"
        DAY_MICROSECOND = "day_microsecond"
        DAY_SECOND = "day_second"
        DAY_MINUTE = "day_minute"
        DAY_HOUR = "day_hour"
        YEAR_MONTH = "year_month"

    value: int
    unit: Unit

    def to_sql(self) -> str:
        return f"INTERVAL {self.value} {self.unit.value.upper()}"
