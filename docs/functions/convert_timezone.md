# ConvertTimezone

## Basic information

|                 |                                |
|-----------------|--------------------------------|
| **Object type** | `functions.ConvertTimezone`    |
| **Since**       | 0.1.0                          |
| **Dialects**    | `MySQL` `MariaDB`              |

## Object attributes

| Attribute       | Accepts                                                  | Required |
|-----------------|----------------------------------------------------------|----------|
| obj             | `functions.ConvertTimezone`                              | True     |
| property        | `functions.*` `Property` `Constant`                      | True     |
| date_from       | `Constant`                                               | True     |
| date_to         | `Constant`                                               | True     |
| alias           | String                                                   | False    |

## JSON format

```json
{
  "obj": "functions.ConvertTimezone",
  "property": {
    "obj": "properties.Property",
    "name": "users.name"
  },
  "date_from": {
    "obj": "properties.Constant",
    "value": "+00:00"
  },
  "date_to": {
    "obj": "properties.Constant",
    "value": "Europe/Bratislava"
  },
  "alias": "my_time"
}
```

## SQL

```sql
CONVERT_TZ(users.name, '+00:00', 'Europe/Bratislava') AS my_time
```
