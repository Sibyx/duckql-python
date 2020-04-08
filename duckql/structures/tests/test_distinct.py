import pytest

from duckql.exceptions import ParseError
from duckql.properties import Property
from duckql.structures import Distinct


def test_simple():
    my_distinct = Distinct(
        property=Property(name='users.name')
    )

    assert str(my_distinct) == 'DISTINCT users.name'


def test_parse_error():
    with pytest.raises(ParseError):
        Distinct(
            property=Property(
                name='users.name',
                alias="my_name"
            )
        )
