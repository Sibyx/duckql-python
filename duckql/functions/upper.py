from typing import Union

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from .base import BaseFunction
from ..properties import Constant
from ..properties.property import Property
from ..structures.cast_operator import CastOperator
from ..structures.case import Case


class Upper(BaseFunction):
    obj: Literal['functions.Upper'] = 'functions.Upper'
    property: Union[Property, BaseFunction, Constant, CastOperator, Case]
    alias: str = None

    def to_sql(self) -> str:
        sql = f"upper({self.property})"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
