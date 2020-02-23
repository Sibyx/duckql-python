from typing_extensions import Literal

from backboneql.base import BaseType


class Boolean(BaseType):
    obj: Literal['boolean'] = 'boolean'
    value: bool

    def to_sql(self) -> str:
        return 'TRUE' if self.value else 'FALSE'
