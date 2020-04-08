from duckql.functions.extract import Extract
from duckql.properties.property import Property


def test_simple():
    my_function = Extract(
        property=Property(name='users.created_at'),
        unit=Extract.Unit.CENTURY,
    )

    assert str(my_function) == 'EXTRACT(CENTURY FROM users.created_at)'
