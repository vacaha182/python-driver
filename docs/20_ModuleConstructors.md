### Module Constructors

`teradatasql.connect(` *JSONConnectionString* `,` *Parameters...* `)`

Creates a connection to the database and returns a Connection object.

The first parameter is an optional JSON string that defaults to `None`. The second and subsequent arguments are optional `kwargs`. Specify connection parameters as a JSON string, as `kwargs`, or a combination of the two.

When a combination of parameters are specified, connection parameters specified as `kwargs` take precedence over same-named connection parameters specified in the JSON string.

---

`teradatasql.Date(` *Year* `,` *Month* `,` *Day* `)`

Creates and returns a `datetime.date` value.

---

`teradatasql.DateFromTicks(` *Seconds* `)`

Creates and returns a `datetime.date` value corresponding to the specified number of seconds after 1970-01-01 00:00:00.

---

`teradatasql.Time(` *Hour* `,` *Minute* `,` *Second* `)`

Creates and returns a `datetime.time` value.

---

`teradatasql.TimeFromTicks(` *Seconds* `)`

Creates and returns a `datetime.time` value corresponding to the specified number of seconds after 1970-01-01 00:00:00.

---

`teradatasql.Timestamp(` *Year* `,` *Month* `,` *Day* `,` *Hour* `,` *Minute* `,` *Second* `)`

Creates and returns a `datetime.datetime` value.

---

`teradatasql.TimestampFromTicks(` *Seconds* `)`

Creates and returns a `datetime.datetime` value corresponding to the specified number of seconds after 1970-01-01 00:00:00.

<a id="ModuleFunctions"></a>

