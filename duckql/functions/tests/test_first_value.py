from duckql import Property, FirstValue, Order


def test_property():
    stm = FirstValue(
        property=Property(name='users.name'),
        partition=[
            Property(name='users.age'),
            Property(name='users.city')
        ],
        order=[
            Order(
                property=Property(name='users.created_at')
            )
        ]
    )

    assert str(stm) == 'FIRST_VALUE(users.name) OVER (PARTITION BY users.age, users.city ORDER BY users.created_at ' \
                       'ASC)'
