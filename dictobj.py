class DictionaryObject(object):
  """
  A class that has all the functionality of a normal Python dictionary, except
  for the fact it is itself immutable, but it also has the added feature of
  being able to lookup values by using keys as attributes.
  
  Example:
    >>> d = DictionaryObject({'a':1, 'b':True, 3:'x'})
    >>> print d.a, d.b, d[3]
    1 True x
    
    >>> d = DictionaryObject((('a',1),('b',2)))
    >>> print d.a, d.b
    1 2
    
    >>> d = DictionaryObject(a=1, b=True)
    >>> print d
    {'a':1, b=True}
  """
  def __init__(self, *args, **kwargs):
    """
    Take as input a dictionary-like object and return a DictionaryObject.
    If recursive is True, then make sure any keys containing dictionaries
    are also converted to DictionaryObjects.  Otherwise, leave them as vanilla
    Python dictionaries.
    """
    super(DictionaryObject, self).__init__()

    if len(args) > 1:
      raise TypeError("expected at most 1 argument, got %d" % len(args))

    dictionary = dict(args[0]) if 1 == len(args) else {}

    if len(kwargs) > 0:
      if len(args) > 0:
        raise TypeError('Cannot mix args and kwargs.')
      dictionary = dict(kwargs)
    
    items = {}
    for k in dictionary:
      items[k] = dictionary[k]
    for k in items:
      if isinstance(items[k], dict): 
        items[k] = DictionaryObject(items[k])
    self.__dict__['_items'] = items

  def __getattr__(self, name):
    """
    This is the method that makes all the magic happen.  Obviously, for
    certain reasons, it makes sense for "keys" matching the same name
    as our internal methods, we want to return the methods instead of
    the value out of the dictionary.

    Example:
      >>> d = DictionaryObject({'keys':[1,2], 'values':3, 'x':1})
      >>> d.keys ==> Will return DictionaryObject.keys() method
      >>> d.values ==> Will return DictionaryObject.values() method
      >>> d.x ==> Will return value 1
      >>> d['keys'] ==> Will return value [1,2]
      >>> d['values'] ==> Will return value 3.
    """
    if name in self.__dict__:
      return self.__dict__[name]
    if name in self._items:
      return self._items[name]
    raise AttributeError("'%s' object has no attribute '%s'" % (__name__, name))

  def __setattr__(self, name, value):
    raise AttributeError("'%s' object does not support assignment" % __name__)

  def __getitem__(self, name):
    return self._items[name]
    
  def __contains__(self, name):
    return name in self._items
    
  def __len__(self):
    return len(self._items)
    
  def __iter__(self):
    return iter(self._items)
      
  def __repr__(self):
    return repr(self._items)
    
  def __str__(self):
    return str(self._items)

  def __cmp__(self, rhs):
    return cmp(self._items, rhs._items)

  def keys(self):
    return self._items.keys()
    
  def values(self):
    return self._items.values()
