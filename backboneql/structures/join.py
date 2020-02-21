from enum import Enum
from typing import Union

from pydantic.dataclasses import dataclass

from backboneql.base import BaseType
from .operator import Operator
from .comparision import Comparision


@dataclass
class Join(BaseType):
    class Type(Enum):
        LEFT = 'left'
        RIGHT = 'right'
        INNER = 'inner'
        OUTER = 'outer'
        CROSS = 'cross'
        FULL_OUTER = 'full_outer'
        LEFT_OUTER = 'left_outer'
        RIGHT_OUTER = 'right_outer'

        def __str__(self):
            mapping = {
                self.LEFT: 'LEFT',
                self.RIGHT: 'RIGHT',
                self.INNER: 'INNER',
                self.OUTER: 'OUTER',
                self.CROSS: 'CROSS',
                self.FULL_OUTER: 'FULL OUTER',
                self.LEFT_OUTER: 'LEFT OUTER',
                self.RIGHT_OUTER: 'RIGHT OUTER'
            }

            try:
                return mapping[self]
            except KeyError:
                raise ValueError(f"{self.value} doesnt have valid string representation specified!")

    entity: str
    type: Type
    on: Union[Comparision, Operator]
    alias: str = None

    def __post_init__(self):
        self.entity = self.escape(self.entity)
        if self.alias is not None:
            self.alias = self.escape(self.alias)

    def to_sql(self) -> str:
        sql = f"{self.type} JOIN {self.entity} ON {self.on}"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
