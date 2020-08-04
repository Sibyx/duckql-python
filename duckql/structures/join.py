from enum import Enum
from typing import Union

from pydantic import validator

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..base import BaseType
from .operator import Operator
from .comparision import Comparision


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
        NATURAL = 'natural'

        def __str__(self):
            mapping = {
                self.LEFT: 'LEFT',
                self.RIGHT: 'RIGHT',
                self.INNER: 'INNER',
                self.OUTER: 'OUTER',
                self.CROSS: 'CROSS',
                self.FULL_OUTER: 'FULL OUTER',
                self.LEFT_OUTER: 'LEFT OUTER',
                self.RIGHT_OUTER: 'RIGHT OUTER',
                self.NATURAL: 'NATURAL'
            }

            try:
                return mapping[self]
            except KeyError:
                raise ValueError(f"{self.value} doesnt have valid string representation specified!")

    obj: Literal['structures.Join'] = 'structures.Join'
    entity: str
    type: Type
    on: Union[Comparision, Operator] = []
    alias: str = None

    @validator('entity', pre=True)
    def escape_entity(cls, v):
        return cls.escape(v)

    def to_sql(self) -> str:
        sql = f"{self.type} JOIN {self.entity}"

        if self.alias is not None:
            sql = f"{sql} {self.alias}"

        if self.type != self.Type.NATURAL:
            sql = f"{sql} ON {self.on}"

        return sql
