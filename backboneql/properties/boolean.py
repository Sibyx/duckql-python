from typing_extensions import Literal

from ..base import BaseType


class Boolean(BaseType):
    obj: Literal['properties.Boolean'] = 'properties.Boolean'
    value: bool

    def to_sql(self) -> str:
        return 'TRUE' if self.value else 'FALSE'
