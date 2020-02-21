from enum import Enum
from typing import Union

from pydantic.dataclasses import dataclass

from backboneql.exceptions import ParseError
from backboneql.base import BaseType
from backboneql.functions.base import BaseFunction
from backboneql.properties.property import Property


@dataclass
class Order(BaseType):
    class Direction(Enum):
        ASC = 'ASC'
        DESC = 'DESC'

    property: Union[Property, BaseFunction]
    kind: Direction = Direction.ASC

    def __post_init__(self):
        if hasattr(self.property, 'alias') and self.property.alias is not None:
            raise ParseError("You can't have alias in ORDER BY clause!")

    def to_sql(self) -> str:
        return f"{self.property} {self.kind.value}"
