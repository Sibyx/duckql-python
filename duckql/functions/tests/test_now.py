from ..now import Now


def test_property():
    my_now = Now()

    assert str(my_now) == 'NOW()'


def test_alias():
    my_now = Now(alias='"now_name')

    assert str(my_now) == 'NOW() AS now_name'
