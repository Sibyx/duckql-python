import pytest

from duckql.properties import Property


@pytest.fixture(scope="module")
def valid_instance() -> Property:
    return Property(
        name='users.name',
        alias='"name'
    )


def test_string(valid_instance: Property):
    assert str(valid_instance) == 'users.name AS "name"'


def test_obj(valid_instance: Property):
    assert valid_instance.obj == 'properties.Property'


def test_json_field():
    json_property = Property(
        name='users.additional_data ->> title'
    )
    assert str(json_property) == "users.additional_data ->> 'title'"


def test_json_field_parser():
    json_property = Property.parse_raw(
        '{"obj": "properties.Property", "name": "users.additional_data ->> title", "alias": "title"}'
    )
    assert json_property.name == "users.additional_data ->> title"
    assert str(json_property) == "users.additional_data ->> 'title' AS \"title\""


def test_json_parse(valid_instance: Property):
    assert valid_instance.json() == '{"obj": "properties.Property", "name": "users.name", "alias": "name"}'


def test_json_serialize(valid_instance: Property):
    assert valid_instance == Property.parse_raw(
        '{"obj": "properties.Property", "name": "users.name", "alias": "name"}'
    )


def test_escape():
    my_property = Property(
        name='users."name',
        alias='--name'
    )

    assert str(my_property) == 'users.name AS "name"'
    assert my_property.json() == '{"obj": "properties.Property", "name": "users.name", "alias": "name"}'
