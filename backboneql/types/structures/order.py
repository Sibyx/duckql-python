from enum import Enum
from typing import Union

from pydantic.dataclasses import dataclass

from backboneql.exceptions import ParseError
from backboneql.types.base import BaseType
from backboneql.types.functions.base import BaseFunction
from backboneql.types.properties import Property


@dataclass
class Order(BaseType):
    class OrderDirection(Enum):
        ASC = 'ASC'
        DESC = 'DESC'

    property: Union[Property, BaseFunction]
    kind: OrderDirection = OrderDirection.ASC

    def __post_init__(self):
        if hasattr(self.property, 'alias') and self.property.alias is not None:
            raise ParseError("You can't have alias in ORDER BY clause!")

    def to_sql(self) -> str:
        return f"{self.property} {self.kind.value}"
