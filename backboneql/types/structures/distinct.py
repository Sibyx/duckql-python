from typing import Union

from pydantic.dataclasses import dataclass

from backboneql.exceptions import ParseError
from backboneql.types.base import BaseType
from backboneql.types.functions.base import BaseFunction
from backboneql.types.properties import Property


@dataclass
class Distinct(BaseType):
    property: Union[Property, BaseFunction]

    def __post_init__(self):
        if hasattr(self.property, 'alias') and self.property.alias:
            raise ParseError("You can't have alias inside of distinct!")

    def to_sql(self) -> str:
        return f"DISTINCT {self.property}"
