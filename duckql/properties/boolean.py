try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..base import BaseType


class Boolean(BaseType):
    obj: Literal['properties.Boolean'] = 'properties.Boolean'
    value: bool

    class Config:
        title = "Boolean"
        schema_extra = {
            'description': 'Object representation of SQL boolean'
        }

    def to_sql(self) -> str:
        return 'TRUE' if self.value else 'FALSE'
