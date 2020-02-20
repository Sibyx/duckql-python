from backboneql.types.properties import Property, Constant
from backboneql.types.structures import Order


def test_simple():
    my_order = Order(Property('users.name'))

    assert str(my_order) == 'users.name ASC'


def test_descending():
    my_order = Order(Property('users.name'), Order.Direction.DESC)

    assert str(my_order) == 'users.name DESC'
