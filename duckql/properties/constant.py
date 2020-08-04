from decimal import Decimal
from typing import Union

from pydantic import validator

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..base import BaseType


class Constant(BaseType):
    obj: Literal['properties.Constant'] = 'properties.Constant'
    value: Union[str, int, float, Decimal]

    class Config:
        title = "Constant"
        schema_extra = {
            'description': "Object representation of alphanumeric constant"
        }

    @validator('value', pre=True)
    def escape_value(cls, v):
        return cls.escape(str(v))

    def to_sql(self) -> str:
        sql = f"{self.value}"

        if not sql.isnumeric():
            sql = f"'{sql}'"

        return sql
