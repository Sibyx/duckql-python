from typing import Union

from pydantic import validator

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..functions.base import BaseFunction
from ..properties.property import Property
from ..properties.constant import Constant
from ..structures.cast_operator import CastOperator


class ToDate(BaseFunction):
    obj: Literal['functions.ToDate'] = 'functions.ToDate'
    property: Union[Property, Constant, BaseFunction, CastOperator]
    format: str
    alias: str = None

    @validator('format', pre=True)
    def sanitize_format(cls, v):
        return cls.escape(v)

    def to_sql(self) -> str:
        sql = f"to_date({self.property}, '{self.format}')"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
