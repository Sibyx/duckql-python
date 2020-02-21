from typing import Union, List

from pydantic.dataclasses import dataclass

from backboneql.exceptions import ParseError
from backboneql.base import BaseType
from backboneql.functions.base import BaseFunction
from backboneql.properties.property import Property
from backboneql.properties.constant import Constant


@dataclass
class Between(BaseType):
    property: Union[BaseFunction, Property, Constant]
    values: List[Union[BaseFunction, Constant, Property]]

    def __post_init__(self):
        if len(self.values) != 2:
            raise ParseError("Between requires exactly two attributes!")

    def to_sql(self) -> str:
        return f"{self.property} BETWEEN {self.values[0]} AND {self.values[1]}"
