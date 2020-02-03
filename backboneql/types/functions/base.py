from abc import ABC

from pydantic.dataclasses import dataclass

from backboneql.types.base import BaseType


@dataclass
class BaseFunction(BaseType, ABC):
    pass
