from typing import Union, List

from pydantic import validator

from backboneql.exceptions import ParseError
from backboneql.base import BaseType
from backboneql.functions.base import BaseFunction
from backboneql.properties.property import Property
from backboneql.properties.constant import Constant


class Between(BaseType):
    property: Union[BaseFunction, Property, Constant]
    values: List[Union[BaseFunction, Constant, Property]]

    @validator('values', pre=True)
    def check_number_of_attributes(cls, v):
        if len(v) != 2:
            raise ParseError("Between requires exactly two attributes!")
        return v

    def to_sql(self) -> str:
        return f"{self.property} BETWEEN {self.values[0]} AND {self.values[1]}"
