class DictionaryObject(object):
  """
  A class that has all the functionality of a normal Python dictionary, except
  for the fact it is itself immutable.  It also has the added feature of
  being able to lookup values by using keys as attributes.

  The reason for the class being immutable by default is to help make it a
  little easier to use in multiprocessing situations.  Granted, the underlying
  values themselves are not deeply copied, but the aim is to enforce some
  ensurances of immutability on the container class.

  When using positional arguments, the first argument must always be something
  that would be a valid argument for a dict().  However, a second, optional
  argument may be passed to create a default value when keys are not found.
  
  Examples:
    >>> d = DictionaryObject({'a':1, 'b':True, 3:'x'})
    >>> print d.a, d.b, d[3]
    1 True x
    
    >>> d = DictionaryObject((('a',1),('b',2)))
    >>> print d.a, d.b
    1 2
    
    >>> d = DictionaryObject(a=1, b=True)
    >>> print d
    {'a':1, b=True}

    >>> d = DictionaryObject({'a':1, 'b':True}, None)
    >>> print d.a, d.b, d.c, d.d
    1 True None None
  """
  def __init__(self, contents=(), *args, **kwargs):
    """
    Take as input a dictionary-like object and return a DictionaryObject.
    It also makes sure any keys containing dictionaries are also converted
    to DictionaryObjects.
    """
    super(DictionaryObject, self).__init__()
    self.__dict__['_items'] = dict(contents, **kwargs)

    if args:
      self.__dict__['_defaultValue'] = args[0]
    self.__dict__['_defaultIsSet'] = len(args) > 0

    for k in self._items:
      if isinstance(self._items[k], dict): 
        self._items[k] = DictionaryObject(self._items[k])

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
    if name in self._items:
      return self._items[name]
    if self._defaultIsSet:
      return self._defaultValue
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

class MutableDictionaryObject(DictionaryObject):
  """
  Slight enhancement of the DictionaryObject allowing one to add
  attributes easily, in cases where that functionality is wanted.

  Examples:
    >>> d = MutableDictionaryObject({'a':1, 'b':True}, None)
    >>> print d.a, d.b, d.c, d.d
    1 True None None
    >>> d.c = 3
    >>> del d.a
    >>> print d.a, d.b, d.c, d.d
    None True 3 None
  """
  def __setattr__(self, name, value):
    self._items[name] = value

  def __delattr__(self, name):
    del self._items[name]

  def __delitem__(self, name):
    del self._items[name]
