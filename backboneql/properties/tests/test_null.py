import pytest

from backboneql.properties import Null


@pytest.fixture(scope="module")
def valid_instance() -> Null:
    return Null()


def test_string(valid_instance: Null):
    assert str(valid_instance) == 'NULL'


def test_obj(valid_instance: Null):
    assert valid_instance.obj == 'properties.Null'


def test_json_parse(valid_instance: Null):
    print(valid_instance.json())
    assert valid_instance.json() == '{"obj": "properties.Null"}'
