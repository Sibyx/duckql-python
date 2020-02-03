import pytest

from backboneql.exceptions import ParseError
from backboneql.types.functions.concat import Concat
from backboneql.types.properties import Property, Constant


def test_simple():
    my_concat = Concat([Property('users.name'), Constant(' '), Property('users.surname')], alias='"full_name')

    assert str(my_concat) == "CONCAT(users.name, ' ', users.surname) AS full_name"


def test_parse_error():
    with pytest.raises(ParseError):
        Concat([Property('users.name'), Constant(' '), Property('users.surname', alias='al')], alias='full_name')
