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
            bits = []

            for i, bit in enumerate(self.name.split('->>')):
                # Escape all nested attributes
                bit = self.escape(bit).strip()

                # Put all nested JSON fields into apostrophes
                # Zero index is a column name, which we don't want to have in apostrophes
                if i > 0:
                    bit = f"'{bit}'"

                bits.append(bit)

            self.name = ' ->> '.join(bits)
        else:
            self.name = self.escape(self.name)

        sql = f"{self.name}"

        if self.alias is not None:
            sql = f'{sql} AS "{self.alias}"'

        return sql
