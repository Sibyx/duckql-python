from backboneql.types.properties import Property, Constant
from backboneql.types.structures import Between


def test_simple():
    my_structure = Between(Property('transactions.happened_at'), [Constant('2020-01-01'), Constant('2020-02-01')])

    assert str(my_structure) == "transactions.happened_at BETWEEN '2020-01-01' AND '2020-02-01'"
