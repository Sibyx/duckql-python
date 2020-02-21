from backboneql.structures.interval import Interval


def test_simple():
    my_interval = Interval(-5, Interval.Unit.DAY)

    assert str(my_interval) == "INTERVAL -5 DAY"
