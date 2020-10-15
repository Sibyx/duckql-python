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
        if '->>' in self.name or '->' in self.name:
            sql = ''
            # WARNING: behaviour depends on params order in function multiple_separators_split
            bits = self.multiple_separators_split(('->>', '->'), self.name)

            for i, bit in enumerate(bits):
                # Escape all nested attributes
                bit = self.escape(bit).strip()

                # Put all nested JSON fields into apostrophes
                # Zero index is a column name, which we don't want to have in apostrophes
                if i == 0:
                    sql += bit
                elif i == len(bits) - 1:
                    sql += f" ->> '{bit}'"
                else:
                    sql += f" -> '{bit}'"
        else:
            self.name = self.escape(self.name)
            sql = self.name

        if self.alias is not None:
            sql = f'{sql} AS "{self.alias}"'

        return sql
