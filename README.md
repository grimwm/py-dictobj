py-dictobj
==========

An immutable Python dictionary object where keys can be access as class attributes.

A class that has all the functionality of a normal Python dictionary, except
for the fact it is itself immutable, but it also has the added feature of
being able to lookup values by using keys as attributes.

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
