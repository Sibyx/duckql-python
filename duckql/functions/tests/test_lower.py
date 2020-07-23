from duckql.properties.property import Property
from duckql.functions.lower import Lower


def test_property():
    my_function = Lower(property=Property(name='users.name'))

    assert str(my_function) == 'lower(users.name)'


def test_alias():
    my_function = Lower(property=Property(name='users.name'), alias='"lower_name')

    assert str(my_function) == 'lower(users.name) AS lower_name'
