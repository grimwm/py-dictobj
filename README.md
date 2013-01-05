py-dictobj
==========

This package extends the functionality of the normal Python dictionary by affording the
ability to lookup dictionary keys as instance attributes (i.e. `__getattr__`)
instead of "indices" (i.e. `__getitem__`).  Two caveats remain, however, prevent
the use of `__getattr__` in certain circumstances.  In these cases, access the
`DictionaryObject` using `__getitem__` (e.g. `d['3x&']`).  These cases are

 1. Names that do not follow the valid conventions for Normal Python syntax
 2. Names that match class attributes of the `DictionaryObject` class hierarchy
    (e.g. `d.keys` will return the method, not the value, assuming `d['keys']` exists).

There are two primary classes of interest: `DictionaryObject` and `MutableDictionaryObject`.
`DictionaryObject` is the base class, and it acts as an immutable dictionary.
`MutableDictionaryObject`, as the name implies, provides the ability to mutate the object via
`__setattr__` (e.g. `d.x = 500`) and `__setitem__` (e.g. `d['x'] = 500`).  For a description
on the design considerations behind this choice, please see [Immutable-by-Default](#mutability).

Care has been taken to make sure these classes are picklable so that they can be
stored and passed around, especially in the case of multiprocessing.  Care has
also been taken that the `__repr__` of these classes can be eval()'d by the Python
interpretter.

Mutable vs Immutable
--------------------

The base `DictionaryObject` class is itself __immutable__, meaning that once the data is
set during the call to `DictionaryObject.__init__`, no other keys may be added, nor
may any existing keys have their values changed.  One caveat to this is that if the
values a `DictionaryObject` points to are themselves __mutable__, then the underlying
object may change.

If your use-case requires a more liberal `DictionaryObject` with _mutability_, please use
`MutableDictionaryObject`.  It behaves the same, but you can add keys via `__setattr__`
or `__setitem__` (e.g. `d.x = 5` or `d['x'] = 5`).

<a name="mutability"></a>
Immutable-by-Default
--------------------

The base `DictionaryObject` was created as __immutable-by-default__ in order to facilitate
[Separation of Concerns](http://en.wikipedia.org/wiki/Separation_of_concerns)
By doing my best to ensure the top-level object is itself immutable, developers are more free
to consider an object instance as _static values_.  This allows them to make better assumptions,
such as the fact they cannot change any values and indirectly interfere with the processing of the
same data on another thread or process.

In practice, Python itself does support a model of strong assurances with regard to immutability.  So,
the programmer must still be careful; however, this package should help.

Installation
------------

If you have Python installed and wish to get the package directly from the
[Python Package Index](http://pypi.python.org/pypi/dictobj), just run
`pip install dictobj` from the command-line.  If you already have a prior
version installed, just run `pip install dictobj -U` instead.

Contribute
----------

Please help contribute to this project by going to the
[GitHub Project Repository](https://github.com/grimwm/py-dictobj) and doing one
of a few things:

 * send me pull requests through the github interface
 * point me directly to your git repo so I can pull changes
 * send bug reports and feature requests by filing them under the __Issues__ tab at the top

Examples
--------
    >>> d = DictionaryObject({'a':1, 'b':True, 3:'x'})
    >>> print d.a, d.b, d[3]
    1 True x
    
    >>> d = DictionaryObject((('a',1),('b',2)))
    >>> print d.a, d.b
    1 2
    
    >>> d = DictionaryObject(a=1, b=True)
    >>> print d
    DictionaryObject({'a': 1, 'b': True})

    >>> d = DictionaryObject({'a':1, 'b':True}, None)
    >>> print d.a, d.b, d.c, d.d
    1 True None None
    
    >>> d = DictionaryObject({'a':1}, None)
    >>> m = MutableDictionaryObject(d)
    >>> print d == m
    True
    >>> m.a = 0
    >>> print d == m, d < m, d > m, d != m, d <= m, d >= m
    False False True True False True
  
    >>> import pickle
    >>> m1 = MutableDictionaryObject({'a':1}, None)
    >>> m2 = pickle.loads(pickle.dumps(m1))
    >>> print m1 == m2
    True
    >>> m1.a = 3
    >>> print m1 == m2
    False

    >>> d = DictionaryObject({'keys':[1,2], 'values':3, 'x':1})
    >>> d.keys
    <bound method DictionaryObject.keys of DictionaryObject({'keys': [1, 2], 'x': 1, 'values': 3})>
    >>> d.values
    <bound method DictionaryObject.values of DictionaryObject({'keys': [1, 2], 'x': 1, 'values': 3})>
    >>> d.x
    1
    >>> d['keys']
    [1, 2]
    >>> d['values']
    3
