### Client Attributes

Client Attributes record a variety of information about the client system and client software in the system tables `DBC.SessionTbl` and `DBC.EventLog`. Client Attributes are intended to be a replacement for the information recorded in the `LogonSource` column of the system tables `DBC.SessionTbl` and `DBC.EventLog`.

The Client Attributes are recorded at session logon time. Subsequently, the system views `DBC.SessionInfoV` and `DBC.LogOnOffV` can be queried to obtain information about the client system and client software on a per-session basis. Client Attribute values may be recorded in the database in either mixed-case or in uppercase, depending on the session character set and other factors. Analysis of recorded Client Attributes must flexibly accommodate either mixed-case or uppercase values.

Warning: The information in this section is subject to change in future releases of the driver. Client Attributes can be "mined" for information about client system demographics; however, any applications that parse Client Attribute values must be changed if Client Attribute formats are changed in the future.

Client Attributes are not intended to be used for workload management. Instead, query bands are intended for workload management. Any use of Client Attributes for workload management may break if Client Attributes are changed, or augmented, in the future.

Client Attribute            | Source   | Description
--------------------------- | -------- | ---
`MechanismName`             | database | The connection's logon mechanism; for example, TD2, LDAP, etc.
`ClientIpAddress`           | database | The client IP address, as determined by the database
`ClientTcpPortNumber`       | database | The connection's client TCP port number, as determined by the database
`ClientIPAddrByClient`      | driver   | The client IP address, as determined by the driver
`ClientPortByClient`        | driver   | The connection's client TCP port number, as determined by the driver
`ClientInterfaceKind`       | driver   | The value `P` to indicate Python, available beginning with Teradata Database 17.20.03.19
`ClientInterfaceVersion`    | driver   | The driver version, available beginning with Teradata Database 17.20.03.19
`ClientProgramName`         | driver   | The client program name, followed by a streamlined call stack
`ClientSystemUserId`        | driver   | The client user name
`ClientOsName`              | driver   | The client operating system name
`ClientProcThreadId`        | driver   | The client process ID
`ClientVmName`              | driver   | Python runtime information
`ClientSecProdGrp`          | driver   | Go crypto library version
`ClientCoordName`           | driver   | The proxy server hostname and port number when a proxy server is used for a database connection
`ClientTerminalId`          | driver   | The proxy server hostname and port number when a proxy server is used for an Identity Provider
`ClientSessionDesc`         | driver   | TLS cipher information is available in this column as a list of name=value pairs, each terminated by a semicolon. Individual values can be accessed using the `NVP` system function.
&nbsp; | `C` | Y/N indicates whether the `sslcipher` connection parameter was specified
&nbsp; | `D` | the database TLS cipher
&nbsp; | `I` | the Identity Provider TLS cipher
`ClientTdHostName`          | driver   | The database hostname as specified by the application, without any COP suffix
`ClientCOPSuffixedHostName` | driver   | The COP-suffixed database hostname chosen by the driver
`ServerIPAddrByClient`      | driver   | The database node's IP address, as determined by the driver
`ServerPortByClient`        | driver   | The destination port number of the TCP connection to the database node, as determined by the driver
`ClientConfType`            | driver   | The confidentiality type, as determined by the driver
&nbsp;                      | `V`      | TLS used for encryption, with full certificate verification
&nbsp;                      | `C`      | TLS used for encryption, with Certificate Authority (CA) verification
&nbsp;                      | `R`      | TLS used for encryption, with no certificate verification
&nbsp;                      | `E`      | TLS was not attempted, and TDGSS used for encryption
&nbsp;                      | `U`      | TLS was not attempted, and TDGSS encryption depends on central administration
&nbsp;                      | `F`      | TLS was attempted, but the TLS handshake failed, so this is a fallback to using TDGSS for encryption
&nbsp;                      | `H`      | SSLMODE was set to PREFER, but a non-TLS connection was made, and TDGSS encryption depends on central administration
`ServerConfType`            | database | The confidentiality type, as determined by the database
&nbsp;                      | `T`      | TLS used for encryption
&nbsp;                      | `E`      | TDGSS used for encryption
&nbsp;                      | `U`      | Data transfer is unencrypted
`ClientConfVersion`         | database | The TLS version as determined by the database, if this is an HTTPS/TLS connection
`ClientConfCipherSuite`     | database | The TLS cipher as determined by the database, if this is an HTTPS/TLS connection
`ClientEnvName`             | driver   | The OIDC metadata URL for a connection using an OIDC logon authentication mechanism
`ClientJobId`               | driver   | The OIDC client ID for a connection using an OIDC logon authentication mechanism
`ClientJobName`             | driver   | The OIDC scope for a connection using an OIDC logon authentication mechanism
`ClientJobData`             | driver   | The OIDC login hint for a connection using an OIDC logon authentication mechanism
`ClientUserOperId`          | driver   | The OIDC token kind, OIDC claim name, and claim value for a connection using an OIDC logon authentication mechanism
`ClientWorkload`            | driver   | The scopes for acquired OAuth tokens, separated by vertical bar `\|` characters
`ClientAttributesEx`        | driver   | Additional Client Attributes are available in the `ClientAttributesEx` column as a list of name=value pairs, each terminated by a semicolon. Individual values can be accessed using the `NVP` system function.
&nbsp;                      | `AS`     | the application connection's endpoint session number
&nbsp;                      | `BA`     | Y/N indicator for Browser Authentication
&nbsp;                      | `CCS`    | the client character set
&nbsp;                      | `CERT`   | the database TLS certificate status (see [table below](#CertStatus))
&nbsp;                      | `CF`     | the `connect_function` connection parameter
&nbsp;                      | `CRC`    | the `sslcrc` connection parameter
&nbsp;                      | `CRL`    | Y/N indicator for `sslcrl` connection parameter
&nbsp;                      | `CS`     | the control session's endpoint session number
&nbsp;                      | `DL`     | this connection's database logon sequence number
&nbsp;                      | `DP`     | the `dbs_port` connection parameter
&nbsp;                      | `EL`     | this connection's endpoint logon sequence number
&nbsp;                      | `ENC`    | Y/N indicator for `encryptdata` connection parameter
&nbsp;                      | `ES`     | endpoint session number if connected to an endpoint such as Unity, Session Manager, or Business Continuity Manager; database session number otherwise
&nbsp;                      | `FIPS`   | Y/N indicator for FIPS mode
&nbsp;                      | `GO`     | the Go version
&nbsp;                      | `GOV`    | the `govern` connection parameter
&nbsp;                      | `HP`     | the `https_port` connection parameter
&nbsp;                      | `HR`     | the `https_retry` connection parameter and number of HTTPS retries
&nbsp;                      | `IDPC`   | the Identity Provider TLS certificate status (see [table below](#CertStatus))
&nbsp;                      | `JH`     | JWT header parameters to identify signature key
&nbsp;                      | `JWS`    | the JSON Web Signature (JWS) algorithm
&nbsp;                      | `LM`     | the logon authentication method
&nbsp;                      | `LOB`    | Y/N indicator for LOB support
&nbsp;                      | `OA`     | the `oauth_level` connection parameter
&nbsp;                      | `OAC`    | sequence of comma-separated OAuth token reuse counts
&nbsp;                      | `OAR`    | sequence of Y/N values to indicate OAuth refresh token availability
&nbsp;                      | `OC`     | OIDC token cache status O (off) M (miss) H (hit) X (expired)
&nbsp;                      | `OCSP`   | Y/N indicator for `sslocsp` connection parameter
&nbsp;                      | `OSL`    | Numeric level corresponding to `oidc_sslmode`
&nbsp;                      | `OSM`    | the `oidc_sslmode` connection parameter
&nbsp;                      | `PART`   | the `partition` connection parameter
&nbsp;                      | `PYTHON` | the Python version
&nbsp;                      | `RT`     | Y/N indicator for OIDC refresh token available
&nbsp;                      | `SC`     | socket connect attempts and failures
&nbsp;                      | `SCS`    | the session character set
&nbsp;                      | `SIP`    | Y/N indicator for StatementInfo parcel support
&nbsp;                      | `SSL`    | Numeric level corresponding to `sslmode`
&nbsp;                      | `SSLM`   | the `sslmode` connection parameter
&nbsp;                      | `SSLP`   | the `sslprotocol` connection parameter
&nbsp;                      | `TC`     | OIDC token reuse count
&nbsp;                      | `TM`     | the transaction mode indicator A (ANSI) or T (TERA)
&nbsp;                      | `TT`     | OIDC token time-to-live in seconds
&nbsp;                      | `TVD`    | the database TLS protocol version
&nbsp;                      | `TVI`    | the Identity Provider TLS protocol version
&nbsp;                      | `TZ`     | the current time zone

<a id="CertStatus"></a>

The `CERT` and `IDPC` attributes indicate the TLS certificate status of an HTTPS/TLS connection. When the attribute indicates the TLS certificate is valid (`V`) or invalid (`I`), then additional TLS certificate status details are provided as a series of comma-separated two-letter codes.

Code | Description
-----|---
`U`  | the TLS certificate status is unavailable
`V`  | the TLS certificate status is valid
`I`  | the TLS certificate status is invalid
`BU` | sslbase64 is unavailable for server certificate verification
`BA` | server certificate was accepted by sslbase64
`BR` | server certificate was rejected by sslbase64
`PU` | sslca PEM file is unavailable for server certificate verification
`PA` | server certificate was verified using sslca PEM file
`PR` | server certificate was rejected using sslca PEM file
`DU` | sslcapath PEM directory is unavailable for server certificate verification
`DA` | server certificate was verified using sslcapath PEM directory
`DR` | server certificate was rejected using sslcapath PEM directory
`TA` | server certificate was verified by the system
`TR` | server certificate was rejected by the system
`CY` | server certificate passed VERIFY-CA check
`CN` | server certificate failed VERIFY-CA check
`HU` | server hostname is unavailable for server certificate matching, because database IP address was specified
`HY` | server hostname matches server certificate
`HN` | server hostname does not match server certificate
`RU` | resolved server hostname is unavailable for server certificate matching, because database IP address was specified
`RY` | resolved server hostname matches server certificate
`RN` | resolved server hostname does not match server certificate
`IY` | IP address matches server certificate
`IN` | IP address does not match server certificate
`FY` | server certificate passed VERIFY-FULL check
`FN` | server certificate failed VERIFY-FULL check
`SU` | certificate revocation check status is unavailable
`SG` | certificate revocation check status is good
`SR` | certificate revocation check status is revoked

#### LogonSource Column

The `LogonSource` column is obsolete and has been superseded by Client Attributes. The `LogonSource` column may be deprecated and subsequently removed in future releases of the database.

When the driver establishes a connection to the database, the driver composes a string value that is stored in the `LogonSource` column of the system tables `DBC.SessionTbl` and `DBC.EventLog`. The `LogonSource` column is included in system views such as `DBC.SessionInfoV` and `DBC.LogOnOffV`. All `LogonSource` values are recorded in the database in uppercase.

The driver follows the format documented in the Teradata Data Dictionary, section "System Views Columns Reference", for network-attached `LogonSource` values. Network-attached `LogonSource` values have eight fields, separated by whitespace. The database composes fields 1 through 3, and the driver composes fields 4 through 8.

Field | Source   | Description
----- | -------- | ---
1     | database | The string `(TCP/IP)` to indicate the connection type
2     | database | The connection's client TCP port number, in hexadecimal
3     | database | The client IP address, as determined by the database
4     | driver   | The database hostname as specified by the application, without any COP suffix
5     | driver   | The client process ID
6     | driver   | The client user name
7     | driver   | The client program name
8     | driver   | The string `01 LSS` to indicate the `LogonSource` string version `01`

<a id="UserStartup"></a>

