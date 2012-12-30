py-dictobj
==========

An immutable Python dictionary object where keys can be access as class attributes.

A class that has all the functionality of a normal Python dictionary, except
for the fact it is itself immutable, but it also has the added feature of
being able to lookup values by using keys as attributes.

Example:
  > >>> d = DictionaryObject({'a':1, 'b':True, 3:'x'})
  > >>> print d.a, d.b, d[3]
  > 1 True x

  > >>> d = DictionaryObject((('a',1),('b',2)))
  > >>> print d.a, d.b
  > 1 2
    
  > >>> d = DictionaryObject(a=1, b=True)
  > >>> print d
  > {'a':1, b=True}
