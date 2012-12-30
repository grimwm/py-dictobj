import unittest

from dictobj import *

class TestDictionaryObject(unittest.TestCase):
  def setUp(self):
    self.vanilla = DictionaryObject((('a',1),('b',2)))
    self.kinky = DictionaryObject({'a':1, 'b':{'c':True, 'd':[1,2]}, 1:'x'})
    self.default = DictionaryObject((), None, a=3)
    self.mutable = MutableDictionaryObject(a=3, b=4)
    self.mutableDefault = MutableDictionaryObject((), None, b=4)

  def test_copy(self):
    x = MutableDictionaryObject(self.vanilla)
    self.assertEqual(x, self.vanilla)

    x.a = 2
    self.assertNotEqual(x, self.vanilla)
    
  def test_len(self):
    self.assertEqual(3, len(self.kinky))

  def test_default(self):
    self.assertEqual(self.default.a, 3)
    self.assertEqual(self.default.b, None)

    self.assertEqual(self.mutableDefault.a, None)
    self.assertEqual(self.mutableDefault.b, 4)

  def test_mutable(self):
    self.assertEqual(self.mutable.a, 3)
    self.assertEqual(self.mutable.b, 4)

    self.mutable.c = 5
    self.assertEqual(self.mutable.c, 5)
    
    self.assertRaises(AttributeError, getattr, self.mutable, 'd')

  def test_mutable_default(self):
    self.assertEqual(self.mutableDefault.b, 4)
    
    self.mutableDefault.c = 5
    self.assertEqual(self.mutableDefault.c, 5)

    self.assertEqual(self.mutableDefault.a, None)
    
  def test_iter(self):
    keys = [1,'a','b']
    for i,k in enumerate(sorted(self.kinky)):
      self.assertEqual(k, keys[i])

  def test_getattr(self):
    self.assertEqual(self.kinky.a, 1)
    self.assertEqual(self.kinky.b, DictionaryObject({'c':True, 'd':[1,2]}))

  def test_getitem(self):
    self.assertEqual(self.kinky['a'], 1)
    self.assertEqual(self.kinky['b'], DictionaryObject({'c':True, 'd':[1,2]}))
    self.assertEqual(self.kinky[1], 'x')

  def test_exception(self):
    self.assertRaises(AttributeError, setattr, self.kinky, 'c', 3)

unittest.main()
