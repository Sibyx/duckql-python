from typing import List

from typing_extensions import Literal

from ..base import BaseType
from ..properties.constant import Constant


class Array(BaseType):
    obj: Literal['properties.Array'] = 'properties.Array'
    values: List[Constant]

    def to_sql(self) -> str:
        return f'({", ".join(map(str, self.values))})'
