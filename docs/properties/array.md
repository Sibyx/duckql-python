# Array

## Basic information

|                 |                                |
|-----------------|--------------------------------|
| **Object type** | `properties.Array`             |
| **Since**       | 0.1.0                          |
| **Dialects**    | `MySQL` `MariaDB` `PostgreSQL` |

## JSON format

```json
{
  "obj": "properties.Array",
  "values": [
    {
      "obj": "properties.Constant",
      "value": "Arthur Dent"
    },
    {
      "obj": "properties.Constant",
      "value": "Deep Thought"
    },
    {
      "obj": "properties.Constant",
      "value": "Tricia Marie McMillan"
    },
    {
      "obj": "properties.Constant",
      "value": "Questular Rontok"
    }
  ]
}
```

## SQL

```sql
('Arthur Dent', 'Deep Thought', 'Tricia Marie McMillan', 'Questular Rontok')
```

## SQL reference

- [PostgreSQL](https://www.postgresql.org/docs/current/arrays.html)
