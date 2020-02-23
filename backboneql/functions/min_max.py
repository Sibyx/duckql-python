from typing import Union

from typing_extensions import Literal

from backboneql.functions.base import BaseFunction
from backboneql.properties.property import Property


class Max(BaseFunction):
    obj: Literal['max'] = 'max'
    property: Union[Property, BaseFunction]
    alias: str = None

    def to_sql(self) -> str:
        sql = f"MAX({self.property})"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql


class Min(BaseFunction):
    obj: Literal['min'] = 'min'
    property: Union[Property, BaseFunction]
    alias: str = None

    def to_sql(self) -> str:
        sql = f"MIN({self.property})"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
