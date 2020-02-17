from backboneql.types.functions.extract import Extract
from backboneql.types.properties import Property


def test_simple():
    my_function = Extract(
        Property('users.created_at'),
        Extract.Unit.CENTURY,
    )

    assert str(my_function) == 'EXTRACT(CENTURY FROM users.created_at)'
