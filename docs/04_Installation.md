### Installation

The `teradatasql` package depends on the `pycryptodome` package which is available from PyPI.

Use `pip install` to download and install the driver and its dependencies automatically.

Platform       | Command
-------------- | ---
macOS or Linux | `pip install teradatasql`
Windows        | `py -3 -m pip install teradatasql`

When upgrading to a new version of the driver, you may need to use pip install's `--no-cache-dir` option to force the download of the new version.

Platform       | Command
-------------- | ---
macOS or Linux | `pip install --no-cache-dir -U teradatasql`
Windows        | `py -3 -m pip install --no-cache-dir -U teradatasql`

The `teradatasql` package depends on the `pycryptodome` package, because one of the included sample programs (`TJEncryptPassword.py`) uses `pycryptodome`. The driver itself does not use `pycryptodome`.

If you want to avoid installing `pycryptodome`, you can use the `--no-deps` option of pip install to avoid installing `pycryptodome`. Without `pycryptodome`, you will not be able to run the `TJEncryptPassword.py` sample program.

Platform       | Command
-------------- | ---
macOS or Linux | `pip install --no-deps teradatasql`
Windows        | `py -3 -m pip install --no-deps teradatasql`

<a id="License"></a>

