### COP Discovery

The driver provides Communications Processor (COP) discovery behavior when the `cop` connection parameter is `true` or omitted. COP Discovery is turned off when the `cop` connection parameter is `false`.

A database system can be composed of multiple database nodes. One or more of the database nodes can be configured to run the database Gateway process. Each database node that runs the database Gateway process is termed a Communications Processor, or COP. COP Discovery refers to the procedure of identifying all the available COP hostnames and their IP addresses. COP hostnames can be defined in DNS, or can be defined in the client system's `hosts` file. Teradata strongly recommends that COP hostnames be defined in DNS, rather than the client system's `hosts` file. Defining COP hostnames in DNS provides centralized administration, and enables centralized changes to COP hostnames if and when the database is reconfigured.

The `coplast` connection parameter specifies how COP Discovery determines the last COP hostname.
* When `coplast` is `false` or omitted, or COP Discovery is turned off, then the driver will not perform a DNS lookup for the coplast hostname.
* When `coplast` is `true`, and COP Discovery is turned on, then the driver will first perform a DNS lookup for a coplast hostname to obtain the IP address of the last COP hostname before performing COP Discovery. Subsequently, during COP Discovery, the driver will stop searching for COP hostnames when either an unknown COP hostname is encountered, or a COP hostname is encountered whose IP address matches the IP address of the coplast hostname.

Specifying `coplast` as `true` can improve performance with DNS that is slow to respond for DNS lookup failures, and is necessary for DNS that never returns a DNS lookup failure.

When performing COP Discovery, the driver starts with cop1, which is appended to the database hostname, and then proceeds with cop2, cop3, ..., copN. The driver supports domain-name qualification for COP Discovery and the coplast hostname. Domain-name qualification is recommended, because it can improve performance by avoiding unnecessary DNS lookups for DNS search suffixes.

The following table illustrates the DNS lookups performed for a hypothetical three-node database system named "whomooz".

&nbsp; | No domain name qualification | With domain name qualification<br/>(Recommended)
------ | ---------------------------- | ---
Application-specified<br/>database hostname | `whomooz` | `whomooz.domain.com`
Default: COP Discovery turned on, and `coplast` is `false` or omitted,<br/>perform DNS lookups until unknown COP hostname is encountered | `whomoozcop1`&rarr;`10.0.0.1`<br/>`whomoozcop2`&rarr;`10.0.0.2`<br/>`whomoozcop3`&rarr;`10.0.0.3`<br/>`whomoozcop4`&rarr;undefined | `whomoozcop1.domain.com`&rarr;`10.0.0.1`<br/>`whomoozcop2.domain.com`&rarr;`10.0.0.2`<br/>`whomoozcop3.domain.com`&rarr;`10.0.0.3`<br/>`whomoozcop4.domain.com`&rarr;undefined
COP Discovery turned on, and `coplast` is `true`,<br/>perform DNS lookups until COP hostname is found whose IP address matches the coplast hostname, or unknown COP hostname is encountered | `whomoozcoplast`&rarr;`10.0.0.3`<br/>`whomoozcop1`&rarr;`10.0.0.1`<br/>`whomoozcop2`&rarr;`10.0.0.2`<br/>`whomoozcop3`&rarr;`10.0.0.3` | `whomoozcoplast.domain.com`&rarr;`10.0.0.3`<br/>`whomoozcop1.domain.com`&rarr;`10.0.0.1`<br/>`whomoozcop2.domain.com`&rarr;`10.0.0.2`<br/>`whomoozcop3.domain.com`&rarr;`10.0.0.3`
COP Discovery turned off and round-robin DNS,<br/>perform one DNS lookup that returns multiple IP addresses | `whomooz`&rarr;`10.0.0.1`, `10.0.0.2`, `10.0.0.3` | `whomooz.domain.com`&rarr;`10.0.0.1`, `10.0.0.2`, `10.0.0.3`

Round-robin DNS rotates the list of IP addresses automatically to provide load distribution. Round-robin is only possible with DNS, not with the client system `hosts` file.

The driver supports the definition of multiple IP addresses for COP hostnames and non-COP hostnames.

For the first connection to a particular database system, the driver generates a random number to index into the list of COPs. For each subsequent connection, the driver increments the saved index until it wraps around to the first position. This behavior provides load distribution across all discovered COPs.

The driver masks connection failures to down COPs, thereby hiding most connection failures from the client application. An exception is thrown to the application only when all the COPs are down for that database. If a COP is down, the next COP in the sequence (including a wrap-around to the first COP) receives extra connections that were originally destined for the down COP. When multiple IP addresses are defined in DNS for a COP, the driver will attempt to connect to each of the COP's IP addresses, and the COP is considered down only when connection attempts fail to all of the COP's IP addresses.

If COP Discovery is turned off, or no COP hostnames are defined in DNS, the driver connects directly to the hostname specified in the `host` connection parameter. This permits load distribution schemes other than the COP Discovery approach. For example, round-robin DNS or a TCP/IP load distribution product can be used. COP Discovery takes precedence over simple database hostname lookup. To use an alternative load distribution scheme, either ensure that no COP hostnames are defined in DNS, or turn off COP Discovery with `cop` as `false`.

<a id="StoredPasswordProtection"></a>

