from backboneql.functions.weekday import Weekday
from backboneql.properties.property import Property


def test_simple():
    my_function = Weekday(Property('users.birthday'), alias='special_day')

    assert str(my_function) == 'WEEKDAY(users.birthday) AS special_day'
