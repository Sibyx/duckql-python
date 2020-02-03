from pydantic.dataclasses import dataclass

from backboneql.types.base import BaseType


@dataclass
class Property(BaseType):
    name: str
    alias: str = None

    def __post_init__(self):
        self.name = self.escape(self.name)

        if self.alias is not None:
            self.alias = self.escape(self.alias)

    def to_sql(self) -> str:
        sql = f"{self.name}"

        if self.alias is not None:
            sql = f'{sql} AS "{self.alias}"'

        return sql
