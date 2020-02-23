from backboneql.functions import ConvertTimezone
from backboneql.properties import Property, Constant, Array
from backboneql.structures import Query, Join, Operator, Comparision, Limit, Order


def test_simple():
    my_query = Query(
        entity='users',
        properties=[
            Property(name='users.name'),
            ConvertTimezone(
                property=Property(name='users.created_at'),
                date_from=Constant(value='+00:00'),
                date_to=Constant(value='Europe/Bratislava'),
            )
        ],
        joins=[
            Join(
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
                )
            )
        ],
        conditions=Operator(
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
        ),
        group=[
            Property(name='users.email'),
            Property(name='users.id')
        ],
        order=[
            Order(property=Property(name='users.surname')),
            Order(property=Property(name='users.name'), kind=Order.Direction.DESC)
        ],
        limit=Limit(limit=10, offset=4),
        alias="my_query"
    )

    sql = "(SELECT users.name, CONVERT_TZ(users.created_at, '+00:00', 'Europe/Bratislava') FROM users " \
          "LEFT JOIN transactions ON ((transactions.user_id = users.id) AND (transactions.creator_id != users.id)) " \
          "WHERE ((users.age >= 15) AND (users.city IN ('Martin', 'Bratislava'))) " \
          "GROUP BY users.email, users.id " \
          "ORDER BY users.surname ASC, users.name DESC " \
          "LIMIT 10 OFFSET 4) AS my_query"

    assert str(my_query) == sql
