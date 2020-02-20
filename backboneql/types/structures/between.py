from typing import Union, List

from pydantic.dataclasses import dataclass

from backboneql.exceptions import ParseError
from backboneql.types.base import BaseType
from backboneql.types.functions.base import BaseFunction
from backboneql.types.properties import Property, Constant


@dataclass
class Between(BaseType):
    property: Union[BaseFunction, Property, Constant]
    values: List[Union[BaseFunction, Constant, Property]]

    def __post_init__(self):
        if len(self.values) != 2:
            raise ParseError("Between requires exactly two attributes!")

    def to_sql(self) -> str:
        return f"{self.property} BETWEEN {self.values[0]} AND {self.values[1]}"
