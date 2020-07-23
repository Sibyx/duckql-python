# Upper

## Basic information

|                 |                                |
|-----------------|--------------------------------|
| **Object type** | `functions.Upper`              |
| **Since**       | 0.6.0                          |
| **Dialects**    | `PostgreSQL` `MySQL` `MariaDB` |


## Object attributes

| Attribute       | Accepts                                                       | Required |
|-----------------|---------------------------------------------------------------|----------|
| obj             | `functions.Upper`                                             | True     |
| property        | `properties.Property` `functions.*` `Constant` `CastOperator` | True     |
| alias           | String                                                        | False    |

## JSON format

```json
{
  "obj": "functions.Upper",
  "property": {
    "obj": "properties.Property",
    "name": "users.name"
  }
}
```

## SQL

```sql
upper(users.name)
```

## SQL reference

- [PostgreSQL - String Functions and Operators](https://www.postgresql.org/docs/current/functions-string.html)
- [MariaDB - Upper](https://mariadb.com/kb/en/upper/)
