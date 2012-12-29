class DictionaryObject(object):
  """
  A class that has all the functionality of a normal Python dictionary, except
  for the fact it is itself immutable, but it also has the added feature of
  being able to lookup values by using keys as attributes.
  
  Example:
    d = DictionaryObject({'a':1, 'b':True, 3:'x'})
    print d.a, d.b, d[3] ==> 1 True x
  """
  def __init__(self, dictionary=None, recursive=True):
    """
    Take as input a dictionary-like object and return a DictionaryObject.
    If recursive is True, then make sure any keys containing dictionaries
    are also converted to DictionaryObjects.  Otherwise, leave them as vanilla
    Python dictionaries.
    """
    if recursive:
      items = {}
      for k in dictionary: 
        items[k] = dictionary[k]
      for k in items:
        if isinstance(items[k], dict): 
          items[k] = DictionaryObject(items[k], recursive)
      self.__dict__['_items'] = items
    else: 
      self.__dict__['_items'] = dictionary
  
  def __getattr__(self, name):
    if name in self.__dict__: 
      return self.__dict__[name]
    if name in self._items: 
      return self._items[name]
    raise AttributeError("'dict' object has no attribute '%s'" % name)

  def __setattr__(self, name, value):
    raise AttributeError("'dict' object has no attribute '%s'" % name)

  def __getitem__(self, name): 
    return self._items[name]
    
  def __contains__(self, name): 
    return name in self._items
    
  def __len__(self): 
    return len(self._items)
    
  def __iter__(self):
    for k in self._items.keys(): 
      yield k
      
  def __reversed__(self):
    for k in reversed(self._items.keys()): 
      yield k

  def __repr__(self): 
    return repr(self._items)
    
  def __str__(self): 
    return str(self._items)

  def keys(self): 
    return self._items.keys()
    
  def values(self): 
    return self._items.values()
