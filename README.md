py-dictobj
==========

A set of Python dictionary objects where keys can be access as instnace attributes.
These classes have all the functionality of a normal Python dictionary, except
in the case of the DictionaryObject, which is itself immutable.  In addition,
these classes also have the added feature of being able to lookup values by
using keys as attributes.

DictionaryObject is an immutable version of these dictionary objects, while, of
course, MutableDictionaryObject is the mutable version.  Use whichever one
seems more appropriate for your use case.

Examples:
  > &gt;&gt;&gt; d = DictionaryObject({'a':1, 'b':True, 3:'x'}) <br>
  > &gt;&gt;&gt; print d.a, d.b, d[3] <br>
  > 1 True x
  
  > &gt;&gt;&gt; d = DictionaryObject((('a',1),('b',2))) <br>
  > &gt;&gt;&gt; print d.a, d.b <br>
  > 1 2

  > &gt;&gt;&gt; d = DictionaryObject(a=1, b=True) <br>
  > &gt;&gt;&gt; print d <br>
  > {'a':1, b=True}

  > &gt;&gt;&gt; d = DictionaryObject({'a':1, 'b':True}, None) <br>
  > &gt;&gt;&gt; print d.a, d.b, d.c, d.d <br>
  > 1 True None None
  
  > &gt;&gt;&gt; d = MutableDictionaryObject({'a':1, 'b':True}, None) <br>
  > &gt;&gt;&gt; print d.a, d.b, d.c, d.d <br>
  > 1 True None None <br>
  > &gt;&gt;&gt; d.c = 3 <br>
  > &gt;&gt;&gt; del d.a <br>
  > &gt;&gt;&gt; print d.a, d.b, d.c, d.d <br>
  > None True 3 None

  > &gt;&gt;&gt; d = DictionaryObject({'a':1}, None) <br>
  > &gt;&gt;&gt; m = MutableDictionaryObject(d) <br>
  > &gt;&gt;&gt; print d == m <br>
  > True <br>
  > &gt;&gt;&gt; m.a = 0 <br>
  > &gt;&gt;&gt; print d == m, d &lt; m, d &gt; m, d != m, d &lt;= m, d &gt;= m <br>
  > False False True True False True

  > &gt;&gt;&gt; import pickle <br>
  > &gt;&gt;&gt; m1 = MutableDictionaryObject({'a':1}, None) <br>
  > &gt;&gt;&gt; m2 = pickle.loads(pickle.dumps(m1)) <br>
  > &gt;&gt;&gt; print m1 == m2 <br>
  > True <br>
  > &gt;&gt;&gt; m1.a = 3 <br>
  > &gt;&gt;&gt; print m1 == m2 <br>
  > False
  