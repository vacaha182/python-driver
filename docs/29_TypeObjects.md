### Type Objects

`teradatasql.BINARY`

Identifies a SQL `BLOB`, `BYTE`, or `VARBYTE` column as a binary data type when compared with the Cursor's description attribute.

`.description[`*Column*`][1] == teradatasql.BINARY`

---

`teradatasql.DATETIME`

Identifies a SQL `DATE`, `TIME`, `TIME WITH TIME ZONE`, `TIMESTAMP`, or `TIMESTAMP WITH TIME ZONE` column as a date/time data type when compared with the Cursor's description attribute.

`.description[`*Column*`][1] == teradatasql.DATETIME`

---

`teradatasql.NUMBER`

Identifies a SQL `BIGINT`, `BYTEINT`, `DECIMAL`, `FLOAT`, `INTEGER`, `NUMBER`, or `SMALLINT` column as a numeric data type when compared with the Cursor's description attribute.

`.description[`*Column*`][1] == teradatasql.NUMBER`

---

`teradatasql.STRING`

Identifies a SQL `CHAR`, `CLOB`, `INTERVAL`, `PERIOD`, or `VARCHAR` column as a character data type when compared with the Cursor's description attribute.

`.description[`*Column*`][1] == teradatasql.STRING`

<a id="EscapeSyntax"></a>

