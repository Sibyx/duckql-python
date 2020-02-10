from backboneql.types.functions import DateSub
from backboneql.types.properties import Property
from backboneql.types.structures import Interval


def test_simple():
    my_function = DateSub(
        Property('users.created_at'),
        Interval(5, Interval.Unit.DAY_MINUTE),
        alias="sub_dated"
    )

    assert str(my_function) == "DATE_SUB(users.created_at, INTERVAL 5 DAY_MINUTE) AS sub_dated"
