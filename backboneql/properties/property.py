from pydantic import validator

from backboneql.base import BaseType


class Property(BaseType):
    name: str
    alias: str = None

    @validator('name', pre=True)
    def escape_name(cls, v):
        return cls.escape(v)

    def to_sql(self) -> str:
        sql = f"{self.name}"

        if self.alias is not None:
            sql = f'{sql} AS "{self.alias}"'

        return sql
