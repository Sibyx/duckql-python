from dataclasses import field
from typing import List, Union

from pydantic.dataclasses import dataclass

from backboneql.base import BaseType
from backboneql.functions.base import BaseFunction
from backboneql.properties.property import Property
from .operator import Operator
from .order import Order
from .limit import Limit
from .join import Join
from ..utils import BaseConfig


@dataclass(config=BaseConfig)
class Query(BaseType):
    entity: str
    properties: List[BaseType] = field(default_factory=list)
    joins: List[Join] = field(default_factory=list)
    conditions: Operator = None
    order: List[Order] = field(default_factory=list)
    group: List[Union[Property, BaseFunction]] = field(default_factory=list)
    limit: Limit = None
    alias: str = None

    def __post_init__(self):
        self.entity = self.escape(self.entity)

        if self.alias:
            self.alias = self.escape(self.alias)

    def to_sql(self) -> str:
        sql = f"SELECT {', '.join(map(str, self.properties))} FROM {self.entity}"

        if self.joins:
            sql = f"{sql} {' '.join(map(str, self.joins))}"

        if self.conditions:
            sql = f"{sql} WHERE {self.conditions}"

        if self.group:
            sql = f"{sql} GROUP BY {', '.join(map(str, self.group))}"

        if self.order:
            sql = f"{sql} ORDER BY {', '.join(map(str, self.order))}"

        if self.limit:
            sql = f"{sql} {self.limit}"

        if self.alias:
            sql = f"({sql}) AS {self.alias}"

        return sql
