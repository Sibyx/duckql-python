from duckql.properties import Constant, Property, Array
from duckql.structures import Operator, Comparision


def test_simple():
    my_operator = Operator(
        operation=Operator.Operation.AND,
        properties=[
            Comparision(
                properties=[
                    Property(name='users.age'),
                    Constant(value=15)
                ],
                operation=Comparision.Operation.GREATER_EQUAL
            ),
            Comparision(
                properties=[
                    Property(name='users.city'),
                    Array(
                        values=[
                            Constant(value='Martin'),
                            Constant(value='Bratislava')
                        ]
                    )
                ],
                operation=Comparision.Operation.IN
            )
        ]
    )

    assert str(my_operator) == "((users.age >= 15) AND (users.city IN ('Martin', 'Bratislava')))"
