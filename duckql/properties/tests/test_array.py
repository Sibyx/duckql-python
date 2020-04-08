from duckql.properties import Constant, Array


def test_simple():
    my_array = Array(
        values=[
            Constant(value="Arthur Dent"),
            Constant(value="Deep Thought"),
            Constant(value="Tricia Marie Mc'Millan"),
            Constant(value="Questular Rontok")
        ]
    )

    assert str(my_array) == f"('Arthur Dent', 'Deep Thought', 'Tricia Marie McMillan', 'Questular Rontok')"
