from typing import List

from backboneql.base import BaseType
from backboneql.properties.constant import Constant


class Array(BaseType):
    values: List[Constant]

    def to_sql(self) -> str:
        return f'({", ".join(map(str, self.values))})'
