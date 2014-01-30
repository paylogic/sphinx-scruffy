sphinx-scruffy: Plug-in for Sphinx to render "scruffy" diagrams
===============================================================

Plug-in for Sphinx to render "scruffy" diagrams.

.. image:: https://api.travis-ci.org/paylogic/sphinx-scruffy.png
   :target: https://travis-ci.org/paylogic/sphinx-scruffy
.. image:: https://pypip.in/v/sphinx-scruffy/badge.png
   :target: https://crate.io/packages/sphinx-scruffy/
.. image:: https://coveralls.io/repos/paylogic/sphinx-scruffy/badge.png?branch=master
   :target: https://coveralls.io/r/paylogic/sphinx-scruffy


Installation
------------

.. sourcecode::

    pip install sphinx-scruffy

To use scruffy diagrams you need several external dependencies installed:

- The `Scruffy Python module <https://github.com/aivarsk/scruffy>`_. This module will be installed automatically when
    you use ``pip install sphinx-scruffy``.
- You need ``dot`` (Graphviz), ``rsvg-convert`` (librsvg) and ``pic2plot`` (plotutils).
    You can install all three with one command on Ubuntu: ``sudo apt-get install graphviz librsvg2-bin plotutils``.
- The scruffy font is called Purisa, if you're running Ubuntu you probably have it already but if you don't then
    you can install it using ``sudo apt-get install ttf-thai-tlwg``.


Configuration
-------------

An example of your shpinx's conf.py:

.. code-block:: python

    extensions = ['sphinx_scruffy']


Usage
-----

This section shows a few examples of "scruffy" diagrams done using shpinx-scruffy plugin.

A simple example
****************

The following reStructuredText::

  .. scruffy::

    [User|+Forename;+Surname;+HashedPassword;-Salt|+Login();+Logout()]

Results in this image:

.. scruffy::

  [User|+Forename;+Surname;+HashedPassword;-Salt|+Login();+Logout()]

More complex example
********************

Here's a more complex example::

  .. scruffy::

    [note: You can stick notes on diagrams too!{bg:cornsilk}]
    [Customer]<>1-orders 0..*>[Order]
    [Order]++*->[LineItem]
    [Order]-1>[DeliveryMethod]
    [Order]-*>[Product]
    [Category]<->[Product]
    [DeliveryMethod]^[National]
    [DeliveryMethod]^[International]

This results in the following image:

.. scruffy::

  [note: You can stick notes on diagrams too!{bg:cornsilk}]
  [Customer]<>1-orders 0..*>[Order]
  [Order]++*->[LineItem]
  [Order]-1>[DeliveryMethod]
  [Order]-*>[Product]
  [Category]<->[Product]
  [DeliveryMethod]^[National]
  [DeliveryMethod]^[International]

Class diagram extensions
************************

Here's how to create class diagrams::

  .. scruffy::

    [Node A]->[Node B]
    [Node B]->[Node C]
    [Group [Node A][Node B]]

This results in the following image:

.. scruffy::

  [Node A]->[Node B]
  [Node B]->[Node C]
  [Group [Node A][Node B]]

Sequence diagrams
*****************

Finally there are sequence diagrams::

  .. scruffy::
    :sequence:

    [Patron]order food>[Waiter]
    [Waiter]order food>[Cook]
    [Waiter]serve wine>[Patron]
    [Cook]pickup>[Waiter]
    [Waiter]serve food>[Patron]
    [Patron]pay>[Cashier]

This results in the following image:

.. scruffy::
  :sequence:

  [Patron]order food>[Waiter]
  [Waiter]order food>[Cook]
  [Waiter]serve wine>[Patron]
  [Cook]pickup>[Waiter]
  [Waiter]serve food>[Patron]
  [Patron]pay>[Cashier]


Python3 support
---------------

Package itself supports python3 out of the box, but it's dependency, scruffy package, doesn't yet have a pypi release
with python 3 support.
use git master for now https://github.com/aivarsk/scruffy.git

or via pip::

.. code-block:: sh

    pip install -e git+https://github.com/aivarsk/scruffy.git#egg=scruffy


Contact
-------

If you have questions, bug reports, suggestions, etc. please create an issue on
the `GitHub project page <http://github.com/paylogic/sphinx-scruffy>`_.


License
-------

This software is licensed under the `MIT license <http://en.wikipedia.org/wiki/MIT_License>`_

See `<LICENSE.txt>`_


© 2013 Paylogic International.
