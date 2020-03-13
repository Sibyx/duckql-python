# Count

## Basic information

|                 |                                |
|-----------------|--------------------------------|
| **Object type** | `functions.Count`              |
| **Since**       | 0.1.0                          |
| **Dialects**    | `MySQL` `MariaDB` `PostgreSQL` |

## Object attributes

| Attribute       | Accepts                                                  | Required |
|-----------------|----------------------------------------------------------|----------|
| obj             | `functions.Count`                                        | True     |
| property        | `properties.Property` `CastOperator`                     | True     |
| alias           | String                                                   | False    |

## JSON format

```json
{
  "obj": "functions.Count",
  "property": {
    "obj": "properties.Property",
    "name": "users.id"
  },
  "alias": "user_count"
}
```

## SQL

```sql
COUNT(users.id) AS user_count
```
