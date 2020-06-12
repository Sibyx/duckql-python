# ToDate

## Basic information

|                 |                                |
|-----------------|--------------------------------|
| **Object type** | `functions.ToDate`             |
| **Since**       | 0.4.0                          |
| **Dialects**    | `PostgreSQL`                   |

## Object attributes

| Attribute       | Accepts                                                       | Required |
|-----------------|---------------------------------------------------------------|----------|
| obj             | `functions.ToDate`                                            | True     |
| property        | `functions.*` `Property` `Constant` `CastOperator`            | True     |
| format          | String                                                        | True     |
| alias           | String                                                        | False    |

## JSON format

```json
{
  "obj": "functions.ToDate",
  "property": {
    "obj": "properties.Constant",
    "value": "05 Dec 2000"
  },
  "format": "DD Mon YYYY"
}
```

## SQL

```sql
to_date('05 Dec 2000', 'DD Mon YYYY')
```
