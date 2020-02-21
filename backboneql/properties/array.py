from typing import List

from pydantic.dataclasses import dataclass

from backboneql.base import BaseType
from backboneql.properties.constant import Constant


@dataclass
class Array(BaseType):
    values: List[Constant]

    def to_sql(self) -> str:
        return f'({", ".join(map(str, self.values))})'
