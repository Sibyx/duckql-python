from backboneql.properties import Property
from backboneql.structures.cast_operator import CastOperator


def test_simple():
    my_structure = CastOperator(
        property=Property(name='users.age'),
        to=CastOperator.DataType.VARCHAR,
        alias='age_as_string'
    )

    assert str(my_structure) == 'users.age::varchar AS age_as_string'
