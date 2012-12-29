import unittest

from dictobj import *

class TestDictionaryObject(unittest.TestCase):
  def setUp(self):
    d = {'a':1, 'b':{'c':True, 'd':[1,2]}, 1:'x'}
    self.vanilla = DictionaryObject(d, False)
    self.kinky = DictionaryObject(d)

  def test_len(self):
    self.assertEqual(3, len(self.vanilla))
    self.assertEqual(3, len(self.kinky))
    
  def test_iter(self):
    keys = [1,'a','b']
    for i,k in enumerate(sorted(self.vanilla)):
      self.assertEqual(k, keys[i])
    for i,k in enumerate(sorted(self.kinky)):
      self.assertEqual(k, keys[i])

  def test_getattr(self):
    self.assertEqual(self.vanilla.a, 1)
    self.assertEqual(self.vanilla.b, {'c':True, 'd':[1,2]})
    
    self.assertEqual(self.kinky.a, 1)
    self.assertEqual(self.kinky.b, DictionaryObject({'c':True, 'd':[1,2]}))

  def test_getitem(self):
    self.assertEqual(self.vanilla['a'], 1)
    self.assertEqual(self.vanilla['b'], {'c':True, 'd':[1,2]})
    self.assertEqual(self.vanilla[1], 'x')
    
    self.assertEqual(self.kinky['a'], 1)
    self.assertEqual(self.kinky['b'], DictionaryObject({'c':True, 'd':[1,2]}))
    self.assertEqual(self.kinky[1], 'x')

unittest.main()
