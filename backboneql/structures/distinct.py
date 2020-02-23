from typing import Union

from backboneql.base import BaseType
from backboneql.functions.base import BaseFunction
from backboneql.properties.property import Property


class Distinct(BaseType):
    property: Union[Property, BaseFunction]

    def to_sql(self) -> str:
        return f"DISTINCT {self.property}"
