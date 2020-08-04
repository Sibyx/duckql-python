from typing import Union, List

from duckql.functions.base import BaseFunction
from pydantic import validator

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..exceptions import ParseError
from ..base import BaseType
from ..properties.property import Property
from ..properties.constant import Constant


class Between(BaseType):
    obj: Literal['structures.Between'] = 'structures.Between'
    property: Union[BaseFunction, Property, Constant]
    values: List[Union[BaseFunction, Constant, Property]]

    @validator('values', pre=True)
    def check_number_of_attributes(cls, v):
        if len(v) != 2:
            raise ParseError("Between requires exactly two attributes!")
        return v

    def to_sql(self) -> str:
        return f"{self.property} BETWEEN {self.values[0]} AND {self.values[1]}"
