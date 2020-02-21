import pytest

from backboneql.exceptions import ParseError
from backboneql.functions.count import Count
from backboneql.properties.property import Property


def test_simple():
    my_count = Count(Property('users.id'), alias='user"_count')

    assert str(my_count) == "COUNT(users.id) AS user_count"


def test_parse_error():
    with pytest.raises(ParseError):
        Count(Property('users.name', alias='name'))
