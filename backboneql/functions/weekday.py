from typing import Union

from typing_extensions import Literal

from ..functions.base import BaseFunction
from ..properties.property import Property
from ..properties.constant import Constant


class Weekday(BaseFunction):
    obj: Literal['functions.Weekday'] = 'functions.Weekday'
    property: Union[Property, BaseFunction, Constant]
    alias: str = None

    def to_sql(self) -> str:
        # TODO: postgresql
        sql = f"WEEKDAY({self.property})"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
