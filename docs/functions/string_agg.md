# StringAgg

## Basic information

|                 |                                |
|-----------------|--------------------------------|
| **Object type** | `functions.StringAgg`          |
| **Since**       | 0.1.6                          |
| **Dialects**    | `MySQL` `MariaDB` `PostgreSQL` |

## Object attributes

| Attribute       | Accepts                                                  | Required |
|-----------------|----------------------------------------------------------|----------|
| obj             | `functions.StringAgg`                                    | True     |
| property        | `functions.*` `Property` `Array` `structures.distinct`   | True     |
| separator       | string                                                   | True     |
| alias           | String                                                   | False    |

## JSON format

```json
{
  "obj": "functions.StringAgg",
  "property": {
    "obj": "properties.Property",
    "name": "transactions.amount"
  },
  "separator": ", ",
  "alias": "amounts"
}
```

## SQL

```sql
STRING_AGG(transactions.amount, ', ') AS amounts
```
