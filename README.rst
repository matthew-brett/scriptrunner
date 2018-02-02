#######################################################
Scriptrunner - utility for testing command line scripts
#######################################################

.. shared-text-body

**********
Quickstart
**********

See the tests for examples of using Scriptrunner for testing builds of Sphinx
projects.

************
Installation
************

::

    pip install scriptrunner

****
Code
****

See https://github.com/matthew-brett/scriptrunner

Released under the BSD two-clause license - see the file ``LICENSE`` in the
source distribution.

`travis-ci <https://travis-ci.org/matthew-brett/scriptrunner>`_ kindly tests
the code automatically under Python versions 2.7, and 3.3 through 3.6.

The latest released version is at https://pypi.python.org/pypi/scriptrunner

*****
Tests
*****

* Install ``scriptrunner``
* Install the pytest_ testing framework::

    pip install pytest

* Run the tests with::

    py.test --pyargs scriptrunner

*******
Support
*******

Please put up issues on the `scriptrunner issue tracker`_.

.. standalone-references

.. |scriptrunner-documentation| replace:: `scriptrunner documentation`_
.. _scriptrunner documentation:
    https://matthew-brett.github.com/scriptrunner/scriptrunner.html
.. _documentation: https://matthew-brett.github.com/scriptrunner
.. _pandoc: http://pandoc.org
.. _jupyter: jupyter.org
.. _homebrew: brew.sh
.. _sphinx: http://sphinx-doc.org
.. _rest: http://docutils.sourceforge.net/rst.html
.. _scriptrunner issue tracker: https://github.com/matthew-brett/scriptrunner/issues
.. _pytest: https://pytest.readthedocs.io
.. _mock: https://github.com/testing-cabal/mock
