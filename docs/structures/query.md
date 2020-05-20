# Query

## Basic information

|                 |                                |
|-----------------|--------------------------------|
| **Object type** | `structures.Query`             |
| **Since**       | 0.1.0                          |
| **Dialects**    | `MySQL` `MariaDB` `PostgreSQL` |

## Object attributes

| Attribute       | Accepts                                                                                | Required |
|-----------------|----------------------------------------------------------------------------------------|----------|
| obj             | `structures.Query`                                                                     | True     |
| entity          | String                                                                                 | True     |
| properties      | List[`functions.*` `properties.Property` `structures.Distinct` `structures.CastOperator`] | True     |
| joins           | List[`structures.Join`]                                                                | False    |
| conditions      | `structures.Operator` `structures.Comparision`                                         | False    |
| order           | List[`structures.Order`]                                                               | False    |
| group           | List[`functions.*` `properties.Property`]                                              | False    |
| having          | `structures.Operator` `structures.Comparision`                                         | False    |
| limit           | `structures.Limit`                                                                     | False    |
| alias           | String                                                                                 | False    |

## JSON format

```json
{
  "obj": "structures.Query",
  "entity": "users",
  "properties": [
    {
      "obj": "properties.Property",
      "name": "users.name",
      "alias": "users_name"
    },
    {
      "obj": "functions.ConvertTimezone",
      "property": {
        "obj": "properties.Property",
        "name": "users.created_at",
        "alias": null
      },
      "date_from": {
        "obj": "properties.Constant",
        "value": "+00:00"
      },
      "date_to": {
        "obj": "properties.Constant",
        "value": "Europe/Bratislava"
      },
      "alias": "valid_timezone"
    }
  ],
  "joins": [
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
                "name": "transactions.user_id",
                "alias": null
              },
              {
                "obj": "properties.Property",
                "name": "users.id",
                "alias": null
              }
            ],
            "operation": "eq"
          },
          {
            "obj": "structures.Comparision",
            "properties": [
              {
                "obj": "properties.Property",
                "name": "transactions.creator_id",
                "alias": null
              },
              {
                "obj": "properties.Property",
                "name": "users.id",
                "alias": null
              }
            ],
            "operation": "neq"
          }
        ],
        "alias": null
      },
      "alias": null
    }
  ],
  "conditions": {
    "obj": "structures.Operator",
    "operation": "and",
    "properties": [
      {
        "obj": "structures.Comparision",
        "properties": [
          {
            "obj": "properties.Property",
            "name": "users.age",
            "alias": null
          },
          {
            "obj": "properties.Constant",
            "value": "15"
          }
        ],
        "operation": "gte"
      },
      {
        "obj": "structures.Comparision",
        "properties": [
          {
            "obj": "properties.Property",
            "name": "users.city",
            "alias": null
          },
          {
            "obj": "properties.Array",
            "values": [
              {
                "obj": "properties.Constant",
                "value": "Martin"
              },
              {
                "obj": "properties.Constant",
                "value": "Bratislava"
              }
            ]
          }
        ],
        "operation": "in"
      }
    ],
    "alias": null
  },
  "having": {
    "obj": "structures.Comparision",
    "properties": [
      {
        "obj": "functions.Sum",
        "property": {
          "obj": "properties.Property",
          "name": "transactions.value",
          "alias": null
        },
        "alias": null
      },
      {
        "obj": "properties.Constant",
        "value": "420"
      }
    ],
    "operation": "gt"
  },
  "order": [
    {
      "obj": "structures.Order",
      "property": {
        "obj": "properties.Property",
        "name": "users.surname",
        "alias": null
      },
      "kind": "ASC"
    },
    {
      "obj": "structures.Order",
      "property": {
        "obj": "properties.Property",
        "name": "users.name",
        "alias": null
      },
      "kind": "DESC"
    }
  ],
  "group": [
    {
      "obj": "properties.Property",
      "name": "users.email",
      "alias": null
    },
    {
      "obj": "properties.Property",
      "name": "users.id",
      "alias": null
    }
  ],
  "limit": {
    "obj": "structures.Limit",
    "limit": 10,
    "offset": 4
  },
  "alias": "my_query"
}
```

## SQL

```sql
(
	SELECT users.name,
	CONVERT_TZ(users.created_at, '+00:00', 'Europe/Bratislava')
	FROM users
	LEFT JOIN transactions ON
	(
		(transactions.user_id = users.id)
		AND (transactions.creator_id != users.id)
	)
	WHERE
	(
		(users.age >= 15)
		AND (users.city IN ('Martin', 'Bratislava'))
	)
	GROUP BY users.email, users.id
    HAVING (SUM(transactions.value) > 420)
	ORDER BY users.surname ASC, users.name DESC
	LIMIT 10 OFFSET 4
)
AS my_query
```
