from duckql.structures.interval import Interval
from duckql.properties.property import Property
from duckql.properties.constant import Constant
from duckql.functions.to_char import ToChar
from duckql.structures.cast_operator import CastOperator


def test_property():
    my_function = ToChar(
        property=Property(name='users.created_at'),
        format='HH12:MI:SS',
        alias="formatted'_datetime"
    )

    assert str(my_function) == "to_char(users.created_at, 'HH12:MI:SS') AS formatted_datetime"


def test_interval():
    my_function = ToChar(
        property=Interval(
            unit=Interval.Unit.MONTH,
            value=1
        ),
        format='HH12:MI:SS',
        alias="formatted_interval"
    )

    assert str(my_function) == "to_char(INTERVAL '1 MONTH', 'HH12:MI:SS') AS formatted_interval"


def test_constant():
    my_function = ToChar(
        property=Constant(value=125),
        format='999',
        alias="formatted_constant"
    )

    assert str(my_function) == "to_char(125, '999') AS formatted_constant"


def test_cast():
    my_function = ToChar(
        property=CastOperator(
            to=CastOperator.DataType.REAL,
            property=Constant(value='127.3')
        ),
        format='999D9',
        alias="formatted_cast"
    )

    assert str(my_function) == "to_char('127.3'::real, '999D9') AS formatted_cast"
