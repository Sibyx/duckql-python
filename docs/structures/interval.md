# Interval

## Basic information

|                 |                                |
|-----------------|--------------------------------|
| **Object type** | `structures.Interval`          |
| **Since**       | 0.1.0                          |
| **Dialects**    | `MySQL` `MariaDB` `PostgreSQL` |

## Object attributes

| Attribute       | Accepts                                                                                | Required |
|-----------------|----------------------------------------------------------------------------------------|----------|
| obj             | `structures.Interval`                                                                  | True     |
| value           | Integer                                                                                | True     |
| unit            | Enum[`microsecond` `second` `minute` `hour` `day` `week` `month` `quarter` `year` `second_microsecond` `minute_microsecond` `minute_second` `hour_microsecond` `hour_second` `hour_minute` `day_microsecond` `day_second` `day_minute` `day_hour` `year_month`] | True     |

## JSON format

```json
{
  "obj": "structures.Interval",
  "value": -5,
  "unit": "day"
}
```

## SQL

```sql
INTERVAL '-5 DAY'
```

