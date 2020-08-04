from typing import Union

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..functions.base import BaseFunction
from ..properties.property import Property
from ..structures.cast_operator import CastOperator


class Max(BaseFunction):
    obj: Literal['functions.Max'] = 'functions.Max'
    property: Union[Property, BaseFunction, CastOperator]
    alias: str = None

    def to_sql(self) -> str:
        sql = f"MAX({self.property})"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql


class Min(BaseFunction):
    obj: Literal['functions.Min'] = 'functions.Min'
    property: Union[Property, BaseFunction, CastOperator]
    alias: str = None

    def to_sql(self) -> str:
        sql = f"MIN({self.property})"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
