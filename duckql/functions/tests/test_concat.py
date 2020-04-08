import pytest

from duckql.exceptions import ParseError
from duckql.functions import Concat
from duckql.properties.property import Property
from duckql.properties.constant import Constant


def test_simple():
    my_concat = Concat(
        properties=[
            Property(name='users.name'),
            Constant(value=' '),
            Property(name='users.surname')
        ],
        alias='"full_name'
    )

    assert str(my_concat) == "CONCAT(users.name, ' ', users.surname) AS full_name"


def test_parse_error():
    with pytest.raises(ParseError):
        Concat(
            properties=[
                Property(name='users.name'),
                Constant(value=' '),
                Property(name='users.surname', alias='al')
            ],
            alias='full_name'
        )
