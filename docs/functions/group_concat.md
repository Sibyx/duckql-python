# GroupConcat

## Basic information

|                 |                                |
|-----------------|--------------------------------|
| **Object type** | `functions.GroupConcat`        |
| **Since**       | 0.1.0                          |
| **Dialects**    | `MySQL` `MariaDB` `PostgreSQL` |

## Object attributes

| Attribute       | Accepts                                                  | Required |
|-----------------|----------------------------------------------------------|----------|
| obj             | `functions.GroupConcat`                                  | True     |
| property        | `functions.*` `Property` `Constant`                      | True     |
| alias           | String                                                   | False    |

## JSON format

```json
{
  "obj": "functions.GroupConcat",
  "property": {
    "obj": "properties.Property",
    "name": "users.id"
  },
  "alias": "my_ids"
}
```

## SQL

```sql
GROUP_CONCAT(users.id) AS my_ids
```