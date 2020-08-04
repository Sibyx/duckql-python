from typing import Union

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..functions.base import BaseFunction
from ..properties.property import Property
from ..structures.cast_operator import CastOperator


class Sum(BaseFunction):
    obj: Literal['functions.Sum'] = 'functions.Sum'
    property: Union[Property, BaseFunction, CastOperator]
    alias: str = None

    def to_sql(self) -> str:
        sql = f"SUM({self.property})"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
