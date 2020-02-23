from backboneql.properties import Property
from backboneql.structures import Order


def test_simple():
    my_order = Order(
        property=Property(name='users.name')
    )

    assert str(my_order) == 'users.name ASC'


def test_descending():
    my_order = Order(
        property=Property(name='users.name'),
        kind=Order.Direction.DESC
    )

    assert str(my_order) == 'users.name DESC'
