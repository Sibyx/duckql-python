import pytest

from backboneql.exceptions import ParseError
from backboneql.types.properties import Property
from backboneql.types.structures import Distinct


def test_simple():
    my_distinct = Distinct(Property('users.name'))

    assert str(my_distinct) == 'DISTINCT users.name'


def test_parse_error():
    with pytest.raises(ParseError):
        Distinct(Property('users.name', alias="my_name"))
