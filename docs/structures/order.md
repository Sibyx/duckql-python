# Order

## Basic information

|                 |                                |
|-----------------|--------------------------------|
| **Object type** | `structures.Order`             |
| **Since**       | 0.1.0                          |
| **Dialects**    | `MySQL` `MariaDB` `PostgreSQL` |

## Object attributes

| Attribute       | Accepts                                                                                | Required |
|-----------------|----------------------------------------------------------------------------------------|----------|
| obj             | `structures.Order`                                                                     | True     |
| property        | `functions.*` `properties.Property`                                                    | True     |
| kind            | Enum[`ASC` `DESC`]                                                                     | False    |


## JSON format

```json
{
  "obj": "structures.Order",
  "property": {
    "obj": "properties.Property",
    "name": "users.name"
  }
}
```

## SQL

```sql
users.name ASC
```

