from typing import Union

from typing_extensions import Literal

from backboneql.base import BaseType
from backboneql.functions.base import BaseFunction
from backboneql.properties.property import Property


class Distinct(BaseType):
    obj: Literal['distinct'] = 'distinct'
    property: Union[Property, BaseFunction]

    def to_sql(self) -> str:
        return f"DISTINCT {self.property}"
