# ToChar

## Basic information

|                 |                                |
|-----------------|--------------------------------|
| **Object type** | `functions.ToChar`             |
| **Since**       | 0.4.0                          |
| **Dialects**    | `PostgreSQL`                   |

## Object attributes

| Attribute       | Accepts                                                       | Required |
|-----------------|---------------------------------------------------------------|----------|
| obj             | `functions.ToChar`                                            | True     |
| property        | `functions.*` `Property` `Constant` `CastOperator` `Interval` | True     |
| format          | String                                                        | True     |
| alias           | String                                                        | False    |

## JSON format

```json
{
  "obj": "functions.ToChar",
  "property": {
    "obj": "properties.Property",
    "name": "users.created_at"
  },
  "format": "HH12:MI:SS",
  "alias": "formatted_datetime"
}
```

## SQL

```sql
to_char(users.created_at, 'HH12:MI:SS') AS formatted_datetime
```
