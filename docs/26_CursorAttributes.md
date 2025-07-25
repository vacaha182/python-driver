### Cursor Attributes

`.activityname`

Read-only `str` attribute indicating the activity name of the current SQL statement, such as `Select`, `Insert`, or `Update`.

The value `unknown` indicates the database provided an activity type code that the driver does not recognize.

---

`.activitytype`

Read-only `int` attribute indicating the activity type code of the current SQL statement, such as `1` for Select, `2` for Insert, or `3` for Update.

Activity type codes are documented in the [Activity Type section of the Teradata Call-Level Interface Version 2 Reference](https://docs.teradata.com/r/Enterprise_IntelliFlex_Lake_VMware/Teradata-Call-Level-Interface-Version-2-Reference-for-Workstation-Attached-Systems-17.20/Parcels/Common-Parcel-Fields/Activity-Type).

---

`.arraysize`

Read/write `int` attribute specifying the number of rows to fetch at a time with the `.fetchmany()` method. Defaults to `1` meaning fetch a single row at a time.

---

`.columntypename`

Read-only attribute consisting of a sequence of result set column type names, available after a SQL request is executed.

---

`.connection`

Read-only attribute indicating the Cursor's parent Connection object.

---

`.description`

Read-only attribute consisting of a sequence of seven-item sequences that each describe a result set column, available after a SQL request is executed.
* `.description[`*Column*`][0]` provides the column name.
* `.description[`*Column*`][1]` provides the column type code as an object comparable to one of the Type Objects listed below.
* `.description[`*Column*`][2]` provides the column display size in characters. Not implemented yet.
* `.description[`*Column*`][3]` provides the column size in bytes.
* `.description[`*Column*`][4]` provides the column precision if applicable, or `None` otherwise.
* `.description[`*Column*`][5]` provides the column scale if applicable, or `None` otherwise.
* `.description[`*Column*`][6]` provides the column nullability as `True` or `False`.

---

`.rowcount`

Read-only `int` attribute indicating the number of rows returned from, or affected by, the current SQL statement.

<a id="CursorMethods"></a>

