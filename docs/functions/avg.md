# Avg

|                 |                                |
|-----------------|--------------------------------|
| **Object type** | `functions.Avg`                |
| **Since**       | 0.1.0                          |
| **Dialects**    | `MySQL` `MariaDB` `PostgreSQL` |

**JSON format**

```json
{
  "obj": "functions.Avg",
  "property": {
    "obj": "properties.Property",
    "name": "users.name"
  },
  "alias": "avg_name"
}
```

**SQL**

```sql
AVG(users.name) AS avg_name
```

**JSON schema**

```json
{
  "title": "Avg",
  "description": "Helper class that provides a standard way to create an ABC using\ninheritance.",
  "type": "object",
  "properties": {
    "obj": {
      "title": "Obj",
      "default": "functions.Avg",
      "const": "functions.Avg",
      "type": "string"
    },
    "property": {
      "$ref": "#/definitions/Property"
    },
    "alias": {
      "title": "Alias",
      "type": "string"
    }
  },
  "required": [
    "property"
  ],
  "definitions": {
    "Property": {
      "title": "Property",
      "description": "Helper class that provides a standard way to create an ABC using\ninheritance.",
      "type": "object",
      "properties": {
        "obj": {
          "title": "Obj",
          "default": "properties.Property",
          "const": "properties.Property",
          "type": "string"
        },
        "name": {
          "title": "Name",
          "type": "string"
        },
        "alias": {
          "title": "Alias",
          "type": "string"
        }
      },
      "required": [
        "name"
      ]
    }
  }
}
```

**SQL reference**

- [PostgreSQL](https://www.postgresql.org/docs/current/functions-aggregate.html)
- [MySQL](https://dev.mysql.com/doc/refman/8.0/en/group-by-functions.html#function_avg)
- [MariaDB](https://mariadb.com/kb/en/avg/)
