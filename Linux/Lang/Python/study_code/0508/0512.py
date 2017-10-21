Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> tuple([1,2])
(1, 2)
>>> tuple([[1,2],[2,3]])
([1, 2], [2, 3])
>>> min('asd23A')
'2'
>>> q='asf234WUI@#'
>>> min(q)
'#'
>>> max(q)
's'
>>> len(q)
11
>>> len(q)
11
>>> 's' in q
True
>>> q[2:]
'f234WUI@#'
>>> q.sort()

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    q.sort()
AttributeError: 'str' object has no attribute 'sort'
>>> q.reverse

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    q.reverse
AttributeError: 'str' object has no attribute 'reverse'
>>> w='Hello, %s, %s enough for ya'
>>> w
'Hello, %s, %s enough for ya'
>>> e=('World', 'wmsj')
>>> e
('World', 'wmsj')
>>> w % e
'Hello, World, wmsj enough for ya'
>>> w
'Hello, %s, %s enough for ya'
>>> from math import pi
>>> pi
3.141592653589793
>>> pi.3f
SyntaxError: invalid syntax
>>> pi
3.141592653589793
>>> 'sddfa: %.3f' % pi
'sddfa: 3.142'
>>> from string import Template
>>> Template
<class 'string.Template'>
>>> s= Template('Hello $name, you age is $age')
>>> s
<string.Template object at 0x0000000003053CC0>
>>> d={}
>>> d['name'] = 'wmsj100'
>>> d.age=23

Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    d.age=23
AttributeError: 'dict' object has no attribute 'age'
>>> d['age
  
SyntaxError: EOL while scanning string literal
>>> d['age'] = 23
>>> d
{'age': 23, 'name': 'wmsj100'}
>>> s
<string.Template object at 0x0000000003053CC0>
>>> d
{'age': 23, 'name': 'wmsj100'}
>>> s.substitute(d)
'Hello wmsj100, you age is 23'
>>> r=Template('sdf${a}ljk')
>>> r
<string.Template object at 0x0000000003053C88>
>>> r.substitute(a='wmsj')
'sdfwmsjljk'
>>> r
<string.Template object at 0x0000000003053C88>
>>> r=Template('sdf$$sdf $sdf ')
>>> r.substitute(sdf='sdf123')
'sdf$sdf sdf123 '
>>> 2
2
>>> 2,
(2,)
>>> '$s + $s = $s' % (1,1,2)

Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    '$s + $s = $s' % (1,1,2)
TypeError: not all arguments converted during string formatting
>>> '%s + %s = $s' % (1,1,2)

Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    '%s + %s = $s' % (1,1,2)
TypeError: not all arguments converted during string formatting
>>> (1,1,2)
(1, 1, 2)
>>> '%s' % (1,)
'1'
>>> '%s +' % (1,)
'1 +'
>>> '%s + %s' %(1,2)
'1 + 2'
>>> '%s + %s = %s' % (1,2,3)
'1 + 2 = 3'
>>> '$%d' % 42
'$42'
>>> '%x' % 42
'2a'
>>> pi
3.141592653589793
>>> 'pi: %f...' % pi
'pi: 3.141593...'
>>> '%i' % pi
'3'
>>> '%s ' % 43l
'43 '
>>> '%r' % 43l
'43L'
>>> 
