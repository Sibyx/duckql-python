from typing import Union

from backboneql.functions.base import BaseFunction
from backboneql.properties.constant import Constant
from backboneql.properties.property import Property


class GroupConcat(BaseFunction):
    property: Union[Constant, Property, BaseFunction]
    alias: str = None

    def to_sql(self) -> str:
        # TODO: postgresql
        sql = f"GROUP_CONCAT({self.property})"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
