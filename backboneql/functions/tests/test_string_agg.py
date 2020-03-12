from backboneql.functions.string_agg import StringAgg
from backboneql.properties.property import Property


def test_simple():
    my_function = StringAgg(
        property=Property(name='transactions.amount'),
        separator=', ',
        alias='amounts'
    )

    assert 'STRING_AGG(transactions.amount, ', ') AS amounts' == str(my_function)
