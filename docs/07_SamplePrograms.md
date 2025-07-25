### Sample Programs

Sample programs are provided to demonstrate how to use the driver. When the driver is installed, the sample programs are placed in the `teradatasql/samples` directory under your Python installation directory.

The sample programs are coded with a fake database hostname `whomooz`, username `guest`, and password `please`. Substitute your actual database hostname and credentials before running a sample program.

Program                                                                                                             | Purpose
------------------------------------------------------------------------------------------------------------------- | ---
[AGKRBatchInsert.py](https://github.com/Teradata/python-driver/blob/master/samples/AGKRBatchInsert.py)              | Demonstrates how to insert a batch of rows with Auto-Generated Key Retrieval (AGKR)
[AGKRInsertSelect.py](https://github.com/Teradata/python-driver/blob/master/samples/AGKRInsertSelect.py)            | Demonstrates Insert/Select with Auto-Generated Key Retrieval (AGKR)
[BatchInsert.py](https://github.com/Teradata/python-driver/blob/master/samples/BatchInsert.py)                      | Demonstrates how to insert a batch of rows
[BatchInsertCSV.py](https://github.com/Teradata/python-driver/blob/master/samples/BatchInsertCSV.py)                | Demonstrates how to insert a batch of rows from a CSV file
[BatchInsPerf.py](https://github.com/Teradata/python-driver/blob/master/samples/BatchInsPerf.py)                    | Measures time to insert one million rows
[CancelSleep.py](https://github.com/Teradata/python-driver/blob/master/samples/CancelSleep.py)                      | Demonstrates how to use the cancel method to interrupt a query
[CharPadding.py](https://github.com/Teradata/python-driver/blob/master/samples/CharPadding.py)                      | Demonstrates the database's *Character Export Width* behavior
[CommitRollback.py](https://github.com/Teradata/python-driver/blob/master/samples/CommitRollback.py)                | Demonstrates commit and rollback methods with auto-commit off.
[DecimalDigits.py](https://github.com/Teradata/python-driver/blob/master/samples/DecimalDigits.py)                  | Demonstrates how to format decimal.Decimal values.
[DriverDatabaseVersion.py](https://github.com/Teradata/python-driver/blob/master/samples/DriverDatabaseVersion.py)  | Displays the driver version and database version
[ElicitFile.py](https://github.com/Teradata/python-driver/blob/master/samples/ElicitFile.py)                        | Demonstrates C source file upload to create a User-Defined Function (UDF)
[ExportCSVResult.py](https://github.com/Teradata/python-driver/blob/master/samples/ExportCSVResult.py)              | Demonstrates how to export a query result set to a CSV file
[ExportCSVResults.py](https://github.com/Teradata/python-driver/blob/master/samples/ExportCSVResults.py)            | Demonstrates how to export multiple query result sets to CSV files
[FakeExportCSVResults.py](https://github.com/Teradata/python-driver/blob/master/samples/FakeExportCSVResults.py)    | Demonstrates how to export multiple query result sets with the metadata to CSV files
[FakeResultSetCon.py](https://github.com/Teradata/python-driver/blob/master/samples/FakeResultSetCon.py)            | Demonstrates connection parameter for fake result sets
[FakeResultSetEsc.py](https://github.com/Teradata/python-driver/blob/master/samples/FakeResultSetEsc.py)            | Demonstrates escape function for fake result sets
[FastExportCSV.py](https://github.com/Teradata/python-driver/blob/master/samples/FastExportCSV.py)                  | Demonstrates how to FastExport rows from a table to a CSV file
[FastExportTable.py](https://github.com/Teradata/python-driver/blob/master/samples/FastExportTable.py)              | Demonstrates how to FastExport rows from a table
[FastLoadBatch.py](https://github.com/Teradata/python-driver/blob/master/samples/FastLoadBatch.py)                  | Demonstrates how to FastLoad batches of rows
[FastLoadCSV.py](https://github.com/Teradata/python-driver/blob/master/samples/FastLoadCSV.py)                      | Demonstrates how to FastLoad batches of rows from a CSV file
[HelpSession.py](https://github.com/Teradata/python-driver/blob/master/samples/HelpSession.py)                      | Displays session information
[IgnoreErrors.py](https://github.com/Teradata/python-driver/blob/master/samples/IgnoreErrors.py)                    | Demonstrates how to ignore errors
[InsertLob.py](https://github.com/Teradata/python-driver/blob/master/samples/InsertLob.py)                          | Demonstrates how to insert BLOB and CLOB values
[InsertXML.py](https://github.com/Teradata/python-driver/blob/master/samples/InsertXML.py)                          | Demonstrates how to insert and retrieve XML values
[LoadCSVFile.py](https://github.com/Teradata/python-driver/blob/master/samples/LoadCSVFile.py)                      | Demonstrates how to load data from a CSV file into a table
[LobLocators.py](https://github.com/Teradata/python-driver/blob/master/samples/LobLocators.py)                      | Demonstrates how to use LOB locators
[MetadataFromPrepare.py](https://github.com/Teradata/python-driver/blob/master/samples/MetadataFromPrepare.py)      | Demonstrates how to prepare a SQL request and obtain SQL statement metadata
[MonitorAbort.py](https://github.com/Teradata/python-driver/blob/master/samples/MonitorAbort.py)                    | Demonstrates how to use the Monitor partition to abort a session
[MonitorQueries.py](https://github.com/Teradata/python-driver/blob/master/samples/MonitorQueries.py)                | Demonstrates how to execute Monitor partition queries
[MultiThread.py](https://github.com/Teradata/python-driver/blob/master/samples/MultiThread.py)                      | Demonstrates how to use multiple threads to load data in parallel
[ParamDataTypes.py](https://github.com/Teradata/python-driver/blob/master/samples/ParamDataTypes.py)                | Demonstrates how to specify data types for parameter marker bind values
[ShowCommand.py](https://github.com/Teradata/python-driver/blob/master/samples/ShowCommand.py)                      | Displays the results from the `SHOW` command
[StoredProc.py](https://github.com/Teradata/python-driver/blob/master/samples/StoredProc.py)                        | Demonstrates how to create and call a SQL stored procedure
[TJEncryptPassword.py](https://github.com/Teradata/python-driver/blob/master/samples/TJEncryptPassword.py)          | Creates encrypted password files

<a id="Using"></a>

