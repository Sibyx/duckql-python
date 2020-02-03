from pydantic.dataclasses import dataclass

from backboneql.types.base import BaseType


@dataclass
class Join(BaseType):
    def to_sql(self) -> str:
        pass
