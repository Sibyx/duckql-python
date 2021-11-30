from typing import List, Union, Optional

from pydantic import BaseModel

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..base import BaseType
from ..properties.property import Property
from ..properties.constant import Constant
from ..structures.comparision import Comparision
from ..structures.operator import Operator
from ..functions.base import BaseFunction


class Case(BaseType):
    # TODO: Docs!
    class Condition(BaseModel):
        when: Comparision
        then: Union[BaseFunction, Property, Constant, Operator]

        def __str__(self):
            return f"WHEN {self.when} THEN {self.then}"

    obj: Literal['structures.Case'] = 'structures.Case'
    conditions: List[Condition]
    alternative: Optional[Union[BaseFunction, Property, Constant]] = None
    alias: str = None

    def to_sql(self) -> str:
        sql = "CASE " + " ".join(map(str, self.conditions))
        if self.alternative:
            sql = f"{sql} ELSE {self.alternative}"

        sql = f"({sql} END)"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
