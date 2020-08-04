try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..base import BaseType


class Null(BaseType):
    obj: Literal['properties.Null'] = 'properties.Null'

    class Config:
        title = "Null"
        schema_extra = {
            'description': "Object representation of NULL"
        }

    def to_sql(self) -> str:
        return 'NULL'
