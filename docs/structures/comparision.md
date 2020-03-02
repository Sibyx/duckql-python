# Comparision

## Basic information

|                 |                                |
|-----------------|--------------------------------|
| **Object type** | `structures.Comparision`       |
| **Since**       | 0.1.0                          |
| **Dialects**    | `MySQL` `MariaDB` `PostgreSQL` |

## Object attributes

| Attribute       | Accepts                                                                                | Required |
|-----------------|----------------------------------------------------------------------------------------|----------|
| obj             | `structures.Comparision`                                                               | True     |
| properties      | List[`functions.*` `Constant` `Property` `Array` `Boolean` `Null`]{2}                  | True     |
| operation       | Enum[`eq` `neq` `lt` `lte` `gt` `gte` `like` `in` `nlike` `nin` `is` `nis` `contains`] | True     |

## JSON format

```json
{
  "obj": "structures.Comparision",
  "properties": [
    {
      "obj": "properties.Property",
      "name": "users.id"
    },
    {
      "obj": "properties.Array",
      "values": [
        {
          "obj": "properties.Constant",
          "value": "1"
        },
        {
          "obj": "properties.Constant",
          "value": "2"
        },
        {
          "obj": "properties.Constant",
          "value": "3"
        }
      ]
    }
  ],
  "operation": "in"
}
```

## SQL

```sql
(users.id IN (1, 2, 3))
```

