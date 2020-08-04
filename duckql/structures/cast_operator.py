from enum import Enum
from typing import Union

try:
    from typing import Literal
except ImportError:
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

        # Integers
        SMALLINT = 'smallint'
        INTEGER = 'integer'
        INT = 'int'
        REAL = 'real'

        # Datetime
        TIMESTAMP = 'timestamp'
        DATE = 'date'

    obj: Literal['structures.Distinct'] = 'structures.CastOperator'
    property: Union[Constant, Property, BaseFunction]
    to: DataType
    alias: str = None

    def to_sql(self) -> str:
        sql = f"{self.property}::{self.to.value}"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
