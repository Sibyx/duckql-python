from typing import Union

from backboneql.functions.base import BaseFunction
from typing_extensions import Literal

from backboneql.base import BaseType
from backboneql.properties.property import Property


class Distinct(BaseType):
    obj: Literal['structures.Distinct'] = 'structures.Distinct'
    property: Union[Property, BaseFunction]

    def to_sql(self) -> str:
        return f"DISTINCT {self.property}"
