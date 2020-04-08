from duckql.functions.date_sub import DateSub
from duckql.properties.property import Property
from duckql.structures.interval import Interval


def test_simple():
    my_function = DateSub(
        property=Property(name='users.created_at'),
        interval=Interval(value=5, unit=Interval.Unit.DAY_MINUTE),
        alias="sub_dated"
    )

    assert str(my_function) == "DATE_SUB(users.created_at, INTERVAL 5 DAY_MINUTE) AS sub_dated"
