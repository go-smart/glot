Installation
============

Source
------

Glot's repository is at https://github.com/go-smart/glot.

Dependencies
------------

- Python3
      - aiohttp
      - Click
      - gitpython
      - tabulate
      - colorama
      - setuptools
- pip3 (for one-line installation)

Note that, if using *pip*, these dependencies should be installed
automatically. They should only be installed separately if you want
to use your operating system's distribution packages, or need specific
versions for compatibility with other tools.

Installation
------------

Directly from the repository (recommended):

.. code-block:: bash

    pip3 install git+git://github.com/go-smart/glot.git@master

From local source:

.. code-block:: bash

    git clone https://github.com/go-smart/glot.git
    cd glot
    python3 setup.py install
