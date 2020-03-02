# Min

## Basic information

|                 |                                |
|-----------------|--------------------------------|
| **Object type** | `functions.Min`                |
| **Since**       | 0.1.0                          |
| **Dialects**    | `MySQL` `MariaDB` `PostgreSQL` |

## Object attributes

| Attribute       | Accepts                                                  | Required |
|-----------------|----------------------------------------------------------|----------|
| obj             | `functions.Min`                                          | True     |
| property        | `functions.*` `Property`                                 | True     |
| alias           | String                                                   | False    |

## JSON format

```json
{
  "obj": "functions.Min",
  "property": {
    "obj": "properties.Property",
    "name": "users.age"
  },
  "alias": "minimum_age"
}
```

## SQL

```sql
MIN(users.age) AS minimum_age
```