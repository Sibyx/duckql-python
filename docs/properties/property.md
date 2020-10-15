# Property

## Basic information

|                 |                                |
|-----------------|--------------------------------|
| **Object type** | `properties.Property`          |
| **Since**       | 0.1.0                          |
| **Dialects**    | `MySQL` `MariaDB` `PostgreSQL` |

## JSON format

```json
{
  "obj": "properties.Property",
  "name": "users.name",
  "alias": "name"
}
```

## SQL

```sql
users.name AS "name"
```

## JSON Properties

As of version 0.8.0 you can use `properties.Property` object for `PostgreSQL` JSON lookups.

**JSON**

```json
{
  "obj": "properties.Property",
  "name": "users.additional_data -> metadata ->> age",
  "alias": "age"
}
```

**Python**

```python
from duckql import  Property

json_property = Property(
    name='users.additional_data -> custom_fields ->> age',
    alias='age'
)
```

**SQL**

```sql
users.additional_data -> 'metadata' ->> 'age' AS "age"
```
