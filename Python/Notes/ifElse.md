---
title: 条件语句
Mon 25 Dec 2017 10:58:32 PM CST
tag: [python]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

```python
if number < 0:
    pass
elif number == 0:
    pass
else:
    pass
```

- 真值检测
```python
if x:
    pass
```

## 斐波那契数列
```python
a,b = 0, 1
while b < 100:
    print(b)
    a,b = b, a+b
```

- `print`的另一个参数'end' 可以替换默认的换行符。`print(a, end = ' ')`这个是'python3'的语法，'python2'会报错。
- 'print("-"*50)' 输出50个‘-’
