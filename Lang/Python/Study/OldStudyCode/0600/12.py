Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
============ RESTART: C:/Users/Administrator/Desktop/diedaifn.py ============
>>> strs
['name', '[sdf]', 'age']
>>> sorted(strs)
['[sdf]', 'age', 'name']
>>> strs
['name', '[sdf]', 'age']
>>> reversed(strs)
<listreverseiterator object at 0x0000000001E4AB00>
>>> sorted('hello world')
[' ', 'd', 'e', 'h', 'l', 'l', 'l', 'o', 'o', 'r', 'w']
>>> reversed('hello world')
<reversed object at 0x0000000001E4AB00>
>>> x=reversed('hello world')
>>> x
<reversed object at 0x0000000002EB2BE0>
>>> list(x)
['d', 'l', 'r', 'o', 'w', ' ', 'o', 'l', 'l', 'e', 'h']
>>> ''.join(x)
''
>>> x
<reversed object at 0x0000000002EB2BE0>
>>> ''.join(reversed('hello'))
'olleh'
>>> list(x)
[]
>>> x=reversed('hello world')
>>> x
<reversed object at 0x0000000002EB2B70>
>>> ''.join(x)
'dlrow olleh'
>>> list(x)
[]
>>> range(99, 0)
[]
>>> range(99, 0, -1)
[99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> 
============ RESTART: C:/Users/Administrator/Desktop/diedaifn.py ============
81
>>> 
============ RESTART: C:/Users/Administrator/Desktop/diedaifn.py ============
you import: s
you word is: s
you import: d
you word is: d
you import: hello
you word is: hello
you import: 
>>> 
============ RESTART: C:/Users/Administrator/Desktop/diedaifn.py ============
you import: sdfa
you word is: sdfa
you import: 23
you word is: 23
you import: sa
you word is: sa
you import: 
>>> 
============ RESTART: C:/Users/Administrator/Desktop/diedaifn.py ============
not find
not find
not find
not find
not find
not find
not find
not find
not find
not find
not find
not find
not find
not find
not find
not find
not find
not find
you import: 
============ RESTART: C:/Users/Administrator/Desktop/diedaifn.py ============
>>> [x*x for x in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> [x*x for x in range(10) if not x%3]
[0, 9, 36, 81]
>>> [(x,y) for x in range(3) for y in range(3)]
[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
>>> [{'name': x, 'age': y} for x in range(3) for y in range(3)]
[{'age': 0, 'name': 0}, {'age': 1, 'name': 0}, {'age': 2, 'name': 0}, {'age': 0, 'name': 1}, {'age': 1, 'name': 1}, {'age': 2, 'name': 1}, {'age': 0, 'name': 2}, {'age': 1, 'name': 2}, {'age': 2, 'name': 2}]
>>> [(x, y) for x in range(3) for y in range(3)]
[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
>>> girls = ['alice', 'bernice', 'clarice']
>>> boys = ['chris', 'arnold', 'bob']
>>> girls
['alice', 'bernice', 'clarice']
>>> boys
['chris', 'arnold', 'bob']
>>> [b + '+' + g for b in boys for g in girls if b[0] == g[0]]
['chris+clarice', 'arnold+alice', 'bob+bernice']
>>> for b in boys:


	ss
	
KeyboardInterrupt
>>> wrap = {}
>>> for boy in boys:
	wrap.setdefault(boy[0], []).append(boy)

	
>>> wrap
{'a': ['arnold'], 'c': ['chris'], 'b': ['bob']}
>>> q={}
>>> q.setdefault('sd', [])
[]
>>> q
{'sd': []}
>>> q.setdefault('d', []).append('wmsj')
>>> q
{'d': ['wmsj'], 'sd': []}
>>> boys
['chris', 'arnold', 'bob']
>>> 
============ RESTART: C:/Users/Administrator/Desktop/diedaifn.py ============
>>> 
============ RESTART: C:/Users/Administrator/Desktop/diedaifn.py ============
>>> 
============ RESTART: C:/Users/Administrator/Desktop/diedaifn.py ============
>>> arr
['chris+chris', 'arnold+arnold', 'bob+bob']
>>> 
============ RESTART: C:/Users/Administrator/Desktop/diedaifn.py ============
>>> arr
['chris+chris', 'chris+char', 'arnold+arnold', 'bob+bob', 'char+chris', 'char+char']
>>> 
============ RESTART: C:/Users/Administrator/Desktop/diedaifn.py ============
>>> arr
['chris+chris', 'arnold+arnold', 'bob+bob']
>>> 
