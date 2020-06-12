from duckql.properties.constant import Constant
from duckql.functions.to_date import ToDate


def test_property():
    my_function = ToDate(
        property=Constant(value='05 Dec 2000'),
        format='DD Mon YYYY'
    )

    assert str(my_function) == "to_date('05 Dec 2000', 'DD Mon YYYY')"
