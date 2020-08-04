from typing import List, Union

from .cast_operator import CastOperator
from ..functions.base import BaseFunction
from pydantic import validator

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..base import BaseType
from ..properties.property import Property
from .distinct import Distinct
from .operator import Operator
from .comparision import Comparision
from .order import Order
from .limit import Limit
from .join import Join


class Query(BaseType):
    class Config:
        title = 'Query'

    obj: Literal['structures.Query'] = 'structures.Query'
    entity: Union[str, 'Query']
    properties: List[Union[BaseFunction, Property, Distinct, CastOperator]]
    joins: List[Join] = []
    conditions: Union[Operator, Comparision] = None
    having: Union[Operator, Comparision] = None
    order: List[Order] = []
    group: List[Union[Property, BaseFunction]] = []
    limit: Limit = None
    alias: str = None

    @classmethod
    @validator('entity', pre=True)
    def escape_entity(cls, v):
        return cls.escape(v) if isinstance(v, str) else v

    def to_sql(self) -> str:
        sql = f"SELECT {', '.join(map(str, self.properties))} FROM {self.entity}"

        if self.joins:
            sql = f"{sql} {' '.join(map(str, self.joins))}"

        if self.conditions:
            sql = f"{sql} WHERE {self.conditions}"

        if self.group:
            sql = f"{sql} GROUP BY {', '.join(map(str, self.group))}"

        if self.having:
            sql = f"{sql} HAVING {self.having}"

        if self.order:
            sql = f"{sql} ORDER BY {', '.join(map(str, self.order))}"

        if self.limit:
            sql = f"{sql} {self.limit}"

        if self.alias:
            sql = f"({sql}) AS {self.alias}"

        return sql

    def _extract_properties(self, item: BaseType) -> List[Property]:
        if isinstance(item, Property):
            return [item]
        elif isinstance(item, list):
            my_properties = []
            for i in item:
                my_properties.extend(self._extract_properties(i))
            return my_properties
        elif hasattr(item, 'property'):
            return self._extract_properties(getattr(item, 'property', []))
        elif hasattr(item, 'properties'):
            return self._extract_properties(getattr(item, 'properties', []))
        else:
            return []

    @property
    def nested_properties(self) -> List[Property]:
        my_properties = []

        for item in self.properties:
            my_properties.extend(self._extract_properties(item))

        my_properties.extend(self._extract_properties(self.conditions))

        for item in self.order:
            my_properties.extend(self._extract_properties(item))

        for item in self.group:
            my_properties.extend(self._extract_properties(item))

        return my_properties
