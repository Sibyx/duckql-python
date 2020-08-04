from pydantic import validator

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..base import BaseType


class Property(BaseType):
    obj: Literal['properties.Property'] = 'properties.Property'
    name: str
    alias: str = None

    class Config:
        title = "Property"
        schema_extra = {
            'description': "Object representation of SQL column/property"
        }

    @validator('name', pre=True)
    def escape_name(cls, v):
        return cls.escape(v)

    def to_sql(self) -> str:
        sql = f"{self.name}"

        if self.alias is not None:
            sql = f'{sql} AS "{self.alias}"'

        return sql
