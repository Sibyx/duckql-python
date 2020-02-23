from typing import Union

from pydantic import validator
from typing_extensions import Literal

from backboneql.functions.base import BaseFunction
from backboneql.properties.property import Property
from backboneql.properties.constant import Constant


class DateFormat(BaseFunction):
    obj: Literal['date_format'] = 'date_format'
    property: Union[Property, Constant, BaseFunction]
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
