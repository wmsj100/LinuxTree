Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> tag = 'http://www.paython.org'
>>> tag[3:5]
'p:'
>>> tag[5: -1]
'//www.paython.or'
>>> tag[5: 0]
''
>>> tag[-3: -1]
'or'
>>> tag[-3: 0]
''
>>> tag[-3:]
'org'
>>> tag[3:]
'p://www.paython.org'
>>> tag[: 5]
'http:'
>>> tag[:]
'http://www.paython.org'
>>> #sldfgj
>>> url = raw_input('url: ')
url: www.wmsj100.com
>>> url
'www.wmsj100.com'
>>> url[3, -4]

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    url[3, -4]
TypeError: string indices must be integers, not tuple
>>> url[3: -4]
'.wmsj100'
>>> url[4: -4]
'wmsj100'
>>> tag
'http://www.paython.org'
>>> tag[3: :2]
'p/wwpyhnog'
>>> tag[3: : -2]
'pt'
>>> tag[: 5: -2]
'gonhypww'
>>> tag[5: : -2]
'/pt'
>>> [1,2,3] + [3,4]
[1, 2, 3, 3, 4]
>>> [1,2,3] + '1w'

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    [1,2,3] + '1w'
TypeError: can only concatenate list (not "str") to list
>>> 'we3' * 4
'we3we3we3we3'
>>> [3e] * 4
SyntaxError: invalid syntax
>>> ['3er'] * 4
['3er', '3er', '3er', '3er']
>>> []
[]
>>> []*4
[]
>>> [0] *4
[0, 0, 0, 0]
>>> [none] * 5

Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    [none] * 5
NameError: name 'none' is not defined
>>> [None ] * 4
[None, None, None, None]
>>> len('sdfa')
4
>>> sentence = raw_input('str: ')
str: This is your word!
>>> sentence
'This is your word!'
>>> text_width = len(sentence)
>>> text_width
18
>>> screen = 640
>>> left_margin = (screen - text_width)//2
>>> left_margin
311
>>> print ' ' * left_margin + '+' + '-' * (text_width + 4) + '+'
                                                                                                                                                                                                                                                                                                                       +----------------------+
>>> print ' ' * left_margin + '+' + '-' * (text_width + 4) + '+' /
SyntaxError: invalid syntax
>>> print

>>> print ' ' * left_margin + '+' + '-' * (text_width + 4) + '+'
                                                                                                                                                                                                                                                                                                                       +----------------------+
>>> print ' ' * left_margin + '|' + ' ' * 2 + sentence + ' ' * 2 + '|'
                                                                                                                                                                                                                                                                                                                       |  This is your word!  |
>>> print ' ' * (left_margin  + 4) + '| ' + ' ' * text_width + ' |'
                                                                                                                                                                                                                                                                                                                           |                    |
>>> print ' ' * (left_margin  + 4) + '| ' + sentence + ' |'
                                                                                                                                                                                                                                                                                                                           | This is your word! |
>>> print ' ' * (left_margin  + 4) + '| ' + ' ' * text_width + ' |'
                                                                                                                                                                                                                                                                                                                           |                    |
>>> print ' ' * left_margin + '+' + '-' * (left_margin + 4) + '+'
                                                                                                                                                                                                                                                                                                                       +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>>> print ' ' * left_margin + '+' + '-' * (text_width + 4) + '+'
                                                                                                                                                                                                                                                                                                                       +----------------------+
