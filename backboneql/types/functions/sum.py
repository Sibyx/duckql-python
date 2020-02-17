from typing import Union

from pydantic.dataclasses import dataclass

from backboneql.exceptions import ParseError
from backboneql.types.functions.base import BaseFunction
from backboneql.types.properties import Property


@dataclass
class Sum(BaseFunction):
    property: Union[Property, BaseFunction]
    alias: str = None

    def __post_init__(self):
        if hasattr(self, 'alias') and self.alias is not None:
            self.alias = self.escape(self.alias)

        if hasattr(self.property, 'alias') and self.property.alias is not None:
            raise ParseError("You can't have alias inside of function!")

    def to_sql(self) -> str:
        sql = f"SUM({self.property})"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
