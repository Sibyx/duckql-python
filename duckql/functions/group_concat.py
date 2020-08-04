from typing import Union

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..functions.base import BaseFunction
from ..properties.constant import Constant
from ..properties.property import Property
from ..structures.cast_operator import CastOperator


class GroupConcat(BaseFunction):
    obj: Literal['functions.GroupConcat'] = 'functions.GroupConcat'
    property: Union[Constant, Property, BaseFunction, CastOperator]
    alias: str = None

    def to_sql(self) -> str:
        # TODO: postgresql
        sql = f"GROUP_CONCAT({self.property})"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
