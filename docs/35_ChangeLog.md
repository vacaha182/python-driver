### Change Log

`20.0.0.33` - July 7, 2025
* GOSQL-30 Recoverable Network Protocol and Redrive

`20.0.0.32` - June 11, 2025
* FastLoad to Vector column using transform Vector_IO or Vector_IO_VARCHAR

`20.0.0.31` - June 2, 2025
* Build DLL and shared library with standard Go 1.24.3
* Added import Crypto.Hash.HMAC to sample program TJEncryptPassword.py

`20.0.0.30` - April 25, 2025
* GOSQL-32 DBCCONS partition

`20.0.0.29` - April 22, 2025
* GOSQL-221 connection parameter https_retry
* GOSQL-222 connection parameter sslbase64

`20.0.0.28` - April 5, 2025
* GOSQL-219 sslnamedgroups connection parameter
* GOSQL-220 connection parameter oidc_prompt
* support for Linux ppc64le on 64-bit Power processors
* streamlined teradatasql package description to avoid Azure DevOps artifact metadata limit

`20.0.0.27` - April 1, 2025
* GOSQL-207 OIDC token cache for improved Browser Authentication UX

`20.0.0.26` - March 17, 2025
* Vector data type support for FastLoad
* Build DLL and shared library with standard Go 1.24.1
* Environment variable GODEBUG=fips140=on directs the Go Cryptographic Module to operate in FIPS 140-3 mode, default is off
* No longer uses OpenSSL on Linux, to avoid panic: opensslcrypto: FIPS mode requested (system FIPS mode) but not available in OpenSSL
* client attribute ClientSecProdGrp no longer indicates OpenSSL library on Linux
* Switch to golang.org/x/crypto version 0.36.0

`20.0.0.25` - February 25, 2025
* FIPS support
* proxy server support for FastLoad and FastExport
* GOSQL-182 transmit additional Client Attributes
* client attribute ClientSecProdGrp also indicates OpenSSL library on Linux
* Build DLL and shared library with Microsoft Go 1.24 using build tag goexperiment.systemcrypto for FIPS support
* Requires macOS 12.4 Monterey or later and ends support for older versions of macOS
* Requires Linux kernel version 3.2 or later and ends support for older versions of Linux

`20.0.0.24` - February 3, 2025
* default Linux Kerberos libraries /usr/lib64/libgssapi_krb5.so and /usr/lib64/libgssapi_krb5.so.2

`20.0.0.23` - January 27, 2025
* client attribute ClientSecProdGrp indicates Go crypto library version
* Build DLL and shared library with Go 1.23.5
* Build DLL and shared library with golang.org/x/crypto v0.32.0
* Requires macOS 11 Big Sur or later and ends support for older versions of macOS

`20.0.0.22` - January 6, 2025
* Debug logging for Kerberos library dynamic loading and linking

`20.0.0.21` - December 12, 2024
* Provide driver version number and session number in Teradata Security exceptions
* Add commands to teradatasql module command line interface
* Add connection method `.nativeSQL`

`20.0.0.20` - October 25, 2024
* GOSQL-212 handle Microsoft Entra OIDC Authorization Code Response redirect error parameters
* Add escape function `{fn teradata_provide(dhke)}`
* Improve teradatasql module command line interface

`20.0.0.19` - October 11, 2024
* GOSQL-211 enable logon to database without DHKE bypass after logon to database having DHKE bypass
* Add escape function `{fn teradata_connected}`
* Add teradatasql module `__version__` attribute
* Add teradatasql module command line interface
* Add cursor attribute `columntypename`

