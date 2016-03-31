Usage
=====

The following assumes a Glossia server is running and connected to
a WAMP router (e.g. Crossbar.io). Unless stated otherwise, it will
be assumed that both are running in containers on the local system,
this being the default setup when using the
`Glossia Quickstart <https://go-smart.github.io/glossia/introduction/quickstart>`_
approach.

Unlike a number of other Glossia tools, which must interact with the
Docker daemon directly, glot should not have superuser access, and should be
run as an unprivileged user.

::

    glot [--server SERVERNAME] [--router ROUTERIP] [--port ROUTERPORT]
        [--to TO] [--force] [--debug] [--verbose] [--color/no-color]
        [--help] COMMAND COMMANDARGS

Positional arguments
~~~~~~~~~~~~~~~~~~~~

+------------+-------------------------------------------------------------+
| Argument   | Description                                                 |
+============+=============================================================+
| COMMAND    | A specific task, perhaps with arguments. See                |
|            | `Commands <commands.html>`_ for details of available        |
|            | commands.                                                   |
+------------+-------------------------------------------------------------+

Optional arguments
~~~~~~~~~~~~~~~~~~

+------------------------------------+----------------------------------------------------------+
| Argument                           | Description                                              |
+====================================+==========================================================+
| -h, --help                         | show this help message and exit                          |
+------------------------------------+----------------------------------------------------------+
| --server SERVERNAME                | target Glossia server on router (default: default)       |
+------------------------------------+----------------------------------------------------------+
| --router ROUTERIP                  | location of the WAMP router (default: localhost)         |
+------------------------------------+----------------------------------------------------------+
| --port ROUTERPORT                  | WebSocket port on router to connect to (default: 8080)   |
+------------------------------------+----------------------------------------------------------+
| --to TO                            | explicit destination directory for output, if applicable |
+------------------------------------+----------------------------------------------------------+
| --force                            | overwrite existing output if necessary                   |
+------------------------------------+----------------------------------------------------------+
| --debug                            | enable additional debug output (mostly technical)        |
+------------------------------------+----------------------------------------------------------+
| --verbose                          | provide additional user-relevant output                  |
+------------------------------------+----------------------------------------------------------+
| --color/no-color                   | use ANSI colours in output, if applicable (default: yes) |
+------------------------------------+----------------------------------------------------------+
