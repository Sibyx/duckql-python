from backboneql.functions.date_format import DateFormat
from backboneql.properties.property import Property


def test_simple():
    my_function = DateFormat(
        property=Property(name='users.created_at'),
        format='%Y-%m-%d %H:%i:%s',
        alias="formatted'_datetime"
    )

    assert str(my_function) == "DATE_FORMAT(users.created_at, '%Y-%m-%d %H:%i:%s') AS formatted_datetime"
