# Between

## Basic information

|                 |                                |
|-----------------|--------------------------------|
| **Object type** | `structures.Between`           |
| **Since**       | 0.1.0                          |
| **Dialects**    | `MySQL` `MariaDB` `PostgreSQL` |

## Object attributes

| Attribute       | Accepts                                                  | Required |
|-----------------|----------------------------------------------------------|----------|
| obj             | `structures.Between`                                     | True     |
| property        | `functions.*` `properties.Property` `Constant`           | True     |
| values          | List[`functions.*` `properties.Property` `Constant`]{2}  | True     |

## JSON format

```json
{
  "obj": "structures.Between",
  "property": {
    "obj": "properties.Property",
    "name": "transactions.happened_at"
  },
  "values": [
    {
      "obj": "properties.Constant",
      "value": "2020-01-01"
    },
    {
      "obj": "properties.Constant",
      "value": "2020-02-01"
    }
  ]
}
```

## SQL

```sql
transactions.happened_at BETWEEN '2020-01-01' AND '2020-02-01'
```

