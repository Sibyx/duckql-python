# Unaccent

## Basic information

|                 |                                |
|-----------------|--------------------------------|
| **Object type** | `functions.Unaccent`           |
| **Since**       | 0.5.0                          |
| **Dialects**    | `PostgreSQL`                   |

You need to have enabled `unaccent` extension on your PostgreSQL database (using call `CREATE EXTENSION unaccent`)

## Object attributes

| Attribute       | Accepts                                                       | Required |
|-----------------|---------------------------------------------------------------|----------|
| obj             | `functions.Unaccent`                                          | True     |
| property        | `properties.Property` `functions.*` `Constant` `CastOperator` | True     |
| alias           | String                                                        | False    |

## JSON format

```json
{
  "obj": "functions.Unaccent",
  "property": {
    "obj": "properties.Property",
    "name": "users.name"
  }
}
```

## SQL

```sql
unaccent(users.name)
```

## SQL reference

- [PostgreSQL](https://www.postgresql.org/docs/current/unaccent.html)
