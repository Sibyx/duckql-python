from duckql import Property, Order, ArrayAgg


def test_simple():
    stm = ArrayAgg(
        property=Property(name='warehouse_logs.state'),
    )

    assert str(stm) == 'ARRAY_AGG(warehouse_logs.state)'


def test_order_by():
    stm = ArrayAgg(
        property=Property(name='warehouse_logs.state'),
        order=[
            Order(
                property=Property(name='warehouse_logs.created_at')
            )
        ]
    )

    assert str(stm) == 'ARRAY_AGG(warehouse_logs.state ORDER BY warehouse_logs.created_at ASC)'


def test_position():
    stm = ArrayAgg(
        property=Property(name='warehouse_logs.state'),
        position=1,
        order=[
            Order(
                property=Property(name='warehouse_logs.created_at')
            )
        ]
    )

    assert str(stm) == '(ARRAY_AGG(warehouse_logs.state ORDER BY warehouse_logs.created_at ASC))[1]'


def test_alias():
    stm = ArrayAgg(
        property=Property(name='warehouse_logs.state'),
        position=1,
        order=[
            Order(
                property=Property(name='warehouse_logs.created_at')
            )
        ],
        alias="first_volume"
    )

    assert str(stm) == '(ARRAY_AGG(warehouse_logs.state ORDER BY warehouse_logs.created_at ASC))[1] AS first_volume'
