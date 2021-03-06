import pytest

from duckql.exceptions import ParseError
from duckql.functions.count import Count
from duckql.properties.property import Property
from duckql.structures.distinct import Distinct


def test_simple():
    my_count = Count(
        property=Property(name='users.id'),
        alias='user"_count'
    )

    assert str(my_count) == "COUNT(users.id) AS user_count"


def test_parse_error():
    with pytest.raises(ParseError):
        Count(
            property=Property(name='users.name', alias='name')
        )


def test_distinct():
    my_count = Count(
        property=Distinct(
            property=Property(name='users.id')
        ),
        alias='distinct_count'
    )
    assert str(my_count) == "COUNT(DISTINCT users.id) AS distinct_count"
