from typing import List, Union

from ..functions.base import BaseFunction
from pydantic import validator
from typing_extensions import Literal

from ..base import BaseType
from ..properties.property import Property
from .distinct import Distinct
from .operator import Operator
from .order import Order
from .limit import Limit
from .join import Join


class Query(BaseType):
    class Config:
        title = 'Query'

    obj: Literal['structures.Query'] = 'structures.Query'
    entity: str
    properties: List[Union[BaseFunction, Property, Distinct]]
    joins: List[Join]
    conditions: Operator = None
    order: List[Order]
    group: List[Union[Property, BaseFunction]]
    limit: Limit = None
    alias: str = None

    @validator('entity', pre=True)
    def escape_entity(cls, v):
        return cls.escape(v)

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
