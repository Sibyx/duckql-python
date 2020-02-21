from backboneql.properties import Constant, Array


def test_simple():
    my_array = Array([
        Constant("Arthur Dent"),
        Constant("Deep Thought"),
        Constant("Tricia Marie Mc'Millan"),
        Constant("Questular Rontok")
    ])

    assert str(my_array) == f"('Arthur Dent', 'Deep Thought', 'Tricia Marie McMillan', 'Questular Rontok')"
