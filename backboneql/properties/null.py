from typing_extensions import Literal

from backboneql.base import BaseType


class Null(BaseType):
    obj: Literal['null'] = 'null'

    def to_sql(self) -> str:
        return 'NULL'
