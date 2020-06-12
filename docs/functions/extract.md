# Extract

## Basic information

|                 |                                |
|-----------------|--------------------------------|
| **Object type** | `functions.Extract`            |
| **Since**       | 0.1.0                          |
| **Dialects**    | `MySQL` `MariaDB` `PostgreSQL` |

## Object attributes

| Attribute       | Accepts                                                  | Required |
|-----------------|----------------------------------------------------------|----------|
| obj             | `functions.Extract`                                      | True     |
| property        | List[`functions.*` `Property` `Constant` `Interval` `CastOperator`] | True     |
| unit            | Enum[`century` `day` `decade` `dow` `doy` `epoch` `hour` `isodow` `isoyear` `microseconds` `millennium` `milliseconds` `minute` `month` `quarter` `second` `timezone` `timezone_hour` `timezone_minute` `week` `year`] | True     |
| alias           | String                                                   | False    |

## JSON format

```json
{
  "obj": "functions.Extract",
  "property": {
    "obj": "properties.Property",
    "name": "users.created_at"
  },
  "unit": "century"
}
```

## SQL

```sql
EXTRACT(CENTURY FROM users.created_at)
```
