# Lower

## Basic information

|                 |                                |
|-----------------|--------------------------------|
| **Object type** | `functions.Lower`              |
| **Since**       | 0.6.0                          |
| **Dialects**    | `PostgreSQL` `MySQL` `MariaDB` |


## Object attributes

| Attribute       | Accepts                                                       | Required |
|-----------------|---------------------------------------------------------------|----------|
| obj             | `functions.Lower`                                             | True     |
| property        | `properties.Property` `functions.*` `Constant` `CastOperator` | True     |
| alias           | String                                                        | False    |

## JSON format

```json
{
  "obj": "functions.Lower",
  "property": {
    "obj": "properties.Property",
    "name": "users.name"
  }
}
```

## SQL

```sql
lower(users.name)
```

## SQL reference

- [PostgreSQL - String Functions and Operators](https://www.postgresql.org/docs/current/functions-string.html)
- [MariaDB - Lower](https://mariadb.com/kb/en/lower/)
