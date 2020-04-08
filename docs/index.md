# Welcome to duckQL library

duckQL is simple library which converts JSON-based object to raw SQL in different SQL dialects.

Follow links in right navigation menu to get closer with syntax.

Simple example of usage:

```python
from duckql import Concat, Avg, Property, Constant, Query, Join, Comparision

my_qyery = Query(
        entity='users',
        properties=[
            Concat(
                properties=[
                    Property(name='users.name'),
                    Constant(value=' '),
                    Property(name='users.surname')
                ],
                alias='full_name'
            ),
            Avg(
                property=Property(name='transactions.value'),
                alias='average_transaction_value'
            )
        ],
        joins=[
            Join(
                entity='transactions',
                type=Join.Type.LEFT,
                on=Comparision(
                    properties=[
                        Property(name='transactions.user_id'),
                        Property(name='users.id')
                    ],
                    operation=Comparision.Operation.EQUAL
                )
            )
        ],
        conditions=Comparision(
            properties=[
                Property(name='users.age'),
                Constant(value=15)
            ],
            operation=Comparision.Operation.GREATER_EQUAL
        ),
        group=[
            Property(name='users.id'),
        ],
    )
```

```json
{
  "obj": "structures.Query",
  "entity": "users",
  "properties": [
    {
      "obj": "functions.Concat",
      "properties": [
        {
          "obj": "properties.Property",
          "name": "users.name"
        },
        {
          "obj": "properties.Constant",
          "value": " "
        },
        {
          "obj": "properties.Property",
          "name": "users.surname"
        }
      ],
      "alias": "full_name"
    },
    {
      "obj": "functions.Avg",
      "property": {
        "obj": "properties.Property",
        "name": "transactions.value",
        "alias": null
      },
      "alias": "average_transaction_value"
    }
  ],
  "joins": [
    {
      "obj": "structures.Join",
      "entity": "transactions",
      "type": "left",
      "on": {
        "obj": "structures.Comparision",
        "properties": [
          {
            "obj": "properties.Property",
            "name": "transactions.user_id"
          },
          {
            "obj": "properties.Property",
            "name": "users.id"
          }
        ],
        "operation": "eq"
      }
    }
  ],
  "conditions": {
    "obj": "structures.Comparision",
    "properties": [
      {
        "obj": "properties.Property",
        "name": "users.age",
        "alias": null
      },
      {
        "obj": "properties.Constant",
        "value": "15"
      }
    ],
    "operation": "gte"
  },
  "group": [
    {
      "obj": "properties.Property",
      "name": "users.id"
    }
  ]
}
```

```postgresql
SELECT CONCAT(users.name, ' ', users.surname) AS full_name, AVG(transactions.value) AS average_transaction_value FROM
users LEFT JOIN transactions ON (transactions.user_id = users.id) WHERE (users.age >= 15) GROUP BY users.id
```
