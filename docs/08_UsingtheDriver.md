### Using the Driver

Your Python script must import the `teradatasql` package in order to use the driver.

    import teradatasql

After importing the `teradatasql` package, your Python script calls the `teradatasql.connect` function to open a connection to the database.

You may specify connection parameters as a JSON string, as `kwargs`, or using a combination of the two approaches. The `teradatasql.connect` function's first argument is an optional JSON string. The `teradatasql.connect` function's second and subsequent arguments are optional `kwargs`.

Connection parameters specified only as `kwargs`:

    con = teradatasql.connect(host="whomooz", user="guest", password="please")

Connection parameters specified only as a JSON string:

    con = teradatasql.connect('{"host":"whomooz","user":"guest","password":"please"}')

Connection parameters specified using a combination:

    con = teradatasql.connect('{"host":"whomooz"}', user="guest", password="please")

When a combination of parameters are specified, connection parameters specified as `kwargs` take precedence over same-named connection parameters specified in the JSON string.

<a id="ConnectionParameters"></a>

