from duckql.properties import Property
from duckql.structures import Join, Operator, Comparision


def test_simple():
    my_join = Join(
        entity='transactions',
        type=Join.Type.LEFT,
        on=Operator(
            operation=Operator.Operation.AND,
            properties=[
                Comparision(
                    properties=[
                        Property(name='t.user_id'),
                        Property(name='users.id')
                    ],
                    operation=Comparision.Operation.EQUAL
                ),
                Comparision(
                    properties=[
                        Property(name='t.creator_id'),
                        Property(name='users.id')
                    ],
                    operation=Comparision.Operation.NOT_EQUAL
                ),
            ]
        ),
        alias="t"
    )

    sql = "LEFT JOIN transactions t ON ((t.user_id = users.id) AND (t.creator_id != users.id))"
    assert str(my_join) == sql


def test_natural():
    my_join = Join(
        entity='transactions',
        type=Join.Type.NATURAL
    )

    sql = "NATURAL JOIN transactions"
    assert str(my_join) == sql
