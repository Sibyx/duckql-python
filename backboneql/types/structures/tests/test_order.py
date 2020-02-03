import pytest
from pydantic import ValidationError

from backboneql.exceptions import ParseError
from backboneql.types.properties import Property, Constant
from backboneql.types.structures import Order


def test_simple():
    my_order = Order(Property('users.name'))

    assert str(my_order) == 'users.name ASC'


def test_descending():
    my_order = Order(Property('users.name'), Order.OrderDirection.DESC)

    assert str(my_order) == 'users.name DESC'


def test_syntax_error():
    with pytest.raises(ParseError):
        Order(Property('users.name', alias='name'))

    with pytest.raises(ValidationError):
        Order(Constant("Thor"))
