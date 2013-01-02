py-dictobj
==========

URL: https://github.com/grimwm/py-dictobj

A set of Python dictionary objects where keys can be accessed as instnace attributes.
These classes have all the functionality of a normal Python dictionary, except
in the case of the DictionaryObject, which is itself immutable.  In addition,
these classes also have the added feature of being able to lookup values by
using keys as attributes.

DictionaryObject is an immutable version of these dictionary objects, while, of
course, MutableDictionaryObject is the mutable version.  Use whichever one
seems more appropriate for your use case.

Care has been taken to make sure these classes are picklable so that they can be
stored and passed around, especially in the case of multiprocessing.  Care has
also been taken that the `__repr__` of these classes can be eval()'d by the Python
interpretter.

Examples
--------
    >>> d = DictionaryObject({'a':1, 'b':True, 3:'x'}) <br>
    >>> print d.a, d.b, d[3] <br>
    1 True x
    
    >>> d = DictionaryObject((('a',1),('b',2))) <br>
    >>> print d.a, d.b <br>
    1 2
  
    >>> d = DictionaryObject(a=1, b=True) <br>
    >>> print d <br>
    {'a':1, b=True}
  
    >>> d = DictionaryObject({'a':1, 'b':True}, None) <br>
    >>> print d.a, d.b, d.c, d.d <br>
    1 True None None
    
    >>> d = MutableDictionaryObject({'a':1, 'b':True}, None) <br>
    >>> print d.a, d.b, d.c, d.d <br>
    1 True None None <br>
    >>> d.c = 3 <br>
    >>> del d.a <br>
    >>> print d.a, d.b, d.c, d.d <br>
    None True 3 None
  
    >>> d = DictionaryObject({'a':1}, None) <br>
    >>> m = MutableDictionaryObject(d) <br>
    >>> print d == m <br>
    True <br>
    >>> m.a = 0 <br>
    >>> print d == m, d < m, d > m, d != m, d <= m, d >= m <br>
    False False True True False True
  
    >>> import pickle <br>
    >>> m1 = MutableDictionaryObject({'a':1}, None) <br>
    >>> m2 = pickle.loads(pickle.dumps(m1)) <br>
    >>> print m1 == m2 <br>
    True <br>
    >>> m1.a = 3 <br>
    >>> print m1 == m2 <br>
    False
    