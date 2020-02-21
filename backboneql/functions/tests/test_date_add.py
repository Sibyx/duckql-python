from backboneql.functions.date_add import DateAdd
from backboneql.properties.property import Property
from backboneql.structures.interval import Interval


def test_simple():
    my_function = DateAdd(
        Property('users.created_at'),
        Interval(4, Interval.Unit.YEAR_MONTH),
        alias="add_dated"
    )

    assert str(my_function) == "DATE_ADD(users.created_at, INTERVAL 4 YEAR_MONTH) AS add_dated"
