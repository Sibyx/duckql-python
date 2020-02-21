from pydantic.dataclasses import dataclass

from backboneql.base import BaseType


@dataclass
class Null(BaseType):
    def to_sql(self) -> str:
        return 'NULL'
