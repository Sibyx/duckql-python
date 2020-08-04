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


class DateAdd(BaseFunction):
    obj: Literal['functions.DateAdd'] = 'functions.DateAdd'
    property: Union[Constant, Property, BaseFunction, CastOperator]
    interval: Interval
    alias: str = None

    def to_sql(self) -> str:
        sql = f"DATE_ADD({self.property}, {self.interval})"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
