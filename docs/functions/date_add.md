# DateAdd

## Basic information

|                 |                                |
|-----------------|--------------------------------|
| **Object type** | `functions.DateAdd`            |
| **Since**       | 0.1.0                          |
| **Dialects**    | `MySQL` `MariaDB` `PostgreSQL` |

## Object attributes

| Attribute       | Accepts                                                  | Required |
|-----------------|----------------------------------------------------------|----------|
| obj             | `functions.DateAdd`                                      | True     |
| property        | `functions.*` `Property` `Constant` `CastOperator`       | True     |
| interval        | `Interval`                                               | True     |
| alias           | String                                                   | False    |

## JSON format

```json
{
  "obj": "functions.DateAdd",
  "property": {
    "obj": "properties.Property",
    "name": "users.created_at",
    "alias": null
  },
  "interval": {
    "obj": "structures.Interval",
    "value": 4,
    "unit": "year_month"
  },
  "alias": "add_dated"
}
```

## SQL

```sql
DATE_ADD(users.created_at, INTERVAL 4 YEAR_MONTH) AS add_dated
```
