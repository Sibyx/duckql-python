from backboneql.base import BaseType


class Null(BaseType):
    def to_sql(self) -> str:
        return 'NULL'
