from pydantic.dataclasses import dataclass

from backboneql.types.functions.base import BaseFunction


@dataclass
class CurrentDate(BaseFunction):
    alias: str = None

    def __post_init__(self):
        if self.alias is not None:
            self.alias = self.escape(self.alias)

    def to_sql(self) -> str:
        sql = "CURRENT_DATE()"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
