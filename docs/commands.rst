Commands
========

Glot has a number of commands that allow it to act as a complete
client for Glossia. These should be included as described in
`Usage <usage.html>`_, bearing in mind that global arguments, preceding the
command, may or may not modify behaviour
(e.g. ``--to`` is relevant only for commands retrieving files
from the Glossia server).

The most commonly used commands are likely to be:

-  ``glot table``
-  ``glot results -i UUID`` (successful simulations)
-  ``glot diagnostic -i UUID`` (failed simulations)
-  | ``glot diagnostic -d UUID`` (on remote host)
   | Transfer ``UUID-results.tgz`` to local machine
   | ``glot inspect UUID-results.tgz`` (local machine)

In general, UUIDs may be given only as the first few characters,
provided that this specifies them uniquely on the server.

Search
------

Search UUID or UUIDs matching a given prefix. Prints a table
showing most recent status of matching simulations on the
Glossia server.

.. code-block:: bash

    glot search [--limit LIMIT] [--server-limit SERVERLIMIT]
        [--sort SORT] [GUID]

+------------------------------------+----------------------------------------------------------+
| Argument / Option                  | Description                                              |
+====================================+==========================================================+
| GUID                               | (prefix of or) GUID to search for on server              |
+------------------------------------+----------------------------------------------------------+
| --limit LIMIT                      | maximum number of entries to display (default: 10)       |
+------------------------------------+----------------------------------------------------------+
| --server-limit SERVERLIMIT         | maximum number of entries for the server to retrieve     |
|                                    | from the DB (NB: pre-sorting) (default: 1000)            |
+------------------------------------+----------------------------------------------------------+
| --sort SORT                        | order returned entries by SORT, which may be either      |
|                                    | 'timestamp' or 'guid' (default: timestamp)               |
+------------------------------------+----------------------------------------------------------+

Table
-----

Show a table of simulations. Slightly prettier, more intuitive alternative to using
``glot search`` with no arguments.

.. code-block:: bash

    glot table [--limit LIMIT] [--server-limit SERVERLIMIT] [--sort SORT]

+------------------------------------+----------------------------------------------------------+
| Argument / Option                  | Description                                              |
+====================================+==========================================================+
| --limit LIMIT                      | maximum number of entries to display (default: 10)       |
+------------------------------------+----------------------------------------------------------+
| --server-limit SERVERLIMIT         | maximum number of entries for the server to retrieve     |
|                                    | from the DB (NB: pre-sorting) (default: 1000)            |
+------------------------------------+----------------------------------------------------------+
| --sort SORT                        | order returned entries by SORT, which may be either      |
|                                    | 'timestamp' or 'guid' (default: timestamp)               |
+------------------------------------+----------------------------------------------------------+

Results
-------

Retrieve results of a simulation. Note that this does not retrieve run-time output, which Glossia
has no access to, only output that has been returned from simulation container. For manual
inspection, this is most useful
in conjunction with the ``-i`` or ``-d`` flags, which bundle diagnostic output.

.. code-block:: bash

    glot results [--target TARGET] ([--include-diagnostic/-d] | [--inspect-diagnostic/-i]) GUID

+------------------------------------+----------------------------------------------------------+
| Argument / Option                  | Description                                              |
+====================================+==========================================================+
| GUID                               | (prefix of or) GUID to cancel on server. Must be unique  |
+------------------------------------+----------------------------------------------------------+
| --target TARGET                    | server for Glossia to push output bundles to using HTTP  |
|                                    | POST commands (on port 18103). By default, Glot will     |
|                                    | start an HTTP server and Glossia will look for it on the |
|                                    | network gateway IP                                       |
+------------------------------------+----------------------------------------------------------+
| --include-diagnostic               | combine this command with the ``diagnostic`` command to  |
|                                    | grab both bundles of data                                |
+------------------------------------+----------------------------------------------------------+
| --inspect-diagnostic               | combine this command with the ``diagnostic`` and         |
|                                    | ``inspect`` commands to produce a ready-to-run local     |
|                                    | simulation                                               |
+------------------------------------+----------------------------------------------------------+

Cancel
------

Interrupt a running simulation. Will raise an ``E_CANCELLED`` error on Glossia
(`more information <https://go-smart.github.io/glossia/reference/errors>`_).

.. code-block:: bash

    glot cancel GUID

+------------------------------------+----------------------------------------------------------+
| Argument / Option                  | Description                                              |
+====================================+==========================================================+
| GUID                               | (prefix of or) GUID to cancel on server. Must be unique  |
+------------------------------------+----------------------------------------------------------+

Logs
------

Send container logs (not filesystem logs) from a simulation to the terminal. This corresponds
to *jobs.out* and *jobs.err* in the diagnostic output.

