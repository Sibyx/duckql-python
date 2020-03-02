# DateSub

## Basic information

|                 |                                |
|-----------------|--------------------------------|
| **Object type** | `functions.DateSub`            |
| **Since**       | 0.1.0                          |
| **Dialects**    | `MySQL` `MariaDB` `PostgreSQL` |

## Object attributes

| Attribute       | Accepts                                                  | Required |
|-----------------|----------------------------------------------------------|----------|
| obj             | `functions.DateSub`                                      | True     |
| property        | `functions.*` `Property` `Constant`                      | True     |
| interval        | `Interval`                                               | True     |
| alias           | String                                                   | False    |

## JSON format

```json
{
  "obj": "functions.DateSub",
  "property": {
    "obj": "properties.Property",
    "name": "users.created_at"
  },
  "interval": {
    "obj": "structures.Interval",
    "value": 5,
    "unit": "day_minute"
  },
  "alias": "sub_dated"
}
```

## SQL

```sql
DATE_SUB(users.created_at, INTERVAL 5 DAY_MINUTE) AS sub_dated
```
