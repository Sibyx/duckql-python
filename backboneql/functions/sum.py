from typing import Union

from backboneql.functions.base import BaseFunction
from backboneql.properties.property import Property


class Sum(BaseFunction):
    property: Union[Property, BaseFunction]
    alias: str = None

    def to_sql(self) -> str:
        sql = f"SUM({self.property})"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
