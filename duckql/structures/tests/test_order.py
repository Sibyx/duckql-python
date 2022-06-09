from duckql import CastOperator
from duckql.properties import Property
from duckql.structures import Order


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


def test_cast():
    my_order = Order(
        property=CastOperator(
            property=Property(name='users.additional_data -> custom_fields ->> age'),
            to=CastOperator.DataType.INT
        )
    )

    assert str(my_order) == "(users.additional_data -> 'custom_fields' ->> 'age')::int ASC"
