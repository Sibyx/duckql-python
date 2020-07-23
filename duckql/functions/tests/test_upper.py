from duckql.properties.property import Property
from duckql.functions.upper import Upper


def test_property():
    my_function = Upper(property=Property(name='users.name'))

    assert str(my_function) == 'upper(users.name)'


def test_alias():
    my_function = Upper(property=Property(name='users.name'), alias='"upper_name')

    assert str(my_function) == 'upper(users.name) AS upper_name'
