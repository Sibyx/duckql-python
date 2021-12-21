from typing import Union, Optional, List

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..structures.distinct import Distinct
from ..functions.base import BaseFunction
from ..properties import Array
from ..properties.property import Property
from ..structures.cast_operator import CastOperator
from ..structures.case import Case
from ..structures.order import Order


class ArrayAgg(BaseFunction):
    obj: Literal['functions.StringAgg'] = 'functions.ArrayAgg'
    property: Union[Property, BaseFunction, Array, CastOperator, Distinct, Case]
    order: Optional[List[Order]]
    position: Optional[int]
    alias: str = None

    def to_sql(self) -> str:
        sql = f"{self.property}"

        if self.order:
            sql = f"{sql} ORDER BY {', '.join(map(str, self.order))}"

        sql = f"ARRAY_AGG({sql})"

        if self.position:
            sql = f"({sql})[{self.position}]"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
