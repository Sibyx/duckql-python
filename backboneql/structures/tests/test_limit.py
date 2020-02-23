import pytest
from pydantic import ValidationError

from backboneql.structures.limit import Limit


def test_simple():
    my_limit = Limit(limit=42)

    assert str(my_limit) == "LIMIT 42"


def test_offset():
    my_limit = Limit(limit=42, offset=5)

    assert str(my_limit) == "LIMIT 42 OFFSET 5"


def test_type_error():
    with pytest.raises(ValidationError):
        Limit(limit="bla")
