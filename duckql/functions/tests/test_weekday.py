from duckql.functions.weekday import Weekday
from duckql.properties.property import Property


def test_simple():
    my_function = Weekday(
        property=Property(name='users.birthday'),
        alias='special_day'
    )

    assert str(my_function) == 'WEEKDAY(users.birthday) AS special_day'
