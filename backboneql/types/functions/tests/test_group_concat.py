from backboneql.types.functions.group_concat import GroupConcat
from backboneql.types.properties import Property


def test_simple():
    my_function = GroupConcat(Property('users.id'), alias='my_ids')

    assert str(my_function) == 'GROUP_CONCAT(users.id) AS my_ids'
