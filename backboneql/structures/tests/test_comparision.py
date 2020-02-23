from backboneql.properties import Property, Array, Constant
from backboneql.structures import Comparision


def test_simple():
    my_structure = Comparision(
        properties=[
            Property(name='users.id'),
            Array(
                values=[
                    Constant(value=1),
                    Constant(value=2),
                    Constant(value=3)
                ]
            )
        ],
        operation=Comparision.Operation.IN
    )

    assert str(my_structure) == "(users.id IN (1, 2, 3))"
