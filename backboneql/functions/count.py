from typing_extensions import Literal

from ..functions.base import BaseFunction
from ..properties.property import Property


class Count(BaseFunction):
    obj: Literal['functions.Count'] = 'functions.Count'
    property: Property
    alias: str = None

    def to_sql(self) -> str:
        sql = f"COUNT({self.property})"

        if self.alias:
            sql = f"{sql} AS {self.alias}"

        return sql
