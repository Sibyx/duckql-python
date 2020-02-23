from typing import Union

from typing_extensions import Literal

from backboneql.functions.base import BaseFunction
from backboneql.properties.property import Property


class Sum(BaseFunction):
    obj: Literal['sum'] = 'sum'
    property: Union[Property, BaseFunction]
    alias: str = None

    def to_sql(self) -> str:
        sql = f"SUM({self.property})"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
