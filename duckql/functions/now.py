try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from .base import BaseFunction


class Now(BaseFunction):
    obj: Literal['functions.Avg'] = 'functions.Now'
    alias: str = None

    def to_sql(self) -> str:
        sql = "NOW()"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
