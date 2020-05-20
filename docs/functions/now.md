# Now

## Basic information

|                 |                                |
|-----------------|--------------------------------|
| **Object type** | `functions.Now`                |
| **Since**       | 0.3.0                          |
| **Dialects**    | `MySQL` `MariaDB` `PostgreSQL` |

## Object attributes

| Attribute       | Accepts                                                  | Required |
|-----------------|----------------------------------------------------------|----------|
| obj             | `functions.Now`                                          | True     |
| alias           | String                                                   | False    |

## JSON format

```json
{
  "obj": "functions.Now",
  "alias": "today"
}
```

## SQL

```sql
NOW() AS today
```
