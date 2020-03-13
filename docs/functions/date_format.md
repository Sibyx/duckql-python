# DateFormat

## Basic information

|                 |                                |
|-----------------|--------------------------------|
| **Object type** | `functions.DateFormat`         |
| **Since**       | 0.1.0                          |
| **Dialects**    | `MySQL` `MariaDB` `PostgreSQL` |

## Object attributes

| Attribute       | Accepts                                                  | Required |
|-----------------|----------------------------------------------------------|----------|
| obj             | `functions.DateFormat`                                   | True     |
| property        | `functions.*` `Property` `Constant` `CastOperator`       | True     |
| format          | String                                                   | True     |
| alias           | String                                                   | False    |

## JSON format

```json
{
  "obj": "functions.DateFormat",
  "property": {
    "obj": "properties.Property",
    "name": "users.created_at",
    "alias": null
  },
  "format": "%Y-%m-%d %H:%i:%s",
  "alias": "formatted_datetime"
}
```

## SQL

```sql
DATE_FORMAT(users.created_at, '%Y-%m-%d %H:%i:%s') AS formatted_datetime
```
