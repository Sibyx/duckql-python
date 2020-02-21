from abc import ABC

from pydantic.dataclasses import dataclass

from backboneql.base import BaseType


@dataclass
class BaseFunction(BaseType, ABC):
    pass
