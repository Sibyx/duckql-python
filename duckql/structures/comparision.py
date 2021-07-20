from enum import Enum
from typing import List

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from duckql.base import BaseType
from duckql.properties.array import Array


class Comparision(BaseType):
    class Operation(Enum):
        EQUAL = 'eq'
        NOT_EQUAL = 'neq'
        LOWER = 'lt'
        LOWER_EQUAL = 'lte'
        GREATER = 'gt'
        GREATER_EQUAL = 'gte'
        LIKE = 'like'
        IN = 'in'
        NOT_LIKE = 'nlike'
        NOT_IN = 'nin'
        IS = 'is'
        IS_NOT = 'nis'
        CONTAINS = 'contains'

        def __str__(self):
            mapping = {
                self.EQUAL: '=',
                self.NOT_EQUAL: '!=',
                self.LOWER: '<',
                self.LOWER_EQUAL: '<=',
                self.GREATER: '>',
                self.GREATER_EQUAL: '>=',
                self.LIKE: 'LIKE',
                self.IN: 'IN',
                self.NOT_LIKE: 'NOT LIKE',
                self.NOT_IN: 'NOT IN',
                self.IS: 'IS',
                self.IS_NOT: 'IS NOT',
                self.CONTAINS: 'CONTAINS'
            }

            try:
                return mapping[self]
            except KeyError:
                raise ValueError(f"{self.value} doesnt have valid string representation specified!")

        @classmethod
        def containers(cls) -> List["Comparision.Operation"]:
            return [cls.NOT_IN, cls.IN]

    obj: Literal['structures.Comparision'] = 'structures.Comparision'
    properties: List[BaseType]
    operation: Operation

    def to_sql(self) -> str:
        sql = f"{self.properties[0]} {self.operation}"

        if not isinstance(self.properties[1], Array) and self.operation in Comparision.Operation.containers():
            sql = f"{sql} ({self.properties[1]})"
        else:
            sql = f"{sql} {self.properties[1]}"

        return f"({sql})"
