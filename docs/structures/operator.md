# Operator

## Basic information

|                 |                                |
|-----------------|--------------------------------|
| **Object type** | `structures.Operator`          |
| **Since**       | 0.1.0                          |
| **Dialects**    | `MySQL` `MariaDB` `PostgreSQL` |

## Object attributes

| Property        | Accepts                                                                                | Required |
|-----------------|----------------------------------------------------------------------------------------|----------|
| obj             | `structures.Operator`                                                                  | True     |
| operation       | Enum[`and` `or` `division` `multiplication` `subtraction` `addition`]                  | True     |
| properties      | List[`functions.*` `Constant` `Property` `Boolean` `structures.Comparision`]           | True     |
| alias           | String                                                                                 | False    |

## JSON format

```json
{
  "obj": "structures.Operator",
  "operation": "and",
  "properties": [
    {
      "obj": "structures.Comparision",
      "properties": [
        {
          "obj": "properties.Property",
          "name": "users.age"
        },
        {
          "obj": "properties.Constant",
          "value": "15"
        }
      ],
      "operation": "gte"
    },
    {
      "obj": "structures.Comparision",
      "properties": [
        {
          "obj": "properties.Property",
          "name": "users.city"
        },
        {
          "obj": "properties.Array",
          "values": [
            {
              "obj": "properties.Constant",
              "value": "Martin"
            },
            {
              "obj": "properties.Constant",
              "value": "Bratislava"
            }
          ]
        }
      ],
      "operation": "in"
    }
  ]
}
```

## SQL

```sql
((users.age >= 15) AND (users.city IN ('Martin', 'Bratislava')))
```

