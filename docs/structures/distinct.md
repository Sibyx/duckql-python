# Distinct

## Basic information

|                 |                                |
|-----------------|--------------------------------|
| **Object type** | `structures.Distinct`          |
| **Since**       | 0.1.0                          |
| **Dialects**    | `MySQL` `MariaDB` `PostgreSQL` |

## Object attributes

| Attribute       | Accepts                                                                                | Required |
|-----------------|----------------------------------------------------------------------------------------|----------|
| obj             | `structures.Distinct`                                                                  | True     |
| property        | `functions.*` `Property`                                                               | True     |

## JSON format

```json
{
  "obj": "structures.Distinct",
  "property": {
    "obj": "properties.Property",
    "name": "users.name"
  }
}
```

## SQL

```sql
DISTINCT users.name
```

