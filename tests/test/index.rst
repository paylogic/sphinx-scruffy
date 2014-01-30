===========
Test system
===========


Purpose
-------

Generic diagram

.. scruffy::

    [Author]<>1-0..*>[Book]
    [AddressInfo]<0..*-1<>[Author]
    [AddressInfo]<0..1-1<>[Author{bg:orange}]


Sequence diagram

.. scruffy::
  :sequence:

  [Patron]order food>[Waiter]
  [Waiter]order food>[Cook]
  [Waiter]serve wine>[Patron]
  [Cook]pickup>[Waiter]
  [Waiter]serve food>[Patron]
  [Patron]pay>[Cashier]


Errored diagram

.. scruffy::

    sdafsadfasdfas fasdf asdf
