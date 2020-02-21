from backboneql.properties import Null


def test_simple():
    my_type = Null()

    assert str(my_type) == 'NULL'
