from backboneql.functions.min_max import Max, Min
from backboneql.properties.property import Property


def test_min_simple():
    my_function = Min(
        property=Property(name='users.age'),
        alias='minimum_age'
    )

    assert str(my_function) == 'MIN(users.age) AS minimum_age'


def test_max_simple():
    my_function = Max(
        property=Property(name='users.age'),
        alias='maximum_age'
    )

    assert str(my_function) == 'MAX(users.age) AS maximum_age'
