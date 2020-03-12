from typing import Union

from pydantic import validator
from typing_extensions import Literal

from ..functions.base import BaseFunction
from ..properties.property import Property


class StringAgg(BaseFunction):
    obj: Literal['functions.StringAgg'] = 'functions.StringAgg'
    property: Union[Property, BaseFunction]
    separator: str
    alias: str = None

    @validator('separator', pre=True)
    def sanitize_separator(cls, v):
        return cls.escape(v)

    def to_sql(self) -> str:
        sql = f"STRING_AGG({self.property}, {self.separator})"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
