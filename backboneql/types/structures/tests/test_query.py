from backboneql.types.functions import ConvertTimezone
from backboneql.types.properties import Property, Constant, Array
from backboneql.types.structures import Query, Join, Operator, Comparision, Limit, Order


def test_simple():
    my_query = Query(
        entity='users',
        properties=[
            Property('users.name'),
            ConvertTimezone(
                property=Property('users.created_at'),
                date_from=Constant('+00:00'),
                date_to=Constant('Europe/Bratislava'),
            )
        ],
        joins=[
            Join(
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
                )
            )
        ],
        conditions=Operator(
            Operator.Operation.AND,
            [
                Comparision([Property('users.age'), Constant(15)], Comparision.Operation.GREATER_EQUAL),
                Comparision(
                    [Property('users.city'), Array([Constant('Martin'), Constant('Bratislava')])],
                    Comparision.Operation.IN
                )
            ]
        ),
        group=[
            Property('users.email'),
            Property('users.id')
        ],
        order=[
            Order(Property('users.surname')),
            Order(Property('users.name'), Order.Direction.DESC)
        ],
        limit=Limit(10, 4),
        alias="my_query"
    )

    sql = "(SELECT users.name, CONVERT_TZ(users.created_at, '+00:00', 'Europe/Bratislava') FROM users " \
          "LEFT JOIN transactions ON ((transactions.user_id = users.id) AND (transactions.creator_id != users.id)) " \
          "WHERE ((users.age >= 15) AND (users.city IN ('Martin', 'Bratislava'))) " \
          "GROUP BY users.email, users.id " \
          "ORDER BY users.surname ASC, users.name DESC " \
          "LIMIT 10 OFFSET 4) AS my_query"

    assert str(my_query) == sql
