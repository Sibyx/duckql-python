# Avg

## Basic information

|                 |                                |
|-----------------|--------------------------------|
| **Object type** | `functions.Avg`                |
| **Since**       | 0.1.0                          |
| **Dialects**    | `MySQL` `MariaDB` `PostgreSQL` |

## Object attributes

| Attribute       | Accepts                                                  | Required |
|-----------------|----------------------------------------------------------|----------|
| obj             | `functions.Avg`                                          | True     |
| property        | `properties.Property` `functions.*` `Constant` `CastOperator` | True     |
| alias           | String                                                   | False    |

## JSON format

```json
{
  "obj": "functions.Avg",
  "property": {
    "obj": "properties.Property",
    "name": "users.name"
  },
  "alias": "avg_name"
}
```

## SQL

```sql
AVG(users.name) AS avg_name
```

## SQL reference

- [PostgreSQL](https://www.postgresql.org/docs/current/functions-aggregate.html)
- [MySQL](https://dev.mysql.com/doc/refman/8.0/en/group-by-functions.html#function_avg)
- [MariaDB](https://mariadb.com/kb/en/avg/)
