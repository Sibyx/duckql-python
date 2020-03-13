from backboneql.functions.string_agg import StringAgg
from backboneql.properties.property import Property
from backboneql.structures.cast_operator import CastOperator


def test_simple():
    my_function = StringAgg(
        property=Property(name='transactions.amount'),
        separator=', ',
        alias='amounts'
    )

    assert "STRING_AGG(transactions.amount, ', ') AS amounts" == str(my_function)


def test_advanced():
    my_function = StringAgg(
        property=CastOperator(
            property=Property(name='transactions.amount'),
            to=CastOperator.DataType.VARCHAR
        ),
        separator=', ',
        alias='amounts'
    )

    assert "STRING_AGG(transactions.amount::varchar, ', ') AS amounts" == str(my_function)
