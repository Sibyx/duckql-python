from typing import List, Union

from backboneql.functions.base import BaseFunction
from backboneql.properties.property import Property
from backboneql.properties.constant import Constant


class Concat(BaseFunction):
    properties: List[Union[Property, BaseFunction, Constant]]
    alias: str = None

    def to_sql(self) -> str:
        sql = f'CONCAT({", ".join(map(str, self.properties))})'

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
