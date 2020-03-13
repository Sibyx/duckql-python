# CastOperator

## Basic information

|                 |                                |
|-----------------|--------------------------------|
| **Object type** | `structures.CastOperator`      |
| **Since**       | 0.1.6                          |
| **Dialects**    | `MySQL` `MariaDB` `PostgreSQL` |

## Object attributes

| Attribute       | Accepts                                                                                | Required |
|-----------------|----------------------------------------------------------------------------------------|----------|
| obj             | `structures.Distinct`                                                                  | True     |
| property        | `functions.*` `Property`                                                               | True     |
| to              | Enum[`boolean` `bool` `char` `varchar` `text` `smallint` `integer` `int` `timestamp` `date`] | True     |
| alias           | String                                                                                 | False    |

## JSON format

```json
{
  "obj": "structures.CastOperator",
  "property": {
    "obj": "properties.Property",
    "name": "users.age"
  },
  "to": "varchar",
  "alias": "age_as_string"
}
```

## SQL

```sql
users.age::varchar AS age_as_string
```

