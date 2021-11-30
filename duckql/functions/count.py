from typing import Union

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..functions.base import BaseFunction
from ..properties import Constant
from ..properties.property import Property
from ..structures.cast_operator import CastOperator
from ..structures.distinct import Distinct
from ..structures.case import Case


class Count(BaseFunction):
    obj: Literal['functions.Count'] = 'functions.Count'
    property: Union[Property, BaseFunction, Constant, CastOperator, Distinct, Case]
    alias: str = None

    def to_sql(self) -> str:
        sql = f"COUNT({self.property})"

        if self.alias:
            sql = f"{sql} AS {self.alias}"

        return sql
