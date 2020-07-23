# InitCap

## Basic information

|                 |                                |
|-----------------|--------------------------------|
| **Object type** | `functions.InitCap`            |
| **Since**       | 0.6.0                          |
| **Dialects**    | `PostgreSQL`                   |


## Object attributes

| Attribute       | Accepts                                                       | Required |
|-----------------|---------------------------------------------------------------|----------|
| obj             | `functions.InitCap`                                           | True     |
| property        | `properties.Property` `functions.*` `Constant` `CastOperator` | True     |
| alias           | String                                                        | False    |

## JSON format

```json
{
  "obj": "functions.InitCap",
  "property": {
    "obj": "properties.Property",
    "name": "users.name"
  }
}
```

## SQL

```sql
initcap(users.name)
```

## SQL reference

- [PostgreSQL - String Functions and Operators](https://www.postgresql.org/docs/current/functions-string.html)
