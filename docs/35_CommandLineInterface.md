### Command Line Interface

The `teradatasql` module provides a command line interface via the `python -m` option.

Running the `teradatasql` module without additional arguments prints a usage message.

Platform       | Command
-------------- | ---
macOS or Linux | `python -m teradatasql`
Windows        | `py -3 -m teradatasql`

Any number of arguments can follow the `teradatasql` module name on the command line, and arguments can be repeated on the command line.

The command line interface can print the `teradatasql` version number.

Platform       | Command
-------------- | ---
macOS or Linux | `python -m teradatasql version`
Windows        | `py -3 -m teradatasql version`

Specify connection parameters to connect to a database.

Connection parameters begin with `host=` and consist of comma-separated key`=`value pairs. A repeated comma `,,` in a connection parameter value is treated as a single literal comma.

Platform       | Command
-------------- | ---
macOS or Linux | `python -m teradatasql host=whomooz,user=guest,password=please`
Windows        | `py -3 -m teradatasql host=whomooz,user=guest,password=please`

This feature serves as a database connectivity test.

SQL requests can be executed after a database connection is established.

Platform       | Command
-------------- | ---
macOS or Linux | `python -m teradatasql host=whomooz,user=guest,password=please "select * from DBC.DBCInfo"`
Windows        | `py -3 -m teradatasql host=whomooz,user=guest,password=please "select * from DBC.DBCInfo"`

<a id="ChangeLog"></a>

