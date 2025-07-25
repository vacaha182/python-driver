### Connection Methods

`.cancel()`

Attempts to cancel the currently executing SQL request, if one is currently executing. Does nothing if called when no SQL request is executing.

This method must be called from a thread other than the thread which is blocked while executing the SQL request.

---

`.close()`

Closes the Connection.

---

`.commit()`

Commits the current transaction.

---

`.cursor()`

Creates and returns a new Cursor object for the Connection.

---

`.nativeSQL(` *SQLRequest* `)`

Returns the specified SQL request text after conversion to native Teradata SQL. Equivalent to the JDBC API `Connection.nativeSQL` method.

The `{fn teradata_nativesql}` escape clause is automatically prepended to the SQL request before processing.

---

`.rollback()`

Rolls back the current transaction.

<a id="CursorAttributes"></a>

