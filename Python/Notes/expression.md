---
title: 表达式和运算符
Sat 23 Dec 2017 10:44:23 AM CST
tag: [python]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

# 运算符
- // 表示整除 4//3; 1
- % 求余数
- divmod(num1, num2) 返回一个包含俩个值的元组，第一个是num1和num2相整除得到的值，第二个值是num1和num2求余得到的值。
    - divmod(43, 30); // (1, 13)

- 关系运算符: >, <, >=, <=, ==, !=
- 逻辑运算符： and, or, not
    - and，or是短路运算符，返回最先确定结果的值，后面的值不会运行
    - 优先级： not > and > or； 逻辑运算符的优先级都小于关系运算符
    - a and not b or c === (a and (not b)) or c
    - 2 > 1 and not 3 > 5 or 4 == True and not False or 4 == True and True or 4 == True or 4 ==> True
- a+=3 == a = a+3
- a*=4 == a = a*4

## 类型转换
- float(string) 字符串 》 浮点数
- int(string) 字符串 》 整数值
- str(integer) 整数》 字符串
- str(float) 浮点数》字符串

- range(1,11) 获取数组，开始值是1，结束值是11-1； [1,2,3,...10]
- 
