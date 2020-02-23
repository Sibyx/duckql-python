from backboneql.properties import Property, Constant
from backboneql.structures import Between


def test_simple():
    my_structure = Between(
        property=Property(name='transactions.happened_at'),
        values=[
            Constant(value='2020-01-01'),
            Constant(value='2020-02-01')
        ]
    )

    assert str(my_structure) == "transactions.happened_at BETWEEN '2020-01-01' AND '2020-02-01'"
