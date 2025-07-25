### Cursor Methods

`.callproc(` *ProcedureName* `,` *OptionalSequenceOfParameterValues* `)`

Calls the stored procedure specified by *ProcedureName*.
Provide the second argument as a sequence of `IN` and `INOUT` parameter values to bind the values to question-mark parameter markers in the SQL request.
Specifying parameter values as a mapping is not supported.
Returns a result set consisting of the `INOUT` parameter output values, if any, followed by any dynamic result sets.

`OUT` parameters are not supported by this method. Use `.execute` to call a stored procedure with `OUT` parameters.

---

`.close()`

Closes the Cursor.

---

`.execute(` *SQLRequest* `,` *OptionalSequenceOfParameterValues* `, ignoreErrors=` *OptionalSequenceOfIgnoredErrorCodes* `)`

Executes the SQL request.
If a sequence of parameter values is provided as the second argument, the values will be bound to question-mark parameter markers in the SQL request. Specifying parameter values as a mapping is not supported.

The `ignoreErrors` parameter is optional. The ignored error codes must be specified as a sequence of integers.

---

`.executemany(` *SQLRequest* `,` *SequenceOfSequencesOfParameterValues* `, ignoreErrors=` *OptionalSequenceOfIgnoredErrorCodes* `)`

Executes the SQL request as an iterated SQL request for the batch of parameter values.
The batch of parameter values must be specified as a sequence of sequences. Specifying parameter values as a mapping is not supported.

The `ignoreErrors` parameter is optional. The ignored error codes must be specified as a sequence of integers.

---

`.fetchall()`

Fetches all remaining rows of the current result set.
Returns a sequence of sequences of column values.

---

`.fetchmany(` *OptionalRowCount* `)`

Fetches the next series of rows of the current result set.
The argument specifies the number of rows to fetch. If no argument is provided, then the Cursor's `.arraysize` attribute will determine the number of rows to fetch.
Returns a sequence of sequences of column values, or an empty sequence to indicate that all rows have been fetched.

---

`.fetchone()`

Fetches the next row of the current result set.
Returns a sequence of column values, or `None` to indicate that all rows have been fetched.

---

`.nextset()`

Advances to the next result set.
Returns `True` if another result set is available, or `None` to indicate that all result sets have been fetched.

---

`.setinputsizes(` *SequenceOfTypesOrSizes* `)`

Has no effect.

---

`.setoutputsize(` *Size* `,` *OptionalColumnIndex* `)`

Has no effect.

<a id="TypeObjects"></a>

