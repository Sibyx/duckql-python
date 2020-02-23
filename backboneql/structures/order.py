from enum import Enum
from typing import Union

from backboneql.base import BaseType
from backboneql.functions.base import BaseFunction
from backboneql.properties.property import Property


class Order(BaseType):
    class Direction(Enum):
        ASC = 'ASC'
        DESC = 'DESC'

    property: Union[Property, BaseFunction]
    kind: Direction = Direction.ASC

    def to_sql(self) -> str:
        return f"{self.property} {self.kind.value}"
