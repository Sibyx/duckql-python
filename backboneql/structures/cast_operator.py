from enum import Enum
from typing import Union

from typing_extensions import Literal

from ..base import BaseType
from ..properties.property import Property
from ..properties.constant import Constant
from ..functions.base import BaseFunction


class CastOperator(BaseType):
    class DataType(Enum):
        # Boolean
        BOOLEAN = 'boolean'
        BOOL = 'bool'

        # Character
        CHAR = 'char'
        VARCHAR = 'varchar'
        TEXT = 'text'

    obj: Literal['structures.Distinct'] = 'structures.CastOperator'
    property: Union[Constant, Property, BaseFunction]
    to: DataType

    def to_sql(self) -> str:
        return f"{self.property}::{self.to}"
