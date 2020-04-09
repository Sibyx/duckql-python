# Join

## Basic information

|                 |                                |
|-----------------|--------------------------------|
| **Object type** | `structures.Join`              |
| **Since**       | 0.1.0                          |
| **Dialects**    | `MySQL` `MariaDB` `PostgreSQL` |

## Object attributes

| Attribute       | Accepts                                                                                | Required |
|-----------------|----------------------------------------------------------------------------------------|----------|
| obj             | `structures.Join`                                                                      | True     |
| entity          | String                                                                                 | True     |
| type            | Enum[`left` `right` `inner` `outer` `cross` `full_outer` `left_outer` `right_outer` `natural`]   | True     |
| on              | `Comparision` `Operator`                                                               | True     |
| alias           | String                                                                                 | False    |


## JSON format

```json
{
  "obj": "structures.Join",
  "entity": "transactions",
  "type": "left",
  "on": {
    "obj": "structures.Operator",
    "operation": "and",
    "properties": [
      {
        "obj": "structures.Comparision",
        "properties": [
          {
            "obj": "properties.Property",
            "name": "t.user_id"
          },
          {
            "obj": "properties.Property",
            "name": "users.id"
          }
        ],
        "operation": "eq"
      },
      {
        "obj": "structures.Comparision",
        "properties": [
          {
            "obj": "properties.Property",
            "name": "t.creator_id"
          },
          {
            "obj": "properties.Property",
            "name": "users.id"
          }
        ],
        "operation": "neq"
      }
    ]
  },
  "alias": "t"
}
```

**SQL**

```sql
LEFT JOIN transactions t ON ((t.user_id = users.id) AND (t.creator_id != users.id))
```

