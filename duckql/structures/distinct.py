from typing import Union

from duckql.functions.base import BaseFunction

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from duckql.base import BaseType
from duckql.properties.property import Property


class Distinct(BaseType):
    obj: Literal['structures.Distinct'] = 'structures.Distinct'
    property: Union[Property, BaseFunction]

    def to_sql(self) -> str:
        return f"DISTINCT {self.property}"
