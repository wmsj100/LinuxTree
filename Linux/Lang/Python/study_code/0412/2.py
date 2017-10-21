Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #!/usr/bin/env python
>>> chomd a+x 1.py
SyntaxError: invalid syntax
>>> ll

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    ll
NameError: name 'll' is not defined
>>> ls

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    ls
NameError: name 'ls' is not defined
>>> cd d:
	
SyntaxError: invalid syntax
>>> ll

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    ll
NameError: name 'll' is not defined
>>> ls

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    ls
NameError: name 'ls' is not defined
>>> cd d
SyntaxError: invalid syntax
>>> ls

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    ls
NameError: name 'ls' is not defined
>>> exit
Use exit() or Ctrl-Z plus Return to exit
>>> ./1.py
SyntaxError: invalid syntax
>>> x="hello "
>>> y="world"
>>> x+y
'hello world'
>>> print "sss" + 42

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print "sss" + 42
TypeError: cannot concatenate 'str' and 'int' objects
>>> print "sss" + repr(42)
sss42
>>> print "sss" + `42`
sss42
>>> x='sss'
>>> x=32
>>> x
32
>>> repr(x)
'32'
>>> input("sss")
sss3
3
>>> raw_input("sss")
sss43
'43'
>>> name = input("ssss")
ssss

Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    name = input("ssss")
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> name = input("ssss")
ssssprint "hello" + name

Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    name = input("ssss")
  File "<string>", line 1
    print "hello" + name
        ^
SyntaxError: invalid syntax
>>> input('ssss')
ssssgr

Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    input('ssss')
  File "<string>", line 1, in <module>
NameError: name 'gr' is not defined
>>> input(sss)

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    input(sss)
NameError: name 'sss' is not defined
>>> input("sss")
sss"sss"
'sss'
>>> raw_input("sss")
sssgr
'gr'
>>> print "ssss\
sfall world"
sssssfall world
>>> print """sdfa" 'sdfa'
a;sdf"sfsa"
;;;'''asdf' """
sdfa" 'sdfa'
a;sdf"sfsa"
;;;'''asdf' 
>>> print r'hello/n /n'
hello/n /n
>>> print r'sdf/
SyntaxError: EOL while scanning string literal
>>> print r'sss\
'
sss\

>>> int('ss')

Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    int('ss')
ValueError: invalid literal for int() with base 10: 'ss'
>>> int('2')
2
>>> float('2)
      
SyntaxError: EOL while scanning string literal
>>> 
KeyboardInterrupt
>>> int('')

Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    int('')
ValueError: invalid literal for int() with base 10: ''
>>> 
input 'sss';
