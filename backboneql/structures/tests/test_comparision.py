from backboneql.properties import Property, Array, Constant
from backboneql.structures import Comparision


def test_simple():
    my_structure = Comparision(
        [Property('users.id'), Array([Constant(1), Constant(2), Constant(3)])],
        operation=Comparision.Operation.IN
    )

    assert str(my_structure) == "(users.id IN (1, 2, 3))"
