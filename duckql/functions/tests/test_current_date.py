from duckql.functions.current_date import CurrentDate


def test_simple():
    my_function = CurrentDate(alias="to'day")

    assert str(my_function) == "CURRENT_DATE() AS today"
