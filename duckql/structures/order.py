from enum import Enum
from typing import Union

from duckql.functions.base import BaseFunction
from typing_extensions import Literal

from ..base import BaseType
from ..properties.property import Property


class Order(BaseType):
    class Direction(Enum):
        ASC = 'ASC'
        DESC = 'DESC'

    obj: Literal['structures.Order'] = 'structures.Order'
    property: Union[Property, BaseFunction]
    kind: Direction = Direction.ASC

    def to_sql(self) -> str:
        return f"{self.property} {self.kind.value}"
