# Weekday

## Basic information

|                 |                                |
|-----------------|--------------------------------|
| **Object type** | `functions.Weekday`            |
| **Since**       | 0.1.0                          |
| **Dialects**    | `MySQL` `MariaDB` `PostgreSQL` |

## Object attributes

| Attribute       | Accepts                                                  | Required |
|-----------------|----------------------------------------------------------|----------|
| obj             | `functions.Weekday`                                      | True     |
| property        | `functions.*` `Property` `Constant` `CastOperator`       | True     |
| alias           | String                                                   | False    |

## JSON format

```json
{
  "obj": "functions.Weekday",
  "property": {
    "obj": "properties.Property",
    "name": "users.birthday"
  },
  "alias": "special_day"
}
```

## SQL

```sql
WEEKDAY(users.birthday) AS special_day
```
