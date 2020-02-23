import pytest

from backboneql.properties import Property


@pytest.fixture(scope="module")
def valid_instance() -> Property:
    return Property(
        name='users.name',
        alias='"name'
    )


def test_string(valid_instance: Property):
    assert str(valid_instance) == 'users.name AS "name"'


def test_obj(valid_instance: Property):
    assert valid_instance.obj == 'property'


def test_json_parse(valid_instance: Property):
    assert valid_instance.json() == '{"obj": "property", "name": "users.name", "alias": "name"}'


def test_json_serialize(valid_instance: Property):
    assert valid_instance == Property.parse_raw('{"obj": "property", "name": "users.name", "alias": "name"}')


def test_escape():
    my_property = Property(
        name='users."name',
        alias='--name'
    )

    assert str(my_property) == 'users.name AS "name"'
    assert my_property.json() == '{"obj": "property", "name": "users.name", "alias": "name"}'
