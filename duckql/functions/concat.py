from typing import List, Union

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..functions.base import BaseFunction
from ..properties.property import Property
from ..properties.constant import Constant
from ..structures.cast_operator import CastOperator


class Concat(BaseFunction):
    obj: Literal['functions.Concat'] = 'functions.Concat'
    properties: List[Union[Property, BaseFunction, Constant, CastOperator]]
    alias: str = None

    def to_sql(self) -> str:
        sql = f'CONCAT({", ".join(map(str, self.properties))})'

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
