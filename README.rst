ArUcoPatternMaker
===============================

.. image:: https://github.com/SciKit-Surgery/ArUcoPatternMaker/raw/master/project-icon.png
   :height: 128px
   :width: 128px
   :target: https://github.com/SciKit-Surgery/ArUcoPatternMaker
   :alt: Logo

|

.. image:: https://github.com/SciKit-Surgery/ArUcoPatternMaker/badges/master/build.svg
   :target: https://github.com/SciKit-Surgery/ArUcoPatternMaker/pipelines
   :alt: GitLab-CI test status

.. image:: https://github.com/SciKit-Surgery/ArUcoPatternMaker/badges/master/coverage.svg
    :target: https://github.com/SciKit-Surgery/ArUcoPatternMaker/commits/master
    :alt: Test coverage

.. image:: https://readthedocs.org/projects/ArUcoPatternMaker/badge/?version=latest
    :target: http://ArUcoPatternMaker.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg
   :target: CODE_OF_CONDUCT.md

.. image:: https://img.shields.io/twitter/follow/scikit_surgery?style=social
   :target: https://twitter.com/scikit_surgery?ref_src=twsrc%5Etfw
   :alt: Follow scikit_surgery on twitter


Author: Stephen Thompson

ArUcoPatternMaker is part of the `SciKit-Surgery`_ software project, developed at the `Wellcome EPSRC Centre for Interventional and Surgical Sciences`_, part of `University College London (UCL)`_.

AruCoPatternMaker seems to be derived from `arucomarker.py`_

ArUcoPatternMaker supports Python 2.7 and Python 3.6.

    python arucopatternmaker.py
    python arucopatternmaker.py


Developing
----------

Cloning
^^^^^^^

You can clone the repository using the following command:

::

    git clone https://github.com/SciKit-Surgery/ArUcoPatternMaker


Running tests
^^^^^^^^^^^^^
Pytest is used for running unit tests:
::

    pip install pytest
    python -m pytest


Linting
^^^^^^^

This code conforms to the PEP8 standard. Pylint can be used to analyse the code:

::

    pip install pylint
    pylint --rcfile=tests/pylintrc arucopatternmaker


Installing
----------

You can pip install directly from the repository as follows:

::

    pip install git+https://github.com/SciKit-Surgery/ArUcoPatternMaker



Contributing
^^^^^^^^^^^^

Please see the `contributing guidelines`_.


Useful links
^^^^^^^^^^^^

* `Source code repository`_
* `Documentation`_


Licensing and copyright
-----------------------

Copyright 2020 University College London.
ArUcoPatternMaker is released under the BSD-3 license. Please see the `license file`_ for details.


Acknowledgements
----------------

Supported by `Wellcome`_ and `EPSRC`_.


.. _`Wellcome EPSRC Centre for Interventional and Surgical Sciences`: http://www.ucl.ac.uk/weiss
.. _`source code repository`: https://github.com/SciKit-Surgery/ArUcoPatternMaker
.. _`Documentation`: https://ArUcoPatternMaker.readthedocs.io
.. _`SciKit-Surgery`:  https://github.com/SciKit-Surgery
.. _`University College London (UCL)`: http://www.ucl.ac.uk/
.. _`Wellcome`: https://wellcome.ac.uk/
.. _`EPSRC`: https://www.epsrc.ac.uk/
.. _`contributing guidelines`: https://github.com/SciKit-Surgery/ArUcoPatternMaker/blob/master/CONTRIBUTING.rst
.. _`license file`: https://github.com/SciKit-Surgery/ArUcoPatternMaker/blob/master/LICENSE
.. _`arucomarker.py`: https://gist.github.com/eruffaldi/1e95c5fef80c0feda105
