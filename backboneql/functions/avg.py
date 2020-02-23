from typing import Union

from typing_extensions import Literal

from .base import BaseFunction
from backboneql.properties.property import Property


class Avg(BaseFunction):
    obj: Literal['avg'] = 'avg'
    property: Union[Property]
    alias: str = None

    def to_sql(self) -> str:
        sql = f"AVG({self.property})"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
