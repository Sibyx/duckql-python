from decimal import Decimal
from typing import Union

from pydantic.dataclasses import dataclass

from backboneql.base import BaseType


@dataclass
class Constant(BaseType):
    value: Union[str, int, float, Decimal]

    def __post_init__(self):
        self.value = self.escape(str(self.value))

    def to_sql(self) -> str:
        sql = f"{self.value}"

        if not sql.isnumeric():
            sql = f"'{sql}'"

        return sql
