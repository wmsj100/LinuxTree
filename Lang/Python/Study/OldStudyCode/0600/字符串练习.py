Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 'sdf %S sdf %o' % ('wmsj', 23)

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    'sdf %S sdf %o' % ('wmsj', 23)
ValueError: unsupported format character 'S' (0x53) at index 5
>>> 'sdf %o sdf %o' % ('wmsj', 23)

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    'sdf %o sdf %o' % ('wmsj', 23)
TypeError: %o format: a number is required, not str
>>> q='hello %s lsdfj $s'
>>> q
'hello %s lsdfj $s'
>>> w='wmdj', 23
>>> w
('wmdj', 23)
>>> q %w

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    q %w
TypeError: not all arguments converted during string formatting
>>> q %s w
SyntaxError: invalid syntax
>>> w = 'wmsj', '23'
>>> w
('wmsj', '23')
>>> str(w)
"('wmsj', '23')"
>>> w
('wmsj', '23')
>>> q % w

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    q % w
TypeError: not all arguments converted during string formatting
>>> q
'hello %s lsdfj $s'
>>> print q % w

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print q % w
TypeError: not all arguments converted during string formatting
>>> w
('wmsj', '23')
>>> q
'hello %s lsdfj $s'
>>> q = 'hello %s asdff %s'
>>> q
'hello %s asdff %s'
>>>  q % w
 
  File "<pyshell#19>", line 2
    q % w
    ^
