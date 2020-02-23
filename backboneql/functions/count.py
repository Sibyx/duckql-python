from backboneql.functions.base import BaseFunction
from backboneql.properties.property import Property


class Count(BaseFunction):
    property: Property
    alias: str = None

    def to_sql(self) -> str:
        sql = f"COUNT({self.property})"

        if self.alias:
            sql = f"{sql} AS {self.alias}"

        return sql
