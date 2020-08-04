from typing import List

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..base import BaseType
from ..properties.constant import Constant


class Array(BaseType):
    obj: Literal['properties.Array'] = 'properties.Array'
    values: List[Constant]

    class Config:
        title = "Array"
        schema_extra = {
            'description': "Object representation of SQL array"
        }

    def to_sql(self) -> str:
        return f'({", ".join(map(str, self.values))})'
