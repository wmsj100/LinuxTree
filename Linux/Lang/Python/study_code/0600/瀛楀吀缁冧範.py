Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> q=[['name', 'age'], ['wmsj', 34]]
>>> q
[['name', 'age'], ['wmsj', 34]]
>>> w=dict(q)
>>> w
{'name': 'age', 'wmsj': 34}
>>> w['name']
'age'
>>> q=[['name', 'wmsj'], ['age', 23]]
>>> w=dict(q)
>>> w
{'age': 23, 'name': 'wmsj'}
>>> w['name']
'wmsj'
>>> w['age']
23
>>> e=dict(name='wmsj', age=23)
>>> e
{'age': 23, 'name': 'wmsj'}
>>> e==w
True
>>> e===w
SyntaxError: invalid syntax
>>> w
{'age': 23, 'name': 'wmsj'}
>>> len(w)
2
>>> w['sex']='male'
>>> w
{'age': 23, 'name': 'wmsj', 'sex': 'male'}
>>> del w['sex']
>>> w
{'age': 23, 'name': 'wmsj'}
>>> del w['ss']

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    del w['ss']
KeyError: 'ss'
>>> 'ss' in w
False
>>> 'name' in w
True
>>> q=[]
>>> q[1]

Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    q[1]
IndexError: list index out of range
>>> q[0]

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    q[0]
IndexError: list index out of range
>>> len(q)
0
>>> len(q)=1
SyntaxError: can't assign to function call
>>> r=dict()
>>> r
{}
>>> r[23]='ss'
>>> r
{23: 'ss'}
>>> r[23]
'ss'
>>> r['23']

Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    r['23']
KeyError: '23'
>>> r.23
SyntaxError: invalid syntax
>>> r[23]
'ss'
>>> r
{23: 'ss'}
>>> people = {
	'wmsj': {
		'phone': 1234,
		'addr': 'caojiamiu'
		},
	"wanmei': {
	
SyntaxError: EOL while scanning string literal
>>> people = {
	'wmsj': {
		'phone': 1234,
		'addr': 'caojiamiu'
		},
	"wanmei': {}}
	
SyntaxError: EOL while scanning string literal
>>> people = {
	'wmsj': {
		'phone': 1234,
		'addr': 'caojiamiu'
		},
	'wanmei': {
		''phone': 1234,
		'addr': 'caojiamiu'
		
SyntaxError: invalid syntax
>>> people = {
	'wmsj': {
		'phone': 1234,
		'addr': 'caojiamiu'
		},
	'wanmei': {
		'phone': 1234,
		'addr': 'caojiamiu'
		}
	}
>>> people
{'wanmei': {'phone': 1234, 'addr': 'caojiamiu'}, 'wmsj': {'phone': 1234, 'addr': 'caojiamiu'}}
>>> people['wmsj']
{'phone': 1234, 'addr': 'caojiamiu'}
>>> labels = {
	'phone': 'phone number',
	'addr': 'address'
	}
>>> req=raw_input('you write')
you writen
>>> req
'n'
>>> if req == 'n': key = 'phone'
req
SyntaxError: invalid syntax
>>> req=raw_input('')
p
>>> r=req
>>> r
'p'
>>> if r == 'p': key = 'phone'
r
SyntaxError: invalid syntax
>>> req
'p'
>>> r
'p'
>>> r == 'p'
True
>>> if r == 'p' : key = 'phone'
key
SyntaxError: invalid syntax
>>> name = raw_input('')
wmsj
>>> name
'wmsj'
>>> name in people
True
>>> r
'p'
>>> r == 'p'
True
>>> if r == 'p' : key = 'phone'

>>> r
'p'
>>> key
'phone'
>>> if r == 'a' : key = 'addr'

>>> r = raw_input('')
a
>>> r
'a'
>>> key
'phone'
>>> name
'wmsj'
>>> if name in people :
	print "%s's %s is %s." % \
	      (name, labels[key], people[name][key])

	
wmsj's phone number is 1234.
>>> labels
{'phone': 'phone number', 'addr': 'address'}
>>> key
'phone'
>>> label[key]

Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    label[key]
NameError: name 'label' is not defined
>>> labels[key]
'phone number'
>>> name = input('name')
name'wanmei'
>>> name
'wanmei'
>>> req = input('phone (p) or addr (a): ')
phone (p) or addr (a): 'a'
>>> req
'a'
>>> if req == 'p' : key = 'phone'

>>> key
'phone'
>>> req
'a'
>>> if req == 'a' : key = 'addr'

>>> key
'addr'
>>> name
'wanmei'
>>> name in people
True
>>> if name in people:
	print "%s's %s is %s." % (name, labels[key], people[name][key])

	
wanmei's address is caojiamiu.
>>> q
[]
>>> w
{'age': 23, 'name': 'wmsj'}
>>> 'name\'s name is $(name)s.' % w
"name's name is $(name)s."
>>> 'name\'s name is %(name)s.' % w
"name's name is wmsj."
>>> template = '''<html>
<head><title>%(title)s</title></head>
<body>
<h1>%(title)s</h1>
<p>%(text)s</p>
</body>
</html>
'''
>>> template
'<html>\n<head><title>%(title)s</title></head>\n<body>\n<h1>%(title)s</h1>\n<p>%(text)s</p>\n</body>\n</html>\n'
>>> print template
<html>
<head><title>%(title)s</title></head>
<body>
<h1>%(title)s</h1>
<p>%(text)s</p>
</body>
</html>

>>> data = {
	'title': 'my home page',
	'text': 'hello world!'
	}
>>> data
{'text': 'hello world!', 'title': 'my home page'}
>>> template % data
'<html>\n<head><title>my home page</title></head>\n<body>\n<h1>my home page</h1>\n<p>hello world!</p>\n</body>\n</html>\n'
>>> print template % data
<html>
<head><title>my home page</title></head>
<body>
<h1>my home page</h1>
<p>hello world!</p>
</body>
</html>

>>> w
{'age': 23, 'name': 'wmsj'}
>>> a=w
>>> a
{'age': 23, 'name': 'wmsj'}
>>> w={}
>>> w
{}
>>> a
{'age': 23, 'name': 'wmsj'}
>>> w=a
>>> w
{'age': 23, 'name': 'wmsj'}
>>> a
{'age': 23, 'name': 'wmsj'}
>>> w.clear()
>>> w
{}
>>> a
{}
>>> w={'age': 23, 'name': 'wmsj'}
>>> w
{'age': 23, 'name': 'wmsj'}
>>> a = w.copy()
>>> w
{'age': 23, 'name': 'wmsj'}
>>> a
{'age': 23, 'name': 'wmsj'}
>>> w.clear()
>>> w
{}
>>> a
{'age': 23, 'name': 'wmsj'}
>>> a
{'age': 23, 'name': 'wmsj'}
>>> w
{}
>>> from copy import deepcopy
>>> deepcopy
<function deepcopy at 0x0000000002DA37B8>
>>> w
{}
>>> w = a.copy()
>>> w
{'age': 23, 'name': 'wmsj'}
>>> r=deepcopy(a)
>>> r
{'age': 23, 'name': 'wmsj'}
>>> a['sex'] = [1,2,3]
>>> a
{'age': 23, 'name': 'wmsj', 'sex': [1, 2, 3]}
>>> w
{'age': 23, 'name': 'wmsj'}
>>> e
{'age': 23, 'name': 'wmsj'}
>>> r
{'age': 23, 'name': 'wmsj'}
>>> q=dict()
>>> q
{}
>>> q['stor'] = ['name', 'age']
>>> q
{'stor': ['name', 'age']}
>>> w=q.copy()
>>> e=deepcopy(q)
>>> w
{'stor': ['name', 'age']}
>>> e
{'stor': ['name', 'age']}
>>> q['stor']
['name', 'age']
>>> q['stor'].append('male')
>>> q
{'stor': ['name', 'age', 'male']}
>>> w
{'stor': ['name', 'age', 'male']}
>>> e
{'stor': ['name', 'age']}
>>> q=dict
>>> q
<type 'dict'>
>>> q1=dict.fromkeys(['name', 'age'])
>>> q1
{'age': None, 'name': None}
>>> q2 = dict.fromkeys(['name', 'age'], 'unknow')
>>> q2
{'age': 'unknow', 'name': 'unknow'}
>>> q2['age']
'unknow'
>>> q1
{'age': None, 'name': None}
>>> q1.get('sss')
>>> q1.get('sss', 's3')
's3'
>>> people
{'wanmei': {'phone': 1234, 'addr': 'caojiamiu'}, 'wmsj': {'phone': 1234, 'addr': 'caojiamiu'}}
>>> labels
{'phone': 'phone number', 'addr': 'address'}
>>> labels
{'phone': 'phone number', 'addr': 'address'}
>>> name
'wanmei'
>>> name = 'er'
>>> req
'a'
>>> req = raw_input('ss')
sse
>>> key = req
>>> if req == 'p' : key = 'phone';
s
SyntaxError: invalid syntax
>>> key
'e'
>>> print labels.get(key, 'not exist')
not exist
>>> print labels.get('phone', 'not exist')
phone number
>>> q1
{'age': None, 'name': None}
>>> q1.items()
[('age', None), ('name', None)]
>>> q3=q1.items()
>>> q3
[('age', None), ('name', None)]
>>> q3[0]
('age', None)
>>> q3[0][0]
'age'
>>> q3[0][0] = 1

Traceback (most recent call last):
  File "<pyshell#206>", line 1, in <module>
    q3[0][0] = 1
TypeError: 'tuple' object does not support item assignment
>>> q1.iteritems()
<dictionary-itemiterator object at 0x0000000002E69728>
>>> q4=q1.iteritems()
>>> q4
<dictionary-itemiterator object at 0x0000000002E69638>
>>> list(q4)
[('age', None), ('name', None)]
>>> q1.keys()
['age', 'name']
>>> q1.items()
[('age', None), ('name', None)]
>>> q1.iterkeys()
<dictionary-keyiterator object at 0x0000000002E697C8>
>>> q1
{'age': None, 'name': None}
>>> q1.pop('name')
>>> q1
{'age': None}
>>> q2
{'age': 'unknow', 'name': 'unknow'}
>>> q3
[('age', None), ('name', None)]
>>> q4
<dictionary-itemiterator object at 0x0000000002E69638>
>>> q4.list()

Traceback (most recent call last):
  File "<pyshell#220>", line 1, in <module>
    q4.list()
AttributeError: 'dictionary-itemiterator' object has no attribute 'list'
>>> list(q4)
[]
>>> q1
{'age': None}
>>> q1.popitem()
('age', None)
>>> q1
{}
>>> q1=dict.fromkeys(['name', 'age', 'sex'])
>>> q1
{'age': None, 'name': None, 'sex': None}
>>> q1.popitem()
('age', None)
>>> q1
{'name': None, 'sex': None}
>>> q1.pop()

Traceback (most recent call last):
  File "<pyshell#229>", line 1, in <module>
    q1.pop()
TypeError: pop expected at least 1 arguments, got 0
>>> q1.popitem()
('name', None)
>>> q1
{'sex': None}
>>> q1.popitem()
('sex', None)
>>> q1
{}
>>> q1.popitem()

Traceback (most recent call last):
  File "<pyshell#234>", line 1, in <module>
    q1.popitem()
KeyError: 'popitem(): dictionary is empty'
>>> q1
{}
>>> q1.setdefault('age')
>>> q1
{'age': None}
>>> q1['name'] = 'wmsj'
>>> q1
{'age': None, 'name': 'wmsj'}
>>> q1.setdefault('name', 'none')
'wmsj'
>>> q1
{'age': None, 'name': 'wmsj'}
>>> q1.setdefault('sex', 'people')
'people'
>>> q1
{'age': None, 'name': 'wmsj', 'sex': 'people'}
>>> q1.get('sss')
>>> q1.get('sss', 'not')
'not'
>>> q1
{'age': None, 'name': 'wmsj', 'sex': 'people'}
>>> del q1['age']
>>> q1
{'name': 'wmsj', 'sex': 'people'}
>>> q1.pop()

Traceback (most recent call last):
  File "<pyshell#249>", line 1, in <module>
    q1.pop()
TypeError: pop expected at least 1 arguments, got 0
>>> q1.pop('name')
'wmsj'
>>> q1
{'sex': 'people'}
>>> q1.popitem()
('sex', 'people')
>>> q
<type 'dict'>
>>> q1
{}
>>> q1.setdefault('name')
>>> q1
{'name': None}
>>> q2
{'age': 'unknow', 'name': 'unknow'}
>>> q1.update(q2)
>>> q1
{'age': 'unknow', 'name': 'unknow'}
>>> q2
{'age': 'unknow', 'name': 'unknow'}
>>> q1
{'age': 'unknow', 'name': 'unknow'}
>>> w1

Traceback (most recent call last):
  File "<pyshell#262>", line 1, in <module>
    w1
NameError: name 'w1' is not defined
>>> w1=dict(name='wmsj')
>>> w1
{'name': 'wmsj'}
>>> q1
{'age': 'unknow', 'name': 'unknow'}
>>> q1.update(w1)
>>> q1
{'age': 'unknow', 'name': 'wmsj'}
>>> w1['male'] = 'female'
>>> w1
{'male': 'female', 'name': 'wmsj'}
>>> q1
{'age': 'unknow', 'name': 'wmsj'}
>>> q1.update(w1)
>>> q1
{'age': 'unknow', 'male': 'female', 'name': 'wmsj'}
>>> q1
{'age': 'unknow', 'male': 'female', 'name': 'wmsj'}
>>> q1
{'age': 'unknow', 'male': 'female', 'name': 'wmsj'}
>>> q1.values()
['unknow', 'female', 'wmsj']
>>> q1.keys()
['age', 'male', 'name']
>>> print 12, 'sdf'
12 sdf
>>> print 'sdf' + ',',
sdf,
>>> print 'asdf' + ',', 234, 'sdf'
asdf, 234 sdf
>>> from string import join as hhh
>>> ' '.hhh([1,2,3])

Traceback (most recent call last):
  File "<pyshell#281>", line 1, in <module>
    ' '.hhh([1,2,3])
AttributeError: 'str' object has no attribute 'hhh'
>>> hhh
<function join at 0x000000000298EC18>
>>> r1 = ['s', 'd', 'g']
>>> ' '.hhh(r1)

Traceback (most recent call last):
  File "<pyshell#284>", line 1, in <module>
    ' '.hhh(r1)
AttributeError: 'str' object has no attribute 'hhh'
>>> hhh
<function join at 0x000000000298EC18>
>>> hhh(r1)
's d g'
>>> hhh(r1, '0')
's0d0g'
>>> '-'.join(r1)
's-d-g'
>>> x,y,z = 1,2,3
>>> x
1
>>> y
2
>>> z
3
>>> x,y = y,z
>>> x
2
>>> y
3
>>> z
3
>>> x
2
>>> q
<type 'dict'>
>>> q1
{'age': 'unknow', 'male': 'female', 'name': 'wmsj'}
>>> key, val = q1.popitem()
>>> key
'age'
>>> val
'unknow'
>>> x,y,z = 1,2

Traceback (most recent call last):
  File "<pyshell#303>", line 1, in <module>
    x,y,z = 1,2
ValueError: need more than 2 values to unpack
>>> x=y={'name': 'wmsj'}
>>> x
{'name': 'wmsj'}
>>> y
{'name': 'wmsj'}
>>> y.popitem()
('name', 'wmsj')
>>> y
{}
>>> x
{}
>>> x
{}
>>> x=1
>>> x
1
>>> x+=2
>>> x
3
>>> x*=2
>>> x
6
>>> y='asdf'
>>> y+='kkl'
>>> 
>>> y
'asdfkkl'
>>> y*=2
>>> y
'asdfkklasdfkkl'
>>> bool(0)
False
>>> bool(())
False
>>> bool({})
False
>>> bool(Nune)

Traceback (most recent call last):
  File "<pyshell#326>", line 1, in <module>
    bool(Nune)
NameError: name 'Nune' is not defined
>>> bool(None)
False
>>> bool(Nan)

Traceback (most recent call last):
  File "<pyshell#328>", line 1, in <module>
    bool(Nan)
NameError: name 'Nan' is not defined
>>> bool('')
False
>>> bool('None')
True
>>> bool(0)
False
>>> bool(())
False
>>> bool({})
False
>>> bool([])
False
>>> bool('ss')
True
>>> num = input('ss')
ss4
>>> num
4
>>> input('as')
assd

Traceback (most recent call last):
  File "<pyshell#338>", line 1, in <module>
    input('as')
  File "<string>", line 1, in <module>
NameError: name 'sd' is not defined
>>> num
4
>>> if num < 0 :
	print "fu shu"
	elif num > 0:
		
SyntaxError: invalid syntax
>>> if num < 0 :
	print 'fu shu'

	
>>> if num > 0:
	print 'sss';
    elif num < 0:
	    
  File "<pyshell#348>", line 4
    elif num < 0:
                ^
IndentationError: unindent does not match any outer indentation level
>>> elif num < 0:
	
SyntaxError: invalid syntax
>>> if num > 0: print 'asdf' elif num < 0 : print 'xiao yu' else print '==0'
SyntaxError: invalid syntax
>>> name = raw_input('sss')
ssswmsj
>>> name.endswith('sss')
False
>>> name.endswith('sj')
True
>>> name.endswith('wmsj')
True
>>> 