.. code-block:: bash

    glot logs [--stdout] GUID

+------------------------------------+----------------------------------------------------------+
| Argument / Option                  | Description                                              |
+====================================+==========================================================+
| GUID                               | (prefix of or) GUID to cancel on server. Must be unique  |
+------------------------------------+----------------------------------------------------------+
| --stdout                           | request container's STDOUT, not STDERR (default: STDERR) |
+------------------------------------+----------------------------------------------------------+

Status
------

Retrieve status information about a (current or ended) simulation. Particularly useful for
retrieving status or error messages that span multiple lines and cannot be fully displayed
by ``glot search`` or ``glot table``.

.. code-block:: bash

    glot status GUID

+------------------------------------+----------------------------------------------------------+
| Argument / Option                  | Description                                              |
+====================================+==========================================================+
| GUID                               | (prefix of or) GUID to cancel on server. Must be unique  |
+------------------------------------+----------------------------------------------------------+

Diagnostic
----------

Retrieve diagnostic output of a (successful or) failed simulation. This includes log output to
STDERR/STDOUT, any input and any settings files supplied by Glossia to the container. Glossia
stores the UUID of container image used for simulation within the diagnostic data.

.. code-block:: bash

    glot diagnostic [--target TARGET] [--inspect/-i] GUID

+------------------------------------+----------------------------------------------------------+
| Argument / Option                  | Description                                              |
+====================================+==========================================================+
| GUID                               | (prefix of or) GUID to cancel on server. Must be unique  |
+------------------------------------+----------------------------------------------------------+
| --target TARGET                    | server for Glossia to push output bundles to using HTTP  |
|                                    | POST commands (on port 18103). By default, Glot will     |
|                                    | start an HTTP server and Glossia will look for it on the |
|                                    | network gateway IP                                       |
+------------------------------------+----------------------------------------------------------+
| --inspect                          | combine this command with the ``inspect`` command to     |
|                                    | achieve a ready-to-run simulation in the ./UUID/         |
|                                    | directory                                                |
+------------------------------------+----------------------------------------------------------+

Launch
------

Launch a new simulation.

.. code-block:: bash

    glot launch [--tmp-directory TMPDIR] [--input/-i INPUT1 -i INPUT2 ...]
            [--definition/-d DEF1 -d DEF2 ...] GSSAXML

+------------------------------------+----------------------------------------------------------+
| Argument / Option                  | Description                                              |
+====================================+==========================================================+
| GSSAXML                            | A file containing GSSA-XML defining the simulation       |
|                                    | (this is *original.xml* in diagnostic output)            |
+------------------------------------+----------------------------------------------------------+
| --tmp-directory TMPDIR             | directory to use for exchanging files with Glossia       |
|                                    | (default: /tmp)                                          |
+------------------------------------+----------------------------------------------------------+
| --input INPUTN                     | (with multiplicity) files that are referenced with the   |
|                                    | GSSA-XML and are expected in the input/ subfolder of the |
|                                    | simulation directory                                     |
+------------------------------------+----------------------------------------------------------+
| --definition DEFN                  | (with multiplicity) files that constitute the internal   |
|                                    | configuration. This corresponds to the content of the    |
|                                    | numerical model in the Go-Smart CDM framework. For       |
|                                    | instance, a Jinja2 SIF file for Goosefoot or a Python    |
|                                    | script and custom modules for a FEniCS simulation.       |
+------------------------------------+----------------------------------------------------------+

Inspect
-------

Take a diagnostic bundle and prepare it to be run as a new simulation locally (without Glossia,
but using a simulation container). This allows precise reproduction of the remote behaviour
(with certain standard Docker caveats, regarding kernel versions, etc.). To do so, it untars
the diagnostic bundle, and clones a remote repository containing tools to execute the simulation.
For more information on executing standalone simulations, see the individual mode repositories.

Modes:
    - goosefoot
        - https://github.com/go-smart/glossia-container-goosefoot-control
    - fenics (not yet incorporated into glot)
        - https://github.com/go-smart/glossia-container-fenics-control

.. code-block:: bash

    glot inspect [--mode MODE] ARCHIVE

+------------------------------------+----------------------------------------------------------+
| Argument / Option                  | Description                                              |
+====================================+==========================================================+
| ARCHIVE                            | bundle retrieved by ``glot diagnostic``, as TGZ          |
+------------------------------------+----------------------------------------------------------+
| --mode                             | type of setup that should be used (corresponds to a      |
|                                    | tool repository to clone into the diagnostic data).      |
|                                    | At present the only valid mode is 'goosefoot' (default)  |
+------------------------------------+----------------------------------------------------------+
