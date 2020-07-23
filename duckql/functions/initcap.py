from typing import Union

from typing_extensions import Literal

from .base import BaseFunction
from ..properties import Constant
from ..properties.property import Property
from ..structures.cast_operator import CastOperator


class InitCap(BaseFunction):
    obj: Literal['functions.InitCap'] = 'functions.InitCap'
    property: Union[Property, BaseFunction, Constant, CastOperator]
    alias: str = None

    def to_sql(self) -> str:
        sql = f"initcap({self.property})"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
