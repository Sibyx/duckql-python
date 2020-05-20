from duckql.functions.date_add import DateAdd
from duckql.properties.property import Property
from duckql.structures.interval import Interval


def test_simple():
    my_function = DateAdd(
        property=Property(name='users.created_at'),
        interval=Interval(value=4, unit=Interval.Unit.YEAR_MONTH),
        alias="add_dated"
    )

    assert str(my_function) == "DATE_ADD(users.created_at, INTERVAL '4 YEAR_MONTH') AS add_dated"
