from enum import Enum
from typing import List, Union

from duckql.functions.base import BaseFunction

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..base import BaseType
from ..properties.constant import Constant
from ..properties.property import Property
from ..properties.boolean import Boolean
from ..structures.interval import Interval
from .comparision import Comparision


class Operator(BaseType):
    class Operation(Enum):
        AND = 'and'
        OR = 'or'
        DIVISION = 'division'
        MULTIPLICATION = 'multiplication'
        SUBTRACTION = 'subtraction'
        ADDITION = 'addition'

        def __str__(self):
            mapping = {
                self.AND: 'AND',
                self.OR: 'OR',
                self.DIVISION: '/',
                self.MULTIPLICATION: '*',
                self.SUBTRACTION: '-',
                self.ADDITION: '+'
            }

            try:
                return mapping[self]
            except KeyError:
                raise ValueError(f"{self.value} doesnt have valid string representation specified!")

    obj: Literal['structures.Operator'] = 'structures.Operator'
    operation: Operation
    properties: List[Union[BaseFunction, Constant, Property, Boolean, Comparision, Interval]]
    alias: str = None

    def to_sql(self) -> str:
        sql = f' {self.operation} '.join(map(str, self.properties))
        sql = f"({sql})"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
