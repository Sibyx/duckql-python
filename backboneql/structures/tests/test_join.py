from backboneql.properties import Property
from backboneql.structures import Join, Operator, Comparision


def test_simple():
    my_join = Join(
        'transactions',
        Join.Type.LEFT,
        Operator(
            Operator.Operation.AND,
            [
                Comparision(
                    [Property('transactions.user_id'), Property('users.id')],
                    Comparision.Operation.EQUAL
                ),
                Comparision(
                    [Property('transactions.creator_id'), Property('users.id')],
                    Comparision.Operation.NOT_EQUAL
                ),
            ]
        ),
        "t"
    )

    sql = "LEFT JOIN transactions ON ((transactions.user_id = users.id) " \
          "AND (transactions.creator_id != users.id)) AS t"
    assert str(my_join) == sql
