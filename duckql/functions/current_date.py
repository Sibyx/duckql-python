try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..functions.base import BaseFunction


class CurrentDate(BaseFunction):
    obj: Literal['functions.CurrentDate'] = 'functions.CurrentDate'
    alias: str = None

    def to_sql(self) -> str:
        sql = "CURRENT_DATE()"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
