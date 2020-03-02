# Limit

## Basic information

|                 |                                |
|-----------------|--------------------------------|
| **Object type** | `structures.Limit`             |
| **Since**       | 0.1.0                          |
| **Dialects**    | `MySQL` `MariaDB` `PostgreSQL` |

## Object attributes

| Attribute       | Accepts                                                                                | Required |
|-----------------|----------------------------------------------------------------------------------------|----------|
| obj             | `structures.Limit`                                                                     | True     |
| limit           | Integer                                                                                | True     |
| offset          | Integer                                                                                | False    |

## JSON format

```json
{
  "obj": "structures.Limit",
  "limit": 42,
  "offset": 5
}
```

## SQL

```sql
LIMIT 42 OFFSET 5
```

