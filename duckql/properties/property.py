from duckql.exceptions import ParseError

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

    def to_sql(self) -> str:
        if '->>' in self.name:
            bits = self.name.split('->>')
            if len(bits) != 2:
                raise ParseError("duckQL doesn't support nested JSON lookups (yet).")
            self.name = f"{self.escape(bits[0].strip())} ->> '{self.escape(bits[1].strip())}'"
        else:
            self.name = self.escape(self.name)

        sql = f"{self.name}"

        if self.alias is not None:
            sql = f'{sql} AS "{self.alias}"'

        return sql
