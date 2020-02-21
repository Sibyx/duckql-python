from typing import Union

from pydantic.dataclasses import dataclass

from backboneql.exceptions import ParseError
from backboneql.functions.base import BaseFunction
from backboneql.properties.constant import Constant
from backboneql.properties.property import Property


@dataclass
class ConvertTimezone(BaseFunction):
    property: Union[Property, BaseFunction, Constant]
    date_from: Constant
    date_to: Constant
    alias: str = None

    def __post_init__(self):
        if hasattr(self, 'alias') and self.alias is not None:
            self.alias = self.escape(self.alias)

        if hasattr(self.property, 'alias') and self.property.alias is not None:
            raise ParseError("You can't have alias inside of function!")

    def to_sql(self) -> str:
        """
        TODO: not supported in PostgreSQL
        https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_convert-tz MySQL
        https://mariadb.com/kb/en/library/convert_tz/ MariaDB
        :return: str
        """
        sql = f"CONVERT_TZ({self.property}, {self.date_from}, {self.date_to})"

        if self.alias is not None:
            sql = f"{sql} AS {self.alias}"

        return sql
