from backboneql.functions.sum import Sum
from backboneql.properties.property import Property


def test_simple():
    my_function = Sum(
        property=Property(name='transactions.amount'),
        alias='total_amount'
    )

    assert str(my_function) == 'SUM(transactions.amount) AS total_amount'