>>> 'w' in 'wer'
True
>>> '$$$' in '$$$sdf$$$'
True
>>> 'we' in ['we', 'wf']
True
>>> [1,2] in [[1,2,3], [1,2], [4,5]]
True
>>> [1] in [[1,2,3], [1,2], [4,5]]
False
>>> database = [
	['wmsj', '1234'],
	['qw', '2345
	 
SyntaxError: EOL while scanning string literal
>>> database = [
	['wmsj', '1234'],
	['qw', '2345']
	]
>>> database
[['wmsj', '1234'], ['qw', '2345']]
>>> username = raw_input('your name: ')
your name: wmsj
>>> pass = raw_input('your pass: ')
SyntaxError: invalid syntax
>>> passval = raw_input('your pass: ')
your pass: 1234
>>> if[username, passval] in database : print 'Sussess login!'
username
SyntaxError: invalid syntax
>>> passval
'1234'
>>> username
'wmsj'
>>> if[username, passval] in database : print 'Sussess login!'

Sussess login!
>>> # 这个方法可以用于验证用户登录
>>> len(456)

Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    len(456)
TypeError: object of type 'int' has no len()
>>> len([2,3])
2
>>> len({a: 1, b: 2})

Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    len({a: 1, b: 2})
NameError: name 'a' is not defined
>>> num = [23, 12, 45]
>>> max(num)
45
>>> min(num)
12
>>> len(num)
3
>>> max(34, 2, 45)
45
>>> min(2, 1)
1
>>> list('hello')
['h', 'e', 'l', 'l', 'o']
>>> arr = list('hello')
>>> arr
['h', 'e', 'l', 'l', 'o']
>>> arr[0]
'h'
>>> arr[0] = 'H'
>>> arr
['H', 'e', 'l', 'l', 'o']
>>> ''.join(arr)
'Hello'
>>> ' '.join(arr)
'H e l l o'
>>> '-'.join(arr)
'H-e-l-l-o'
>>> arr
['H', 'e', 'l', 'l', 'o']
>>> arr[12]

Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    arr[12]
IndexError: list index out of range
>>> len(arr)
5
>>> arr[5]

Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    arr[5]
IndexError: list index out of range
>>> arr[len(arr)-1]
'o'
>>> del arr[1]
>>> arr
['H', 'l', 'l', 'o']
>>> name=list('hello')
>>> name
['h', 'e', 'l', 'l', 'o']
>>> name[1:]
['e', 'l', 'l', 'o']
>>> name[1:] = list('ython')
>>> name
['h', 'y', 't', 'h', 'o', 'n']
>>> nums=[1,5]
>>> nums
[1, 5]
>>> nums[1:1]
[]
>>> nums[1:1] = [2,3,4]
>>> nums
[1, 2, 3, 4, 5]
>>> nums
[1, 2, 3, 4, 5]
>>> nums[1: len(nums)-1]
[2, 3, 4]
>>> nums[1: len(nums)-1] = []
>>> nums
[1, 5]
>>> nums[1] = None
>>> nums
[1, None]
>>> del nums[1]
>>> nums
[1]
>>> nums = [1,2,3,4]
>>> nums.append('er')
>>> nums
[1, 2, 3, 4, 'er']
>>> nums[1:1] = 'er'
>>> nums
[1, 'e', 'r', 2, 3, 4, 'er']
>>> nums[1:1] = ['er
	     
SyntaxError: EOL while scanning string literal
>>> nums[1:1] = ['er']
>>> nums
[1, 'er', 'e', 'r', 2, 3, 4, 'er']
>>> nums.count('er')
2
>>> nums.count('e')
1
>>> nums[1:2]
['er']
>>> nums
[1, 'er', 'e', 'r', 2, 3, 4, 'er']
>>> num1=[1,2]
>>> nums.extend(num1)
>>> nums
[1, 'er', 'e', 'r', 2, 3, 4, 'er', 1, 2]
>>> nums[len(nums)-1:]
[2]
>>> nums[len(nums)]

Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    nums[len(nums)]
IndexError: list index out of range
>>> nums[len(nums):]
[]
>>> nums[len(nums):] = num1
>>> nums
[1, 'er', 'e', 'r', 2, 3, 4, 'er', 1, 2, 1, 2]
>>> nums.extend(num1)
>>> nums
[1, 'er', 'e', 'r', 2, 3, 4, 'er', 1, 2, 1, 2, 1, 2]
>>> nums.index(2)
4
>>> nums.index(' a')

Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    nums.index(' a')
ValueError: ' a' is not in list
>>> 2 in nums
True
>>> nums
[1, 'er', 'e', 'r', 2, 3, 4, 'er', 1, 2, 1, 2, 1, 2]
>>> nums.insert(1, 'wmsj')
>>> nums
[1, 'wmsj', 'er', 'e', 'r', 2, 3, 4, 'er', 1, 2, 1, 2, 1, 2]
>>> nums[1:1] = ['wmsj']
>>> nums
[1, 'wmsj', 'wmsj', 'er', 'e', 'r', 2, 3, 4, 'er', 1, 2, 1, 2, 1, 2]
>>> nums = [1,2,3]
>>> nums
[1, 2, 3]
>>> nums.pop()
3
>>> nums
[1, 2]
>>> nums.pop(0)
1
>>> nums
[2]
>>> nums = [1,2,3]
>>> nums.append(nums.pop())
>>> nums
[1, 2, 3]
>>> nums
[1, 2, 3]
>>> nums.insert(1, 'wmsj')
>>> nums
[1, 'wmsj', 2, 3]
>>> nums.remove('wmsj')
>>> nums
[1, 2, 3]
>>> nums
[1, 2, 3]
>>> nums.reverse()
>>> nums
[3, 2, 1]
>>> ''.join(list('hell0').reverse())

Traceback (most recent call last):
  File "<pyshell#160>", line 1, in <module>
    ''.join(list('hell0').reverse())
TypeError: can only join an iterable
>>> list('hello')
['h', 'e', 'l', 'l', 'o']
>>> list('hello').reverse()
>>> str = 'hello'
>>> str
'hello'
>>> arr = list(str).reverse()
>>> arr
>>> arr = list(str)
>>> arr
['h', 'e', 'l', 'l', 'o']
>>> arr.reverse()
>>> arr
['o', 'l', 'l', 'e', 'h']
>>> ''.join(arr)
'olleh'
>>> 
