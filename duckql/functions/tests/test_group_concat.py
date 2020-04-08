from duckql.functions.group_concat import GroupConcat
from duckql.properties.property import Property


def test_simple():
    my_function = GroupConcat(
        property=Property(name='users.id'),
        alias='my_ids'
    )

    assert str(my_function) == 'GROUP_CONCAT(users.id) AS my_ids'
