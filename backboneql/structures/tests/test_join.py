from backboneql.properties import Property
from backboneql.structures import Join, Operator, Comparision


def test_simple():
    my_join = Join(
        entity='transactions',
        type=Join.Type.LEFT,
        on=Operator(
            operation=Operator.Operation.AND,
            properties=[
                Comparision(
                    properties=[
                        Property(name='transactions.user_id'),
                        Property(name='users.id')
                    ],
                    operation=Comparision.Operation.EQUAL
                ),
                Comparision(
                    properties=[
                        Property(name='transactions.creator_id'),
                        Property(name='users.id')
                    ],
                    operation=Comparision.Operation.NOT_EQUAL
                ),
            ]
        ),
        alias="t"
    )

    sql = "LEFT JOIN transactions ON ((transactions.user_id = users.id) " \
          "AND (transactions.creator_id != users.id)) AS t"
    assert str(my_join) == sql
