import pytest

from backboneql.exceptions import ParseError
from backboneql.types.functions.avg import Avg
from backboneql.types.properties import Property


def test_property():
    my_avg = Avg(Property('users.name'))

    assert str(my_avg) == 'AVG(users.name)'


def test_alias():
    my_avg = Avg(Property('users.name'), alias='"avg_name')

    assert str(my_avg) == 'AVG(users.name) AS avg_name'


def test_parse_error():
    with pytest.raises(ParseError):
        Avg(Property('users.name', alias='name'))
