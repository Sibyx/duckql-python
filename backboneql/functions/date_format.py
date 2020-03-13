from typing import Union

from pydantic import validator
from typing_extensions import Literal

from ..functions.base import BaseFunction
from ..properties.property import Property
from ..properties.constant import Constant
from ..structures.cast_operator import CastOperator


class DateFormat(BaseFunction):
    obj: Literal['functions.DateFormat'] = 'functions.DateFormat'
    property: Union[Property, Constant, BaseFunction, CastOperator]
    format: str
    alias: str = None

    @validator('format', pre=True)
    def sanitize_format(cls, v):
        return cls.escape(v, ['%'])

    def to_sql(self) -> str:
        sql = f"DATE_FORMAT({self.property}, '{self.format}')"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
