from typing import Union

from backboneql.functions.base import BaseFunction
from backboneql.properties.property import Property


class Max(BaseFunction):
    property: Union[Property, BaseFunction]
    alias: str = None

    def to_sql(self) -> str:
        sql = f"MAX({self.property})"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql


class Min(BaseFunction):
    property: Union[Property, BaseFunction]
    alias: str = None

    def to_sql(self) -> str:
        sql = f"MIN({self.property})"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
