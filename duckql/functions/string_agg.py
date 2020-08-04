from typing import Union

from pydantic import validator

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..structures.distinct import Distinct
from ..functions.base import BaseFunction
from ..properties import Array
from ..properties.property import Property
from ..structures.cast_operator import CastOperator


class StringAgg(BaseFunction):
    obj: Literal['functions.StringAgg'] = 'functions.StringAgg'
    property: Union[Property, BaseFunction, Array, CastOperator, Distinct]
    separator: str
    alias: str = None

    @validator('separator', pre=True)
    def sanitize_separator(cls, v):
        return cls.escape(v)

    def to_sql(self) -> str:
        sql = f"STRING_AGG({self.property}, '{self.separator}')"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
