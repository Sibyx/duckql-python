# Sum

## Basic information

|                 |                                |
|-----------------|--------------------------------|
| **Object type** | `functions.Sum`                |
| **Since**       | 0.1.0                          |
| **Dialects**    | `MySQL` `MariaDB` `PostgreSQL` |

## Object attributes

| Attribute       | Accepts                                                  | Required |
|-----------------|----------------------------------------------------------|----------|
| obj             | `functions.Sum`                                          | True     |
| property        | `functions.*` `Property` `CastOperator`                  | True     |
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
