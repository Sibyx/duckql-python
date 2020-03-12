# StringAgg

## Basic information

|                 |                                |
|-----------------|--------------------------------|
| **Object type** | `functions.StringAgg`          |
| **Since**       | 0.1.0                          |
| **Dialects**    | `MySQL` `MariaDB` `PostgreSQL` |

## Object attributes

| Attribute       | Accepts                                                  | Required |
|-----------------|----------------------------------------------------------|----------|
| obj             | `functions.StringAgg`                                          | True     |
| property        | string                                                   | True     |
| alias           | String                                                   | False    |

## JSON format

```json
{
  "obj": "functions.Sum",
  "property": {
    "obj": "properties.Property",
    "name": "transactions.amount"
  },
  "alias": "total_amount"
}
```

## SQL

```sql
SUM(transactions.amount) AS total_amount
```
