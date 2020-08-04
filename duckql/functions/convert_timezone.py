from typing import Union

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..functions.base import BaseFunction
from ..properties.constant import Constant
from ..properties.property import Property
from ..structures.cast_operator import CastOperator


class ConvertTimezone(BaseFunction):
    obj: Literal['functions.ConvertTimezone'] = 'functions.ConvertTimezone'
    property: Union[Property, BaseFunction, Constant, CastOperator]
    date_from: Constant
    date_to: Constant
    alias: str = None

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
