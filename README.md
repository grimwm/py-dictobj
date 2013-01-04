py-dictobj
==========

A set of Python dictionary objects where keys can be accessed as instance attributes.
These classes have all the functionality of a normal Python dictionary, except
in the case of the DictionaryObject, which is itself immutable.  In addition,
these classes also have the added feature of being able to lookup values by
using keys as attributes.

`DictionaryObject` is an immutable version of these dictionary objects, while, of
course, `MutableDictionaryObject` is the mutable version.  Use whichever one
seems more appropriate for your use case.

Care has been taken to make sure these classes are picklable so that they can be
stored and passed around, especially in the case of multiprocessing.  Care has
also been taken that the `__repr__` of these classes can be eval()'d by the Python
interpretter.

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
