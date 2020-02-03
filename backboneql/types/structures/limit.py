from pydantic.dataclasses import dataclass

from backboneql.types.base import BaseType


@dataclass
class Limit(BaseType):
    limit: int
    offset: int = None

    def to_sql(self) -> str:
        sql = f"LIMIT {self.limit}"

        if self.offset is not None:
            sql = f"{sql} OFFSET {self.offset}"

        return sql
