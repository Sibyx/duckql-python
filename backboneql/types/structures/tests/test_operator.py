from backboneql.types.properties import Constant, Property, Array
from backboneql.types.structures import Operator, Comparision


def test_simple():
    my_operator = Operator(
        Operator.Operation.AND,
        [
            Comparision([Property('users.age'), Constant(15)], Comparision.Operation.GREATER_EQUAL),
            Comparision(
                [Property('users.city'), Array([Constant('Martin'), Constant('Bratislava')])],
                Comparision.Operation.IN
            )
        ]
    )

    assert str(my_operator) == "((users.age >= 15) AND (users.city IN ('Martin', 'Bratislava')))"
