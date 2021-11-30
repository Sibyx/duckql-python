from duckql.properties.property import Property
from duckql.properties.constant import Constant
from duckql.structures.comparision import Comparision
from duckql.structures.case import Case


def test_simple():
    my_structure = Case(
        conditions=[
            Case.Condition(
                when=Comparision(
                    properties=[
                        Property(name='transactions.direction'),
                        Constant(value='in')
                    ],
                    operation=Comparision.Operation.EQUAL
                ),
                then=Property(name='transactions.direction')
            )
        ],
        alternative=Constant(value=0),
        alias='test_case'
    )

    sql = "(CASE WHEN (transactions.direction = 'in') THEN transactions.direction ELSE 0 END) AS test_case"
    assert str(my_structure) == sql
