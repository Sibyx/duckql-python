# Max

## Basic information

|                 |                                |
|-----------------|--------------------------------|
| **Object type** | `functions.Max`                |
| **Since**       | 0.1.0                          |
| **Dialects**    | `MySQL` `MariaDB` `PostgreSQL` |

## Object attributes

| Attribute       | Accepts                                                  | Required |
|-----------------|----------------------------------------------------------|----------|
| obj             | `functions.Max`                                          | True     |
| property        | `functions.*` `Property` `CastOperator`                  | True     |
| alias           | String                                                   | False    |

## JSON format

```json
{
  "obj": "functions.Max",
  "property": {
    "obj": "properties.Property",
    "name": "users.age"
  },
  "alias": "maximum_age"
}
```

## SQL

```sql
MAX(users.age) AS maximum_age
```
