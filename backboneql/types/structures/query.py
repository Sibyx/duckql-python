from dataclasses import field
from typing import List

from pydantic.dataclasses import dataclass

from backboneql.types.base import BaseType
from backboneql.types.structures.join import Join


@dataclass
class Query(BaseType):
    entity: str
    properties: List[BaseType] = field(default_factory=list)
    joins: List[Join] = field(default_factory=list)
    conditions: List = field(default_factory=list)

    def to_sql(self) -> str:
        sql = f"SELECT {', '.join(map(str, self.properties))} FROM {self.entity}"
        return sql
