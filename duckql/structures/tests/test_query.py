from duckql import Concat, Avg, Interval, Sum
from duckql.functions import ConvertTimezone, Count
from duckql.properties import Property, Constant, Array
from duckql.structures import Query, Join, Operator, Comparision, Limit, Order
from duckql.functions import Now


def test_simple():
    my_query = Query(
        entity='users',
        properties=[
            Property(name='users.name', alias='users_name'),
            ConvertTimezone(
                property=Property(name='users.created_at'),
                date_from=Constant(value='+00:00'),
                date_to=Constant(value='Europe/Bratislava'),
                alias='valid_timezone'
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
        having=Comparision(
            operation=Comparision.Operation.GREATER,
            properties=[
                Sum(property=Property(name='transactions.value')),
                Constant(value=420)
            ]
        ),
        order=[
            Order(property=Property(name='users.surname')),
            Order(property=Property(name='users.name'), kind=Order.Direction.DESC)
        ],
        limit=Limit(limit=10, offset=4),
        alias="my_query"
    )

    sql = "(SELECT users.name AS \"users_name\", CONVERT_TZ(users.created_at, '+00:00', 'Europe/Bratislava') " \
          "AS valid_timezone FROM users " \
          "LEFT JOIN transactions ON ((transactions.user_id = users.id) AND (transactions.creator_id != users.id)) " \
          "WHERE ((users.age >= 15) AND (users.city IN ('Martin', 'Bratislava'))) " \
          "GROUP BY users.email, users.id " \
          "HAVING (SUM(transactions.value) > 420) " \
          "ORDER BY users.surname ASC, users.name DESC " \
          "LIMIT 10 OFFSET 4) AS my_query"

    assert str(my_query) == sql

    json_string = my_query.json()
    clone = Query.parse_raw(json_string)

    assert clone == my_query
    assert str(clone) == sql


def test_subquery():
    my_subquery = Query(
        entity='users',
        properties=[
            Property(name='users.name'),
        ],
        group=[
            Property(name='users.birthday'),
        ],
        alias='s'
    )

    my_query = Query(
        entity=my_subquery,
        properties=[
            Count(
                property=Constant(value='*')
            ),
        ],
    )

    sql = "SELECT COUNT('*') FROM (SELECT users.name FROM users GROUP BY users.birthday) AS s"

    assert str(my_query) == sql

    json_string = my_query.json()
    clone = Query.parse_raw(json_string)

    assert clone == my_query
    assert str(clone) == sql


def test_short_example():
    my_query = Query(
        entity='users',
        properties=[
            Property(name='users.name'),
            Property(name='users.surname')
        ],
        conditions=Comparision(
            properties=[
                Property(name='users.age'),
                Constant(value=15)
            ],
            operation=Comparision.Operation.GREATER_EQUAL
        )
    )

    sql = 'SELECT users.name, users.surname FROM users WHERE (users.age >= 15)'

    assert str(my_query) == sql

    json_string = my_query.json()
    clone = Query.parse_raw(json_string)

    assert clone == my_query
    assert str(clone) == sql


def test_example():
    my_query = Query(
        entity='users',
        properties=[
            Concat(
                properties=[
                    Property(name='users.name'),
                    Constant(value=' '),
                    Property(name='users.surname')
                ],
                alias='full_name'
            ),
            Avg(
                property=Property(name='transactions.value'),
                alias='average_transaction_value'
            )
        ],
        joins=[
            Join(
                entity='transactions',
                type=Join.Type.LEFT,
                on=Comparision(
                    properties=[
                        Property(name='transactions.user_id'),
                        Property(name='users.id')
                    ],
                    operation=Comparision.Operation.EQUAL
                )
            )
        ],
        conditions=Comparision(
            properties=[
                Property(name='users.age'),
                Constant(value=15)
            ],
            operation=Comparision.Operation.GREATER_EQUAL
        ),
        group=[
            Property(name='users.id'),
        ],
    )

    sql = "SELECT CONCAT(users.name, ' ', users.surname) AS full_name, AVG(transactions.value) AS " \
          'average_transaction_value FROM users LEFT JOIN transactions ON (transactions.user_id = users.id) WHERE ' \
          '(users.age >= 15) GROUP BY users.id'

    assert str(my_query) == sql

    json_string = my_query.json()
    clone = Query.parse_raw(json_string)

    assert clone == my_query
    assert str(clone) == sql


def test_having():
    my_query = Query(
        entity='organisations',
        properties=[
            Property(name='organisations.id'),
            Count(property=Property(name='campaigns.id'))
        ],
        joins=[
            Join(
                type=Join.Type.LEFT,
                entity='campaigns',
                on=Comparision(
                    operation=Comparision.Operation.EQUAL,
                    properties=[
                        Property(name='organisations.id'),
                        Property(name='campaigns.organisation_id')
                    ]
                )
            )
        ],
        conditions=Comparision(
            operation=Comparision.Operation.LOWER,
            properties=[
                Property(name='organisations.created_at'),
                Operator(
                    operation=Operator.Operation.SUBTRACTION,
                    properties=[
                        Now(),
                        Interval(
                            value=1,
                            unit=Interval.Unit.MONTH
                        )
                    ]
                )
            ]
        ),
        group=[
            Property(name='organisations.id')
        ],
        having=Comparision(
            operation=Comparision.Operation.EQUAL,
            properties=[
                Count(property=Property(name='campaigns.id')),
                Constant(value=0)
            ]
        )
    )

    sql = "SELECT organisations.id, COUNT(campaigns.id) FROM organisations LEFT JOIN campaigns ON " \
          "(organisations.id = campaigns.organisation_id) WHERE (organisations.created_at < " \
          "(NOW() - INTERVAL '1 MONTH')) GROUP BY organisations.id HAVING (COUNT(campaigns.id) = 0)"

    assert str(my_query) == sql

    json_string = my_query.json()
    clone = Query.parse_raw(json_string)

    assert clone == my_query
    assert str(clone) == sql


def test_group_by_json():
    my_query = Query(
        entity='signatories',
        properties=[
            Property(name='signatories.additional_data->organisation->>name'),
            Count(property=Property(name='signatories.additional_data->organisation->>name'))
        ],
        group=[
            Property(name='signatories.additional_data->organisation->>name')
        ]
    )

    sql = "SELECT signatories.additional_data -> 'organisation' ->> 'name', COUNT(signatories.additional_data -> " \
          "'organisation' ->> 'name') FROM signatories GROUP BY signatories.additional_data -> 'organisation' ->> " \
          "'name';"

    assert str(my_query == sql)
