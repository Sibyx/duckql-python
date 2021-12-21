from typing import Union, List

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from .base import BaseFunction
from ..properties.constant import Constant
from ..structures.order import Order
from ..properties.property import Property
from ..structures.cast_operator import CastOperator
from ..structures.case import Case


class FirstValue(BaseFunction):
    obj: Literal['functions.FirstValue'] = 'functions.FirstValue'
    property: Union[Property, BaseFunction, Constant, CastOperator, Case]
    order: List[Order]
    partition: List[Union[Property, BaseFunction, Constant, CastOperator, Case]] = []
    alias: str = None

    def to_sql(self) -> str:
        sql = ""

        if self.partition:
            sql = f"PARTITION BY {', '.join(map(str, self.partition))}"

        sql = f"{sql} ORDER BY {', '.join(map(str, self.order))}"

        sql = f"FIRST_VALUE({self.property}) OVER ({sql})"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
