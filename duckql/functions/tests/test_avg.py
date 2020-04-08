import pytest

from duckql.exceptions import ParseError
from duckql.functions.avg import Avg
from duckql.properties.property import Property


def test_property():
    my_avg = Avg(property=Property(name='users.name'))

    assert str(my_avg) == 'AVG(users.name)'


def test_alias():
    my_avg = Avg(property=Property(name='users.name'), alias='"avg_name')

    assert str(my_avg) == 'AVG(users.name) AS avg_name'


def test_parse_error():
    with pytest.raises(ParseError):
        Avg(property=Property(name='users.name', alias='name'))
