Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 's' in 'sfa'
True
>>> 3 in [2,3]
True
>>> len('sdfw')
4
>>> max([3,4])
4
>>> max(2,3)
3
>>> min(1,3)
1
>>> str = 'ssdfhelo'
>>> list(str)
['s', 's', 'd', 'f', 'h', 'e', 'l', 'o']
>>> arr = list(str)
>>> arr
['s', 's', 'd', 'f', 'h', 'e', 'l', 'o']
>>> del(arr[0])
>>> arr
['s', 'd', 'f', 'h', 'e', 'l', 'o']
>>> arr.count('e')
1
>>> arr.reverse()
>>> arr
['o', 'l', 'e', 'h', 'f', 'd', 's']
>>> arr.reverse()
>>> arr
['s', 'd', 'f', 'h', 'e', 'l', 'o']
>>> arr[1:] = [2,3,4]
>>> arr
['s', 2, 3, 4]
>>> arr[0:0] = [1]
>>> arr
[1, 's', 2, 3, 4]
>>> arr.insert(1, 'he')
>>> arr
[1, 'he', 's', 2, 3, 4]
>>> arr.append('r4')
>>> arr
[1, 'he', 's', 2, 3, 4, 'r4']
>>> arr.pop()
'r4'
>>> arr.pop(1)
'he'
>>> arr
[1, 's', 2, 3, 4]
>>> arr.extend([4,5,6])
>>> arr
[1, 's', 2, 3, 4, 4, 5, 6]
>>> arr.index(2)
2
>>> arr.index('s')
1
>>> arr.remove(4)
>>> ar

Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    ar
NameError: name 'ar' is not defined
>>> arr
[1, 's', 2, 3, 4, 5, 6]
>>> arr.sort()
>>> arr
[1, 2, 3, 4, 5, 6, 's']
>>> y = arr.sort()
>>> y
>>> arr
[1, 2, 3, 4, 5, 6, 's']
>>> y = arr.reverse()
>>> y
>>> arr
['s', 6, 5, 4, 3, 2, 1]
>>> y = arr.sorted()

Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    y = arr.sorted()
AttributeError: 'list' object has no attribute 'sorted'
>>> y=sorted(arr)
>>> y
[1, 2, 3, 4, 5, 6, 's']
>>> arr
['s', 6, 5, 4, 3, 2, 1]
>>> x=arr[:].sort()
>>> x
>>> x=arr[:]
>>> x
['s', 6, 5, 4, 3, 2, 1]
>>> arr
['s', 6, 5, 4, 3, 2, 1]
>>> x.sort()
>>> x
[1, 2, 3, 4, 5, 6, 's']
>>> arr
['s', 6, 5, 4, 3, 2, 1]
>>> sorted(arr).reverse()
>>> arr
['s', 6, 5, 4, 3, 2, 1]
>>> sorted(arr)
[1, 2, 3, 4, 5, 6, 's']
>>> w=sorted(arr).reverse()
>>> w
>>> x
[1, 2, 3, 4, 5, 6, 's']
>>> x.reverse()
>>> x
['s', 6, 5, 4, 3, 2, 1]
>>> sorted(x).reverse()
>>> arr
['s', 6, 5, 4, 3, 2, 1]
>>> cmp(1,2)
-1
>>> cmp(2,1)
1
>>> cmp(1,1)
0
>>> x
['s', 6, 5, 4, 3, 2, 1]
>>> x.sort(cmp)
>>> x
[1, 2, 3, 4, 5, 6, 's']
>>> q=['sd', 'asdf', 2, 'l']
>>> q
['sd', 'asdf', 2, 'l']
>>> q.sort(key=len)

Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    q.sort(key=len)
TypeError: object of type 'int' has no len()
>>> q
['sd', 'asdf', 2, 'l']
>>> q.remove(2)
>>> q
['sd', 'asdf', 'l']
>>> q.sort(key=len)
>>> q
['l', 'sd', 'asdf']
>>> q.sort(cmp)
>>> q
['asdf', 'l', 'sd']
>>> q.sort(reverse=true)

Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    q.sort(reverse=true)
NameError: name 'true' is not defined
>>> q.sort(reverse=True)
>>> q
['sd', 'l', 'asdf']
>>> ()
()
>>> 1,2,3
(1, 2, 3)
>>> (23,)
(23,)
>>> 32.
32.0
>>> 32,
(32,)
>>> 3*32,
(96,)
>>> 3*(32,)
(32, 32, 32)
>>> tuple([1,2,3])
(1, 2, 3)
>>> tuple('hello')
('h', 'e', 'l', 'l', 'o')
>>> x=tuple('hell')
>>> x
('h', 'e', 'l', 'l')
>>> x
('h', 'e', 'l', 'l')
>>> x
('h', 'e', 'l', 'l')
>>> x[1]
'e'
>>> x[1:]
('e', 'l', 'l')
>>> x[:]
('h', 'e', 'l', 'l')
>>> x
('h', 'e', 'l', 'l')
>>> 'h'
'h'
>>> 'h' in x
True
>>> x
('h', 'e', 'l', 'l')
>>> x.reverse()

Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    x.reverse()
AttributeError: 'tuple' object has no attribute 'reverse'
>>> 
