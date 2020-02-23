from backboneql.properties import Constant


def test_simple():
    my_type = Constant(value="The answer!")

    assert str(my_type) == "'The answer!'"


def test_escape():
    my_type = Constant(value='" or ""="')

    assert str(my_type) == "' or ='"


def test_numeric():
    # TODO: decimal etc.
    assert str(Constant(value=42)) == "42"
