from pydantic.dataclasses import dataclass

from backboneql.types.base import BaseType


@dataclass
class Null(BaseType):
    def to_sql(self) -> str:
        return 'NULL'
