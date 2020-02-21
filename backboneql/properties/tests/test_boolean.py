from backboneql.properties import Boolean


def test_true():
    my_type = Boolean(value=True)

    assert my_type.value is True
    assert str(my_type) == 'TRUE'


def test_false():
    my_type = Boolean(value=False)

    assert my_type.value is False
    assert str(my_type) == 'FALSE'
