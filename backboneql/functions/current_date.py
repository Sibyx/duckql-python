from typing_extensions import Literal

from backboneql.functions.base import BaseFunction


class CurrentDate(BaseFunction):
    obj: Literal['current_date'] = 'current_date'
    alias: str = None

    def to_sql(self) -> str:
        sql = "CURRENT_DATE()"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
