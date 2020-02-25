from typing_extensions import Literal

from ..base import BaseType


class Null(BaseType):
    obj: Literal['properties.Null'] = 'properties.Null'

    def to_sql(self) -> str:
        return 'NULL'
