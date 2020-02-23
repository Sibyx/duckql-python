from backboneql.structures.interval import Interval


def test_simple():
    my_interval = Interval(
        value=-5,
        unit=Interval.Unit.DAY
    )

    assert str(my_interval) == "INTERVAL -5 DAY"
