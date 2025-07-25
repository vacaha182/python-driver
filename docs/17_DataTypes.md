### Data Types

The table below lists the database data types supported by the driver, and indicates the corresponding Python data type returned in result set rows.

Database data type                 | Result set Python data type       | With `teradata_values` as `false`
---------------------------------- | --------------------------------- | ---
`BIGINT`                           | `int`                             |
`BLOB`                             | `bytes`                           |
`BYTE`                             | `bytes`                           |
`BYTEINT`                          | `int`                             |
`CHAR`                             | `str`                             |
`CLOB`                             | `str`                             |
`DATE`                             | `datetime.date`                   | `str`
`DECIMAL`                          | `decimal.Decimal`                 | `str`
`FLOAT`                            | `float`                           |
`INTEGER`                          | `int`                             |
`INTERVAL YEAR`                    | `str`                             |
`INTERVAL YEAR TO MONTH`           | `str`                             |
`INTERVAL MONTH`                   | `str`                             |
`INTERVAL DAY`                     | `str`                             |
`INTERVAL DAY TO HOUR`             | `str`                             |
`INTERVAL DAY TO MINUTE`           | `str`                             |
`INTERVAL DAY TO SECOND`           | `str`                             |
`INTERVAL HOUR`                    | `str`                             |
`INTERVAL HOUR TO MINUTE`          | `str`                             |
`INTERVAL HOUR TO SECOND`          | `str`                             |
`INTERVAL MINUTE`                  | `str`                             |
`INTERVAL MINUTE TO SECOND`        | `str`                             |
`INTERVAL SECOND`                  | `str`                             |
`NUMBER`                           | `decimal.Decimal`                 | `str`
`PERIOD(DATE)`                     | `str`                             |
`PERIOD(TIME)`                     | `str`                             |
`PERIOD(TIME WITH TIME ZONE)`      | `str`                             |
`PERIOD(TIMESTAMP)`                | `str`                             |
`PERIOD(TIMESTAMP WITH TIME ZONE)` | `str`                             |
`SMALLINT`                         | `int`                             |
`TIME`                             | `datetime.time`                   | `str`
`TIME WITH TIME ZONE`              | `datetime.time` with `tzinfo`     | `str`
`TIMESTAMP`                        | `datetime.datetime`               | `str`
`TIMESTAMP WITH TIME ZONE`         | `datetime.datetime` with `tzinfo` | `str`
`VARBYTE`                          | `bytes`                           |
`VARCHAR`                          | `str`                             |
`XML`                              | `str`                             |

The table below lists the parameterized SQL bind-value Python data types supported by the driver, and indicates the corresponding database data type transmitted to the server.

Bind-value Python data type       | Database data type
--------------------------------- | ---
`bytes`                           | `VARBYTE`
`datetime.date`                   | `DATE`
`datetime.datetime`               | `TIMESTAMP`
`datetime.datetime` with `tzinfo` | `TIMESTAMP WITH TIME ZONE`
`datetime.time`                   | `TIME`
`datetime.time` with `tzinfo`     | `TIME WITH TIME ZONE`
`datetime.timedelta`              | `VARCHAR` format compatible with `INTERVAL DAY TO SECOND`
`decimal.Decimal`                 | `NUMBER`
`float`                           | `FLOAT`
`int`                             | `BIGINT`
`str`                             | `VARCHAR`

Transforms are used for SQL `ARRAY` data values, and they can be transferred to and from the database as `VARCHAR` values.

Transforms are used for structured UDT data values, and they can be transferred to and from the database as `VARCHAR` values.

<a id="NullValues"></a>

