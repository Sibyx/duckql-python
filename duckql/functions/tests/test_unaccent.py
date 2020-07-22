from duckql.functions.unaccent import Unaccent
from duckql.properties.property import Property


def test_property():
    my_function = Unaccent(property=Property(name='users.name'))

    assert str(my_function) == 'unaccent(users.name)'


def test_alias():
    my_function = Unaccent(property=Property(name='users.name'), alias='"avg_name')

    assert str(my_function) == 'unaccent(users.name) AS avg_name'
