from typing import List

from typing_extensions import Literal

from backboneql.base import BaseType
from backboneql.properties.constant import Constant


class Array(BaseType):
    obj: Literal['array'] = 'array'
    values: List[Constant]

    def to_sql(self) -> str:
        return f'({", ".join(map(str, self.values))})'
