from backboneql.properties import Property


def test_simple():
    my_property = Property('users.name')

    assert str(my_property) == 'users.name'


def test_alias():
    my_property = Property('users.name', alias='"name')

    assert str(my_property) == 'users.name AS "name"'


def test_escape():
    my_property = Property('users."name', alias='--name')

    assert str(my_property) == 'users.name AS "name"'
