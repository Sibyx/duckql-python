import json
from typing import Dict

from duckql import Query


class QueryFactory:
    @classmethod
    def from_dict(cls, payload: Dict) -> Query:
        return Query.parse_raw(json.dumps(payload))

    @classmethod
    def from_json(cls, payload: str) -> Query:
        return Query.parse_raw(payload)

    @classmethod
    def from_msgpack(cls, payload) -> Query:
        try:
            import msgpack
        except ImportError:
            raise RuntimeError("msgpack is not installed!")

        return cls.from_dict(msgpack.loads(payload))

    @classmethod
    def from_bson(cls, payload) -> Query:
        try:
            import bson
        except ImportError:
            raise RuntimeError("bson is not installed!")

        return cls.from_dict(bson.loads(payload))
