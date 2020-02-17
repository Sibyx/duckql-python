from backboneql.types.functions.sum import Sum
from backboneql.types.properties import Property


def test_simple():
    my_function = Sum(Property('transactions.amount'), alias='total_amount')

    assert str(my_function) == 'SUM(transactions.amount) AS total_amount'
