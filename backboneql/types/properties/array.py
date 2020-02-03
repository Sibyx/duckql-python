from typing import List

from pydantic.dataclasses import dataclass

from backboneql.types.base import BaseType
from backboneql.types.properties import Constant


@dataclass
class Array(BaseType):
    values: List[Constant]

    def to_sql(self) -> str:
        return f'({", ".join(map(str, self.values))})'
