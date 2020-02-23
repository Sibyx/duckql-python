from decimal import Decimal
from typing import Union

from pydantic import validator

from backboneql.base import BaseType


class Constant(BaseType):
    value: Union[str, int, float, Decimal]

    @validator('value', pre=True)
    def escape_value(cls, v):
        return cls.escape(str(v))

    def to_sql(self) -> str:
        sql = f"{self.value}"

        if not sql.isnumeric():
            sql = f"'{sql}'"

        return sql
