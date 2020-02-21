import pytest

from backboneql.exceptions import ParseError
from backboneql.functions import Concat
from backboneql.properties.property import Property
from backboneql.properties.constant import Constant


def test_simple():
    my_concat = Concat([Property('users.name'), Constant(' '), Property('users.surname')], alias='"full_name')

    assert str(my_concat) == "CONCAT(users.name, ' ', users.surname) AS full_name"


def test_parse_error():
    with pytest.raises(ParseError):
        Concat([Property('users.name'), Constant(' '), Property('users.surname', alias='al')], alias='full_name')
