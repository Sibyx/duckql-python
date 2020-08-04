try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..base import BaseType


class Limit(BaseType):
    obj: Literal['structures.Limit'] = 'structures.Limit'
    limit: int
    offset: int = None

    def to_sql(self) -> str:
        sql = f"LIMIT {self.limit}"

        if self.offset is not None:
            sql = f"{sql} OFFSET {self.offset}"

        return sql
