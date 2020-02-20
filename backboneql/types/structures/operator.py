from enum import Enum
from typing import List, Union

from pydantic.dataclasses import dataclass

from backboneql.exceptions import ParseError
from backboneql.types.base import BaseType
from backboneql.types.functions.base import BaseFunction
from backboneql.types.properties.constant import Constant
from backboneql.types.properties.property import Property
from backboneql.types.properties.boolean import Boolean
from backboneql.types.structures.comparision import Comparision


@dataclass
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

    operation: Operation
    properties: List[Union[BaseFunction, Constant, Property, Boolean, Comparision, "Operator"]]
    alias: str = None

    def __post_init__(self):
        if self.alias is not None:
            self.alias = self.escape(self.alias)

        if any(map(lambda x: hasattr(x, 'alias') and x.alias is not None, self.properties)):
            raise ParseError("You can't have alias inside of function!")

    def to_sql(self) -> str:
        sql = f' {self.operation} '.join(map(str, self.properties))
        sql = f"({sql})"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
