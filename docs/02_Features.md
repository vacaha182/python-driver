### Features

The *Teradata SQL Driver for Python* is a DBAPI Driver that enables Python applications to connect to the Teradata Database. The driver implements the [PEP-249 Python Database API Specification 2.0](https://www.python.org/dev/peps/pep-0249/).

The driver is a young product that offers a basic feature set. We are working diligently to add features to the driver, and our goal is feature parity with the Teradata JDBC Driver.

At the present time, the driver offers the following features.

* Supported for use with Teradata database 16.20 and later releases.
* [COP Discovery](#COPDiscovery).
* Laddered Concurrent Connect.
* [HTTPS](https://en.wikipedia.org/wiki/HTTPS)/[TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security) connections with Teradata database 16.20.53.30 and later.
* Encrypted logon.
* [GSS-API](https://en.wikipedia.org/wiki/Generic_Security_Services_Application_Program_Interface) logon authentication methods `KRB5` (Kerberos), `LDAP`, `TD2`, and `TDNEGO`.
* [OpenID Connect (OIDC)](https://en.wikipedia.org/wiki/OpenID#OpenID_Connect_(OIDC)) logon authentication methods `BEARER`, `BROWSER`, `CODE`, `CRED`, `JWT`, `ROPC`, and `SECRET`.
* Data encryption provided by TLS for HTTPS connections.
* For non-HTTPS connections, data encryption governed by central administration or enabled via the `encryptdata` connection parameter.
* Recoverable Network Protocol and Redrive.
* Unicode character data transferred via the UTF8 session character set.
* [Auto-commit](#AutoCommit) for ANSI and TERA transaction modes.
* Result set row size up to 1 MB.
* Multi-statement requests that return multiple result sets.
* Most JDBC escape syntax.
* Parameterized SQL requests with question-mark parameter markers.
* Parameterized batch SQL requests with multiple rows of data bound to question-mark parameter markers.
* Auto-Generated Key Retrieval (AGKR) for identity column values and more.
* Large Object (LOB) support for the BLOB and CLOB data types.
* Complex data types such as `XML`, `JSON`, `DATASET STORAGE FORMAT AVRO`, and `DATASET STORAGE FORMAT CSV`.
* ElicitFile protocol support for DDL commands that create external UDFs or stored procedures and upload a file from client to database.
* `CREATE PROCEDURE` and `REPLACE PROCEDURE` commands.
* Stored Procedure Dynamic Result Sets.
* FastLoad and FastExport.
* Monitor partition.

<a id="Limitations"></a>