IndentationError: unexpected indent
>>> q % w
'hello wmsj asdff 23'
>>> from math import pi
>>> pi
3.141592653589793
>>> 'hello %.3f' % pi
'hello 3.142'
>>> s = Template('hello $s, weldcome $s);
	     
SyntaxError: EOL while scanning string literal
>>> s

Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> s= Template('hello $s, welcome $s')

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    s= Template('hello $s, welcome $s')
NameError: name 'Template' is not defined
>>> str.Template

Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    str.Template
AttributeError: type object 'str' has no attribute 'Template'
>>> string

Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    string
NameError: name 'string' is not defined
>>> from str import Template

Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    from str import Template
ImportError: No module named str
>>> from string
SyntaxError: invalid syntax
>>> from string import Template
>>> Template
<class 'string.Template'>
>>> s = Template('hello $s, welcome $s')
>>> s
<string.Template object at 0x0000000002E83978>
>>> s.substitute(s='wmsj')
'hello wmsj, welcome wmsj'
>>> x=Template('sdf{s}asf')
>>> x
<string.Template object at 0x0000000002DF2F28>
>>> x
<string.Template object at 0x0000000002DF2F28>
>>> x.substitute(s='234')
'sdf{s}asf'
>>> x=Template('asdf${s}asdf')
>>> x
<string.Template object at 0x0000000002E83CF8>
>>> x.substitute(s=23)
'asdf23asdf'
>>> s=Template('hello $name, your age is $age')
>>> s
<string.Template object at 0x0000000002DF2F28>
>>> obj={name: 1}

Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    obj={name: 1}
NameError: name 'name' is not defined
>>> obj = {'name': 'wmsj'}
>>> obj
{'name': 'wmsj'}
>>> obj['age'] = 23
>>> obj
{'age': 23, 'name': 'wmsj'}
>>> s
<string.Template object at 0x0000000002DF2F28>
>>> s.substitute(obj)
'hello wmsj, your age is 23'
>>> '%s + %s = %s' % (1,1,2)
'1 + 1 = 2'
>>> pi
3.141592653589793
>>> '%i' % pi
'3'
>>> '%f...' % pi
'3.141593...'
>>> '%f' % pi
'3.141593'
>>> '%s' % pi
'3.14159265359'
>>> '%r' % pi
'3.141592653589793'
>>> '%10f' % pi
'  3.141593'
>>> '%10.2f' % pi
'      3.14'
>>> '%1.2f' % pi
'3.14'
>>> '%5.2f' % pi
' 3.14'
>>> '%.5s' % 'hello my'
'hello'
>>> '%.*s' % (4, 'hello my')
'hell'
>>> '%010.2f' % pi
'0000003.14'
>>> '% 10.2f' % pi
'      3.14'
>>> '%-10.2f' % pi
'3.14      '
>>> '% 5d' % 10
'   10'
>>> '\n'
'\n'
>>> print ('% 5d' % 10) + '\n' + ('% 5d' % -10)
   10
  -10
>>> width = input('Please enter width: ')
Please enter width: 

Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    width = input('Please enter width: ')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> width

Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    width
NameError: name 'width' is not defined
>>> width = input('Please enter width: ')
Please enter width: 100
>>> width
100
>>> priceWidth= 10
>>> itemWidth = width - pri

Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    itemWidth = width - pri
NameError: name 'pri' is not defined
>>> itemWidth = width - priceWidth
>>> itemWidth
90
>>> headerFormate = '%-*s%*s'
>>> contentFormate = '%-*s%*.2f'
>>> print width
100
>>> print '=' * width
====================================================================================================
>>> width 60
SyntaxError: invalid syntax
>>> width = 60
>>> print '=' * width
============================================================
>>> itemWidth
90
>>> itemWidth = width - priceWidth
>>> itemWidth
50
>>> print headerFormate % (itemWidth, 'Item', priceWidth , 'Price')
Item                                                   Price
>>> print '-' * width
------------------------------------------------------------
>>> print contentFormate % (itemWidth, 'Apples', priceWidth, 0.4)
Apples                                                  0.40
>>> print contentFormate % (itemWidth, 'Pears', priceWidth, 1.923)
Pears                                                   1.92
>>> print '=' * widht

Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    print '=' * widht
NameError: name 'widht' is not defined
>>> print '=' * width
============================================================
>>> '%+10.2f' % pi
'     +3.14'
>>> '%+10.2f' % -pi
'     -3.14'
>>> s='hello my name is ...'
>>> s
'hello my name is ...'
>>> s.find('name')
9
>>> s.find('sss')
-1
>>> s.find('e')
1
>>> s.find('e', 1)
1
>>> s.find('e', 2)
12
>>> s.find('e', 2, 10)
-1
>>> q=[1,2,3,4]
>>> '+'.join(q)

Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    '+'.join(q)
TypeError: sequence item 0: expected string, int found
>>> str(q)
'[1, 2, 3, 4]'
>>> q=['1', '2', '3', '4']
>>> q
['1', '2', '3', '4']
>>> '+'.join(q)
'1+2+3+4'
>>> dir = 'file', 'window', 'python'
>>> dir
('file', 'window', 'python')
>>> '\'.join(dir)
SyntaxError: EOL while scanning string literal
>>> '\\'
'\\'
>>> '\'
SyntaxError: EOL while scanning string literal
>>> '/'
'/'
>>> '/'.join(dir)
'file/window/python'
>>> 'C://' + '/'.join(dir)
'C://file/window/python'
>>> print 'C:\'
SyntaxError: EOL while scanning string literal
>>> print 'c:\\'
c:\
>>> print 'C:\\' + '\\'.join(dir)
C:\file\window\python
>>> 'Hello My Name'.lower()
'hello my name'
>>> s
'hello my name is ...'
>>> s='Hello Name Is'
>>> s
'Hello Name Is'
>>> s.lower()
'hello name is'
>>> s.upper()
'HELLO NAME IS'
>>> q=['name', 'wmsj']
>>> 'Name'.lower() in q
True
>>> raw_input('asdf: '.lower())
asdf: HWLLO
'HWLLO'
>>> w=input('hell')
hellsdf

Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    w=input('hell')
  File "<string>", line 1, in <module>
NameError: name 'sdf' is not defined
>>> w=input('asdf: ').lower()
asdf: 'aHLO'
>>> w
'ahlo'
>>> raw_input('asdf: ').lower()
asdf: HleoH
'hleoh'
>>> s="that's is all words"
>>> s
"that's is all words"
>>> s.title()
"That'S Is All Words"
>>> import string
>>> string.capwords(s)
"That's Is All Words"
>>> s
"that's is all words"
>>> s.replace('s', 'S')
"that'S iS all wordS"
>>> s
"that's is all words"
>>> q
['name', 'wmsj']
>>> '+'.join(q)
'name+wmsj'
>>> q
['name', 'wmsj']
>>> w=' '.join(q)
>>> w
'name wmsj'
>>> w.split(' ')
['name', 'wmsj']
>>> w.split(' ') == q
True
>>> q
['name', 'wmsj']
>>> '  asdf asdf  '.strip()
'asdf asdf'
>>> '  ***!!! hello * name *! is **!!!  '.strip(' *!')
'hello * name *! is'
>>> translate

Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    translate
NameError: name 'translate' is not defined
>>> ''.translate
<built-in method translate of str object at 0x0000000001D4B148>
>>> from string import maketrans
>>> maketrans
<built-in function maketrans>
>>> table=maketrans('cs', 'kz')
>>> table
'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abkdefghijklmnopqrztuvwxyz{|}~\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff'
>>> len(table)
256
>>> table[97:123]
'abkdefghijklmnopqrztuvwxyz'
>>> maketrans()

Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    maketrans()
TypeError: maketrans() takes exactly 2 arguments (0 given)
>>> maketrans('', '')[97:123]
'abcdefghijklmnopqrstuvwxyz'
>>> s
"that's is all words"
>>> s.translate(table)
"that'z iz all wordz"
>>> s
"that's is all words"
>>> s='cat is like milk, I am is so'
>>> s
'cat is like milk, I am is so'
>>> s.translate(table)
'kat iz like milk, I am iz zo'
>>> s.translate(table, ' ')
'katizlikemilk,Iamizzo'
>>> s1='一， 二， 三‘
SyntaxError: EOL while scanning string literal
>>> s1='一二三'
>>> s1
'\xd2\xbb\xb6\xfe\xc8\xfd'
>>> 
