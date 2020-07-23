from duckql.properties.property import Property
from duckql.functions.initcap import InitCap


def test_property():
    my_function = InitCap(property=Property(name='users.name'))

    assert str(my_function) == 'initcap(users.name)'


def test_alias():
    my_function = InitCap(property=Property(name='users.name'), alias='"capitalized')

    assert str(my_function) == 'initcap(users.name) AS capitalized'
