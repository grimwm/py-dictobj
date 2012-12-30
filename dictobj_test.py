import unittest

from dictobj import *

class TestDictionaryObject(unittest.TestCase):
  def setUp(self):
    self.vanilla = DictionaryObject((('a',1),('b',2)))
    self.kinky = DictionaryObject({'a':1, 'b':{'c':True, 'd':[1,2]}, 1:'x'})
    self.wowza = DictionaryObject({'a':1, 'b':2}, dictionary={'c':3})
    print self.wowza

  def test_len(self):
    self.assertEqual(3, len(self.kinky))
    
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
