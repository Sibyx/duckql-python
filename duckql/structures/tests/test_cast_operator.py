from duckql.properties import Property
from duckql.structures.cast_operator import CastOperator


def test_simple():
    my_structure = CastOperator(
        property=Property(name='users.age'),
        to=CastOperator.DataType.VARCHAR,
        alias='age_as_string'
    )

    assert str(my_structure) == 'users.age::varchar AS age_as_string'


def test_json_field():
    my_structure = CastOperator(
        property=Property(name='organisations.statistics->campaigns_count'),
        to=CastOperator.DataType.INT,
        alias='campaigns_count'
    )

    assert str(my_structure) == '(organisations.statistics ->> \'campaigns_count\')::int AS campaigns_count'
