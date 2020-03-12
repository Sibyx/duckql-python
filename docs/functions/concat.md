# Concat

## Basic information

|                 |                                |
|-----------------|--------------------------------|
| **Object type** | `functions.Concat`             |
| **Since**       | 0.1.0                          |
| **Dialects**    | `MySQL` `MariaDB` `PostgreSQL` |

## Object attributes

| Attribute       | Accepts                                                  | Required |
|-----------------|----------------------------------------------------------|----------|
| obj             | `functions.Concat`                                       | True     |
| properties      | List[`functions.*` `Property` `Constant`]                | True     |
| alias           | String                                                   | False    |

## JSON format

```json
{
  "obj": "functions.Concat",
  "properties": [
    {
      "obj": "properties.Property",
      "name": "users.name"
    },
    {
      "obj": "properties.Constant",
      "value": " "
    },
    {
      "obj": "properties.Property",
      "name": "users.surname"
    }
  ],
  "alias": "full_name"
}
```

## SQL

```sql
CONCAT(users.name, ' ', users.surname) AS full_name
```
