from backboneql.functions.convert_timezone import ConvertTimezone
from backboneql.properties.constant import Constant
from backboneql.properties.property import Property


def test_simple():
    my_function = ConvertTimezone(
        property=Property(name='users.name'),
        date_from=Constant(value='+00:00'),
        date_to=Constant(value='Europe/Bratislava'),
        alias="'my_time"
    )

    assert str(my_function) == "CONVERT_TZ(users.name, '+00:00', 'Europe/Bratislava') AS my_time"
