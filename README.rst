Introduction
============


.. image:: https://readthedocs.org/projects/micropython-bmi160/badge/?version=latest
    :target: https://micropython-bmi160.readthedocs.io/en/latest/
    :alt: Documentation Status


.. image:: https://img.shields.io/pypi/v/micropython-bmi160.svg
    :alt: latest version on PyPI
    :target: https://pypi.python.org/pypi/micropython-bmi160

.. image:: https://static.pepy.tech/personalized-badge/micropython-bmi160?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Pypi%20Downloads
    :alt: Total PyPI downloads
    :target: https://pepy.tech/project/micropython-bmi160

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

MicroPython Driver for the Bosch BMI160 Acc/Gyro Sensor



Installing from PyPI
=====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/micropython-bmi160/>`_.
To install for current user:

.. code-block:: shell

    pip3 install micropython-bmi160

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install micropython-bmi160

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .venv
    source .env/bin/activate
    pip3 install micropython-bmi160


Usage Example
=============

Take a look at the examples directory

Documentation
=============
API documentation for this library can be found on `Read the Docs <https://micropython-bmi160.readthedocs.io/en/latest/>`_.

