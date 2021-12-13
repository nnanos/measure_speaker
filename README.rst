========
Overview
========

An application that measures the Impulse\Frequency Responce 
of your speakers with Python (like REW) . 
It was a an attempt to confirm what the REW is doing under the scenes .

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/measure_speaker/badge/?style=flat
    :target: https://measure_speaker.readthedocs.io/
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.com/nnanos/measure_speaker.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.com/github/nnanos/measure_speaker

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/nnanos/measure_speaker?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/nnanos/measure_speaker

.. |requires| image:: https://requires.io/github/nnanos/measure_speaker/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/nnanos/measure_speaker/requirements/?branch=master

.. |codecov| image:: https://codecov.io/gh/nnanos/measure_speaker/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/nnanos/measure_speaker

.. |version| image:: https://img.shields.io/pypi/v/measure-speaker.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/measure-speaker

.. |wheel| image:: https://img.shields.io/pypi/wheel/measure-speaker.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/measure-speaker

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/measure-speaker.svg
    :alt: Supported versions
    :target: https://pypi.org/project/measure-speaker

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/measure-speaker.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/measure-speaker

.. |commits-since| image:: https://img.shields.io/github/commits-since/nnanos/measure_speaker/v0.0.1.svg
    :alt: Commits since latest release
    :target: https://github.com/nnanos/measure_speaker/compare/v0.0.1...master



.. end-badges



* Free software: MIT license

Installation
============

::

    pip install measure-speaker

You can also install the in-development version with::

    pip install https://github.com/nnanos/measure_speaker/archive/master.zip


Documentation
=============


https://measure_speaker.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
