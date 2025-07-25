### Session Reconnect

Your application's connection can be disconnected from the database session in various ways outside the control of the driver, such as
* a network cable being unplugged
* a network communication failure
* an administrator terminating the session with the Monitor partition command `Abort Session`
* an administrator terminating the session with the Gateway command `Kill Session`
* a database restart

When Session Reconnect is enabled, the driver will attempt to reconnect the connection to the database session after a communication failure.

Session Reconnect is enabled when one or more of the following conditions are satisfied:
* Recoverable Network Protocol is in effect
* and/or connection parameter `reconnect_count` is specified (if omitted, the default is 11 attempts)
* and/or connection parameter `reconnect_interval` is specified (if omitted, the default is 30 seconds)

| Maximum possible elapsed time for reconnect attempts
| ---
| (*ReconnectCount* - 1) &times; *ReconnectInterval*

Recoverable Network Protocol (RNP) and Redrive are enabled through a combination of database and driver connection parameters; specifically, the database `dbscontrol` fields `RedriveProtection` (67), `RedriveDefaultParticipation` (68), and `DisableRecoverableNetProtocol` (77), and the driver connection parameter `redrive` with level 2 or higher.
* When RNP and Redrive are enabled, then Session Reconnect works for a variety of failure events, including transient network failures.
* Without Recoverable Network Protocol, Session Reconnect only supports reconnection after a database restart; it does not support reconnection after other events, such as transient network failures.

Session Reconnect | RNP and Redrive | Communication failure handling
----------------- | --------------- | ---
Disabled          | Disabled        | The operation in progress fails, the driver closes the connection and returns an error to the application.
Enabled           | Disabled        | The operation in progress fails, the driver attempts to reconnect and returns an error to the application.<br/>If the reconnect is unsuccessful, the driver closes the connection.<br/>If the reconnect is successful, the database discards a significant part of the session state:<br/>&bull; The current transaction is rolled back.<br/>&bull; All open result sets are discarded.<br/>&bull; All volatile tables are discarded.<br/>&bull; All materialized global temp tables are discarded.<br/>The application must be prepared to accommodate the possible loss of session state at any point in time.
Enabled           | Enabled         | The operation in progress fails and the driver attempts to reconnect.<br/>If the reconnect is unsuccessful, the driver closes the connection.<br/>If the reconnect is successful, the operation is redriven automatically, the session's state is preserved, and no error is returned to the application.

Reconnect is never attempted if a communication failure occurs while the application is closing the connection.

The database enforces a limited time period for reconnecting to a session after a database restart. The amount of time is set using the database administrator program `gtwcontrol`. The standard value is 20 minutes. The database will reject all reconnect attempts after the time period expires.

<a id="TransactionMode"></a>

