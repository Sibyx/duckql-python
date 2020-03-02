# CurrentDate

## Basic information

|                 |                                |
|-----------------|--------------------------------|
| **Object type** | `functions.CurrentDate`        |
| **Since**       | 0.1.0                          |
| **Dialects**    | `MySQL` `MariaDB` `PostgreSQL` |

## Object attributes

| Attribute       | Accepts                                                  | Required |
|-----------------|----------------------------------------------------------|----------|
| obj             | `functions.CurrentDate`                                  | True     |
| alias           | String                                                   | False    |

## JSON format

```json
{
  "obj": "functions.CurrentDate",
  "alias": "today"
}
```

## SQL

```sql
CURRENT_DATE() AS today
```