`20.0.0.18` - October 7, 2024
* Omit port suffix from HTTP Host: header when using default port 80 for HTTP or 443 for HTTPS
* Build DLL and shared library with Go 1.22.4 (downgrade) to avoid [Go 1.22.5 performance regression issue #68587](https://github.com/golang/go/issues/68587)

`20.0.0.17` - October 1, 2024
* GOSQL-196 Go TeraGSS logmech=JWT bypass DHKE for HTTPS connections
* GOSQL-210 provide Server Name Indication (SNI) field in the TLS client hello
* Build macOS shared library with golang-fips go1.22.5-3-openssl-fips

`20.0.0.16` - September 27, 2024
* GOSQL-177 asynchronous request support
* GOSQL-178 Go TeraGSS logmech=TD2 bypass DHKE for HTTPS connections

`20.0.0.15` - July 31, 2024
* GOSQL-205 Stored Password Protection for http(s)_proxy_password connection parameters
* GOSQL-206 CRC client attribute
* Build DLL and shared library with Go 1.22.5

`20.0.0.14` - July 26, 2024
* GOSQL-203 Go module
* Build DLL and shared library with Go 1.21.9
* Requires macOS 10.15 Catalina or later and ends support for older versions of macOS

`20.0.0.13` - June 24, 2024
* GOSQL-198 oidc_sslmode connection parameter
* GOSQL-199 sslcrc=ALLOW and PREFER soft fail CRC for VERIFY-CA and VERIFY-FULL
* GOSQL-200 sslcrc=REQUIRE requires CRC for VERIFY-CA and VERIFY-FULL

`20.0.0.12` - April 30, 2024
* GOSQL-31 Monitor partition

`20.0.0.11` - April 25, 2024
* GOSQL-193 Device Code Flow and Client Credentials Flow

`20.0.0.10` - April 10, 2024
* GOSQL-185 Use FIPS-140 Compliant Modules
* Build DLL and shared library with Go 1.20.14
* Build DLL and shared library with Microsoft Go for Windows, Linux Intel, Linux ARM
* Build shared library with golang-fips for macOS Intel, macOS ARM

`20.0.0.9` - April 2, 2024
* Include teradatasql.arm.so in package

`20.0.0.8` - March 18, 2024
* GOSQL-121 Linux ARM support
* GOSQL-184 remove DES and DESede
* PYDBAPI-124 remove DES and DESede
* PYDBAPI-131 cursor attributes activitytype and activityname

`20.0.0.7` - February 1, 2024
* GOSQL-189 improved error messages for missing or invalid logmech value
* GOSQL-190 Go TeraGSS accommodate DH/CI bypass flag in JWT token header

`20.0.0.6` - January 19, 2024
* GOSQL-183 TLS certificate verification for Identity Provider endpoints

`20.0.0.5` - January 17, 2024
* GOSQL-151 proxy server support

`20.0.0.4` - January 9, 2024
* Build DLL and shared library with Go 1.20.12

`20.0.0.2` - December 8, 2023
* Improved exception message for query timeout
* New sample programs CancelSleep.py and MultiThread.py

`20.0.0.1` - November 16, 2023
* Build DLL and shared library with Go 1.20.11

`20.0.0.0` - November 7, 2023
* TDGSS-7022 Go TeraGSS Phase 1
* TDGSS-7232 Go TeraGSS Phase 2
* TDGSS-7233 Go TeraGSS Phase 3
* TDGSS-8123 Integrate Go TeraGSS with the GoSQL Driver phase 1
* TDGSS-8345 Go TeraGSS Phase 4
* TDGSS-9050 Integrate Go TeraGSS with the GoSQL Driver phase 2
* GOSQL-148 TDNEGO logon mechanism for Go TeraGSS
* GOSQL-158 switch to Go TeraGSS
* GOSQL-181 improve TDNEGO interoperability with Kerberos

`17.20.0.32` - October 23, 2023
* GOSQL-179 fake result sets add SPParameterDirection to ColumnMetadata and ParameterMetadata
* GOSQL-180 fake result sets add stored procedure IN parameters to ParameterMetadata

`17.20.0.31` - September 27, 2023
* GOSQL-176 better error message for missing host connection parameter

`17.20.0.30` - September 19, 2023
* GOSQL-175 avoid panic: cannot create context from nil parent
* PYDBAPI-122 provide py.typed file
* PYDBAPI-123 autocommit property for TeradataConnection

`17.20.0.29` - September 5, 2023
* Build DLL and shared library with Go 1.19.12
* Requires 64-bit Python 3.7 or later and ends support for older versions of Python
* Added sample program InsertLob.py

`17.20.0.28` - July 21, 2023
* Build DLL and shared library with Go 1.19.11
* UTC match values for sample program `TJEncryptPassword.py`

`17.20.0.27` - June 23, 2023
* Additional changes for GOSQL-128 use OIDC scope from Gateway Config parcel

`17.20.0.26` - June 15, 2023
* GOSQL-165 Auto-Generated Key Retrieval (AGKR)
* GOSQL-167 use loopback IP address for OIDC redirect

`17.20.0.25` - June 2, 2023
* GOSQL-142 sp_spl connection parameter
* fake result set columns StatementNumber and WarningCode are now INTEGER

`17.20.0.24` - May 23, 2023
* GOSQL-41 escape function teradata_provide(request_scope_column_name_off)
* GOSQL-124 runstartup connection parameter

`17.20.0.23` - May 19, 2023
* GOSQL-157 logon_timeout connection parameter

`17.20.0.22` - May 16, 2023
* Build DLL and shared library with Go 1.19.9

`17.20.0.21` - May 15, 2023
* GOSQL-128 use OIDC scope from Gateway Config parcel

`17.20.0.20` - May 5, 2023
* GOSQL-155 teradata_provide(gateway_config) teradata_provide(governed) teradata_provide(uses_check_workload)

`17.20.0.19` - March 30, 2023
* GOSQL-129 TLS certificate revocation checking with CRL
* GOSQL-130 TLS certificate revocation checking with OCSP (not OCSP stapling)
* GOSQL-132 sslcrc connection parameter

`17.20.0.18` - March 27, 2023
* GOSQL-146 FastLoad and FastExport Unicode Pass Through support

`17.20.0.17` - March 24, 2023
* Build DLL and shared library with Go 1.19.7
* GOSQL-136 escape functions teradata_manage_error_tables_off and teradata_manage_error_tables_on
* GOSQL-139 allow alternate LOCATOR(type) syntax for teradata_parameter escape function
* GOSQL-145 connection parameters error_query_count, error_query_interval, error_table_1_suffix, error_table_2_suffix, error_table_database, manage_error_tables, sessions

`17.20.0.16` - February 21, 2023
* GOSQL-138 avoid panic for aborted session

`17.20.0.15` - February 16, 2023
* GOSQL-137 limit the max number of records in a CSV batch

`17.20.0.14` - January 19, 2023
* GOSQL-24 Asynchronous abort SQL request execution
* GOSQL-134 escape function teradata_request_timeout
* GOSQL-135 connection parameter request_timeout
* PYDBAPI-114 Connection.cancel method to cancel executing SQL request

`17.20.0.13` - January 17, 2023
* GOSQL-133 return FastLoad errors for FastLoad with teradata_read_csv

`17.20.0.12` - December 2, 2022
* Build DLL and shared library with Go 1.19.3
* GOSQL-126 escape functions teradata_values_off and teradata_values_on

`17.20.0.11` - November 1, 2022
* GOSQL-125 FastLoad FastExport govern support for fake_result_sets=true
* GOSQL-127 substitute dash for unavailable program name in Client Attributes

`17.20.0.10` - October 27, 2022
* GOSQL-67 FastLoad FastExport workload management
* GOSQL-120 govern connection parameter
* GOSQL-123 conditional use of Statement Independence depending on database setting

`17.20.0.9` - October 25, 2022
* Build DLL and shared library with Go 1.18.7

`17.20.0.8` - October 19, 2022
* GOSQL-122 case-insensitive VERIFY-FULL

`17.20.0.7` - September 27, 2022
* Avoid Kerberos logon failure

`17.20.0.6` - September 19, 2022
* Build DLL and shared library with Go 1.18.6

`17.20.0.5` - September 15, 2022
* Additional changes for GOSQL-119 avoid nil pointer dereference for FastExport CSV error

`17.20.0.4` - September 14, 2022
* GOSQL-87 support Mac ARM without Rosetta
* GOSQL-119 avoid nil pointer dereference for FastExport CSV error

`17.20.0.3` - September 6, 2022
* GOSQL-118 teradata_write_csv support for queries containing commas

`17.20.0.2` - August 23, 2022
* GOSQL-117 browser_tab_timeout connection parameter

`17.20.0.1` - August 11, 2022
* Build DLL and shared library with Go 1.18.5

`17.20.0.0` - June 16, 2022
* GOSQL-74 FastLoad support for connection parameter fake_result_sets=true

`17.10.0.16` - June 6, 2022
* GOSQL-106 indicate unavailable TLS certificate status with ClientAttributesEx CERT=U

`17.10.0.15` - June 2, 2022
* Switch to TeraGSS 17.20.00.04 and OpenSSL 1.1.1l
* Requires macOS 10.14 Mojave or later and ends support for older versions of macOS

`17.10.0.14` - May 18, 2022
* GOSQL-104 FastExport reports invalid CSV path name for first query but not subsequent
* GOSQL-105 Avoid driver failure when database warning length is invalid

`17.10.0.13` - May 16, 2022
* GOSQL-53 browser and logmech=BROWSER connection parameters
* GOSQL-56 Implement Federated Authentication feature in GoSQL Driver
* PYDBAPI-77 Implement Federated Authentication feature in Python driver

`17.10.0.12` - April 15, 2022
* GOSQL-71 TLS certificate verification
* GOSQL-98 remove escape function teradata_setloglevel

`17.10.0.11` - April 7, 2022
* GOSQL-82 Escape functions teradata_field_sep and teradata_field_quote
* GOSQL-97 FastLoad/FastExport accommodate extra whitespace in SQL request

`17.10.0.10` - March 24, 2022
* GOSQL-95 case-insensitive sslmode connection parameter values
* GOSQL-96 avoid CVE security vulnerabilities present in Go 1.17 and earlier
* Build DLL and shared library with Go 1.18
* Requires macOS 10.13 High Sierra or later and ends support for older versions of macOS

`17.10.0.9` - March 18, 2022
* GOSQL-94 thread-safe connect failure cache

`17.10.0.8` - March 9, 2022
* GOSQL-84 accommodate 64-bit Activity Count
* GOSQL-92 FastLoad returns error 512 when first column value is NULL

`17.10.0.7` - February 23, 2022
* GOSQL-91 Avoid Error 8019 by always sending Config Request message

`17.10.0.6` - February 4, 2022
* GOSQL-26 provide stored procedure creation errors
* GOSQL-73 Write CSV files
* GOSQL-88 Append streamlined client call stack to ClientProgramName

`17.10.0.5` - January 10, 2022
* GOSQL-86 provide UDF compilation errors

`17.10.0.4` - December 13, 2021
* GOSQL-20 TLS support
* GOSQL-29 Laddered Concurrent Connect
* PYDBAPI-82 Implement Laddered Concurrent Connect in Python driver

`17.10.0.3` - November 30, 2021
* GOSQL-12 Centralized administration for data encryption
* GOSQL-25 Assign Response message error handling
* GOSQL-27 Enhance checks for missing logon parameters
* GOSQL-65 improve terasso error messages
* GOSQL-66 transmit Client Attributes to DBS during logon
* PYDBAPI-58 Centralized administration (from database) of Data Encryption
* Build DLL and shared library with Go 1.15.15

`17.10.0.2` - July 2, 2021
* GOSQL-33 CALL to stored procedure INOUT and OUT parameter output values
* GOSQL-35 Statement Independence
* GOSQL-72 Read CSV files
* PYDBAPI-39 JSON, CSV, and Avro data type support
* PYDBAPI-83 Escape Syntax for FLOAT Data Type

`17.10.0.1` - June 9, 2021
* Corrected documentation formatting for PyPI

`17.10.0.0` - June 8, 2021
* GOSQL-75 trim whitespace from SQL request text

`17.0.0.8` - December 18, 2020
* Documentation changes

`17.0.0.7` - December 18, 2020
* GOSQL-13 add support for FastExport protocol

`17.0.0.6` - October 9, 2020
* GOSQL-68 cross-process COP hostname load distribution

`17.0.0.5` - August 26, 2020
* GOSQL-64 improve error checking for FastLoad escape functions

`17.0.0.4` - August 18, 2020
* GOSQL-62 prevent nativesql from executing FastLoad
* GOSQL-63 prevent FastLoad panic

`17.0.0.3` - July 30, 2020
* Build DLL and shared library with Go 1.14.6

`17.0.0.2` - June 10, 2020
* GOSQL-60 CLOBTranslate=Locked workaround for DBS DR 194293

`17.0.0.1` - June 4, 2020
* GOSQL-61 FastLoad accommodate encryptdata true

`16.20.0.62` - May 12, 2020
* GOSQL-58 support multiple files for Elicit File protocol
* GOSQL-59 FastLoad accommodate dbscontrol change of COUNT(*) return type

`16.20.0.61` - Apr 30, 2020
* GOSQL-57 Deferred LOB values larger than 1MB

`16.20.0.60` - Mar 27, 2020
* GOSQL-22 enable insert of large LOB values over 64KB
* GOSQL-52 teradata_try_fastload consider bind value data types
* GOSQL-54 enforce Decimal value maximum precision 38
* PYDBAPI-37 Teradata Data Types Support up to 14.10 including LOB data

`16.20.0.59` - Jan 8, 2020
* GOSQL-51 FastLoad fails when table is dropped and recreated
* PYDBAPI-72 bind value performance improvement
* PYDBAPI-73 DBAPI fails to insert 16383 rows

`16.20.0.58` - Dec 11, 2019
* PYDBAPI-71 execute and executemany ignoreErrors parameter

`16.20.0.57` - Dec 10, 2019
* GOSQL-50 provide FastLoad duplicate row errors with auto-commit on

`16.20.0.56` - Dec 4, 2019
* PYDBAPI-70 raise error for closed cursor usage

`16.20.0.55` - Nov 26, 2019
* GOSQL-15 add database connection parameter
* PYDBAPI-66 Better exception when running on 32-bit Python

`16.20.0.54` - Nov 21, 2019
* GOSQL-49 FastLoad support for additional connection parameters

`16.20.0.53` - Nov 15, 2019
* GOSQL-36 segment and iterate parameter batches per batch row limit
* GOSQL-43 segment and iterate parameter batches per request message size limit for FastLoad

`16.20.0.52` - Oct 18, 2019
* Sample programs for fake result sets

`16.20.0.51` - Oct 16, 2019
* GOSQL-46 LDAP password special characters

`16.20.0.50` - Oct 7, 2019
* PYDBAPI-68 improve performance for batch bind values

`16.20.0.49` - Oct 3, 2019
* GOSQL-45 FastLoad interop with Stored Password Protection

`16.20.0.48` - Sep 6, 2019
* GOSQL-14 add support for FastLoad protocol
* GOSQL-34 negative scale for Number values
* PYDBAPI-29 Data Transfer - FastLoad Protocol

`16.20.0.47` - Aug 27, 2019
* GOSQL-40 Skip executing empty SQL request text
* PYDBAPI-67 teradatasql.connect JSON connection string optional

`16.20.0.46` - Aug 16, 2019
* GOSQL-39 COP Discovery interop with Kerberos

`16.20.0.45` - Aug 12, 2019
* GOSQL-38 timestamp prefix log messages

`16.20.0.44` - Aug 7, 2019
* GOSQL-4 Support COP discovery
* PYDBAPI-36 COP Discovery

`16.20.0.43` - Jul 29, 2019
* GOSQL-18 Auto-commit
* PYDBAPI-61 commit and rollback methods

`16.20.0.42` - Jun 7, 2019
* PYDBAPI-65 sample program `BatchInsert.py`

`16.20.0.41` - Feb 14, 2019
* PYDBAPI-57 fetchmany may return "rows are closed" instead of empty result set

`16.20.0.40` - Feb 8, 2019
* GOSQL-11 JWT authentication method
* GOSQL-16 tmode connection parameter
* GOSQL-17 commit and rollback functions

`16.20.0.39` - Oct 26, 2018
* GOSQL-33 CALL to stored procedure INOUT and OUT parameter output values

`16.20.0.38` - Oct 25, 2018
* PYDBAPI-56 Stored Procedure Dynamic Result Sets

`16.20.0.37` - Oct 22, 2018
* Documentation change

`16.20.0.36` - Oct 22, 2018
* GOSQL-5 Create/Replace Procedure MultiTSR protocol

`16.20.0.35` - Oct 22, 2018
* GOSQL-10 Stored Password Protection
* PYDBAPI-28 Secure Password at rest
* PYDBAPI-47 Port sample program TJEncryptPassword to Python

`16.20.0.34` - Oct 15, 2018
* Fix for sample program `TJEncryptPassword.py`

`16.20.0.33` - Oct 12, 2018
* Installation dependency pycryptodome

`16.20.0.32` - Sep 19, 2018
* Sample programs `LoadCSVFile.py` and `MetadataFromPrepare.py`
* Escape function teradata_fake_result_sets

`16.20.0.31` - Sep 19, 2018
* Added function tracing

`16.20.0.30` - Sep 14, 2018
* PYDBAPI-12 Connectivity
* PYDBAPI-33 Pandas library Interoperability
* Moved samples directory

`16.20.0.29` - Sep 14, 2018
* Sample program `ElicitFile.py`

`16.20.0.28` - Sep 13, 2018
* Documentation change

`16.20.0.27` - Sep 12, 2018
* Documentation change

`16.20.0.26` - Sep 11, 2018
* PYDBAPI-8 Documentation
* PYDBAPI-9 User Guide Content

`16.20.0.25` - Sep 10, 2018
* Documentation change

`16.20.0.24` - Sep 6, 2018
* PYDBAPI-54 Implement cursor rowcount attribute
* PYDBAPI-55 Improved support for Python data types

`16.20.0.23` - Aug 31, 2018
* KeepResponse only for LOB locators

`16.20.0.22` - Aug 30, 2018
* Fixed NUMBER values

`16.20.0.21` - Aug 29, 2018
* Close orphaned rows

`16.20.0.20` - Aug 28, 2018
* decimal and datetime values

`16.20.0.19` - Aug 22, 2018
* timedelta bind values

`16.20.0.18` - Aug 21, 2018
* datetime.datetime bind values

`16.20.0.17` - Aug 20, 2018
* Version number in errors

`16.20.0.16` - Aug 17, 2018
* SLES 11 SP1 compatibility

`16.20.0.15` - Aug 17, 2018
* Documentation change

`16.20.0.14` - Aug 10, 2018
* Documentation change

`16.20.0.13` - Aug 9, 2018
* Documentation change

`16.20.0.12` - Aug 9, 2018
* PYDBAPI-10 User Guide Delivery and Viewability
* PYDBAPI-11 Searchability

`16.20.0.11` - Aug 8, 2018
* Documentation change

`16.20.0.10` - Aug 8, 2018
* Documentation change

`16.20.0.9` - Aug 7, 2018
* Install documentation in teradatasql directory

`16.20.0.8` - Aug 7, 2018
* GOSQL-7 TDNEGO authentication method
* PYDBAPI-42 Teradata Logon mechanism - TDNEGO

`16.20.0.7` - Jul 30, 2018
* GOSQL-8 Support parameter marker batch insert
* PYDBAPI-45 Parameterized Batch Insertion using executeMany

`16.20.0.6` - Jul 25, 2018
* Thread safety for handle maps

`16.20.0.5` - Jul 25, 2018
* Removed atexit

`16.20.0.4` - Jul 23, 2018
* PYDBAPI-4 Provide Python Driver license file

`16.20.0.3` - Jul 19, 2018
* PYDBAPI-46 Accept subclasses of bytes, int, float, str as bind values

`16.20.0.2` - Jul 19, 2018
* Package attributes change

`16.20.0.1` - Jul 18, 2018
* Version number change

`16.20.0.0` - Jul 18, 2018
* GOSQL-1 Encrypted logon
* GOSQL-2 LDAP and Kerberos authentication
* GOSQL-3 Support for 1MB Rows
* GOSQL-6 Elicit File protocol
* PYDBAPI-1 Distribution
* PYDBAPI-5 cursor.execute method return cursor
* PYDBAPI-6 Install and Deployment
* PYDBAPI-7 pip install of python driver package
* PYDBAPI-13 Operating System Platforms
* PYDBAPI-14 Driver must be available for use by Windows OS Users
* PYDBAPI-15 Driver must be available for use by OSX (Mac) Users
* PYDBAPI-16 Driver must be available for use by Linux OS Users
* PYDBAPI-17 Python Language version
* PYDBAPI-18 Python language version 3.4
* PYDBAPI-19 Distribution
* PYDBAPI-23 Teradata Analytics Platform Interoperability/Support
* PYDBAPI-24 Works with Teradata Database 16.10, 16.20
* PYDBAPI-26 Teradata Logon mechanism - Kerberos
* PYDBAPI-32 Downloadable from pypi.org
* PYDBAPI-40 Teradata Logon mechanism - LDAP
* PYDBAPI-41 Teradata Logon mechanism - TD2
* PYDBAPI-43 parameterized single-row inserts
* PYDBAPI-44 parameterized queries
