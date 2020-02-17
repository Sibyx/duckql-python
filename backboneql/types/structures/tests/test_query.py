from backboneql.types.functions import ConvertTimezone
from backboneql.types.properties import Property, Constant
from backboneql.types.structures import Query


def test_simple():
    my_query = Query(
        entity='users',
        properties=[
            Property('users.name'),
            ConvertTimezone(
                property=Property('users.created_at'),
                date_from=Constant('+00:00'),
                date_to=Constant('Europe/Bratislava'),
            )
        ],
    )

    assert str(my_query) == "SELECT users.name, CONVERT_TZ(users.created_at, '+00:00', 'Europe/Bratislava') FROM users"
