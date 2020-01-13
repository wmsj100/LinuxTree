---
title: 二分法猜数字
date: 2020-01-12 16:43:53
modify: 
tags: [Summary]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# 二分法猜数字

## 概要

- 对于二分法这个概念很早就有了，知道它是取中间数值，然后不停判断
- 二分法也是典型的递归思想

## 代码

- 场景：手动输入一个数字，电脑自动运行猜测，判断猜正确需要多少次
- 这个题之前做过，大概思路有，然后就一直做，差不多2小时吧，最后还是查找资料，修改了自己的变量名称然后结合打印过程瞬间就有思路了，代码如下
```python
def gassNum(top=100):
    target = 0
    count = 0 # 猜测次数

    while True:
        target = input("Please input number(1-100)")

        if not target.isdigit():
            print("Please input correct number(1-100)")
        else:
            target = int(target)
            break

    result = {
        'lower': 0,
        'upper': top,
        'middle': 0,
        'target': target,
        'count': 0,
    }

    gass(**result)

def gass(**args):
    middle = args['middle'] = int((args['lower'] + args['upper'])/2)
    target = args['target']
    args['count'] += 1
    print(args)

    if middle == target:
        return args
    else:
        if middle > target:
            args['upper'] = middle-1
        else:
            args['lower'] = middle+1
        gass(**args)

gassNum(100)

# Please input number(1-100)74
# {'lower': 0, 'upper': 100, 'middle': 50, 'target': 74, 'count': 1}
# {'lower': 51, 'upper': 100, 'middle': 75, 'target': 74, 'count': 2}
# {'lower': 51, 'upper': 74, 'middle': 62, 'target': 74, 'count': 3}
# {'lower': 63, 'upper': 74, 'middle': 68, 'target': 74, 'count': 4}
# {'lower': 69, 'upper': 74, 'middle': 71, 'target': 74, 'count': 5}
# {'lower': 72, 'upper': 74, 'middle': 73, 'target': 74, 'count': 6}
# {'lower': 74, 'upper': 74, 'middle': 74, 'target': 74, 'count': 7}
```

- 代码优化，提供上下限自定义功能，函数提供参数校验，不允许多余参数传入
```python
"""
猜数字，灵活定义数字的上下限
输入一个在upper/lower范围内的值，电脑猜测并给出猜测过程
"""

def getInput(upper=100,lower=0):
    while True:
        passwd = input("please input your passwd: ")
        if passwd.isdigit():
            passwd = int(passwd)
            if upper < passwd or lower > passwd:
                print("Please input value should between %d ~ %d" % (lower,upper))
            else:
                break
        else:
            print("input error...,please again")
    return passwd

def gassNumber(lower=0,upper=100,middle=0,pwd=0,count=0):
    middle = int((lower + upper)/2)
    count += 1
    result = {
        'lower': lower,
        'upper': upper,
        'middle': middle,
        'pwd': pwd,
        'count': count
    }

    print(result)
    
    if pwd == middle:
        return result
    else:
        if middle > pwd:
            result['upper'] = middle - 1
        else:
            result['lower'] = middle + 1
        gassNumber(**result)
    
def init(upper=100,lower=0):
    passwd = getInput(upper=upper,lower=lower)
    gassNumber(pwd=passwd,upper=upper,lower=lower)

init(upper=999,lower=34)

# please input your passwd: 20
# Please input value should between 34 ~ 999
# please input your passwd: 33333
# Please input value should between 34 ~ 999
# please input your passwd: 56
# {'lower': 34, 'upper': 999, 'middle': 516, 'pwd': 56, 'count': 1}
# {'lower': 34, 'upper': 515, 'middle': 274, 'pwd': 56, 'count': 2}
# {'lower': 34, 'upper': 273, 'middle': 153, 'pwd': 56, 'count': 3}
# {'lower': 34, 'upper': 152, 'middle': 93, 'pwd': 56, 'count': 4}
# {'lower': 34, 'upper': 92, 'middle': 63, 'pwd': 56, 'count': 5}
# {'lower': 34, 'upper': 62, 'middle': 48, 'pwd': 56, 'count': 6}
# {'lower': 49, 'upper': 62, 'middle': 55, 'pwd': 56, 'count': 7}
# {'lower': 56, 'upper': 62, 'middle': 59, 'pwd': 56, 'count': 8}
# {'lower': 56, 'upper': 58, 'middle': 57, 'pwd': 56, 'count': 9}
# {'lower': 56, 'upper': 56, 'middle': 56, 'pwd': 56, 'count': 10}
```

## 思考

- 这个题目是猜测一个数字，是不是可以扩展到猜测密码，
- 比如现在有一个俩位数字的密码，需要多少次可以猜测出来。这个密码锁是齿轮结构，可以一个一个破解，破解一个，就能听到响应。
- 代码实现如下，结果是一个失败的需求
```python
"""
猜密码，二位数字，可以一个一个破解，破解一个就可以得到反馈
界面输入密码，2~6位
"""

def getPasswd():
    passwd = "" # 暂存用户输入的变量
    while True:
        # 接收界面输入，去除前后空格
        passwd = input("Please input your passwd number(0~9), width(2~6)").strip()

        # 确保输入全部是数字,否则重新输入
        if not passwd.isdigit():
            print("Please input correct number,and write again")
        else:
            break
    return passwd

def gassProcess(passwd):
    # 获取用户输入的密码长度，进行for循环遍历
    pwdLen = len(str(passwd))
    pwdList = []

    for index in range(pwdLen):
        pwd = gassSingleNumber(passwd[index])
        pwdList.append(pwd)
    return ''.join(pwdList)

def gassSingleNumber(pwd):
    # 代码写到这里发现这个需求不成立，因为如果密码可以拆分一个一个猜测，
    # 那么直接顺序按照0~9猜测就可以了，也不需要使用什么二分法了。
    # 这就是一个典型的开始构想的需求在开发过程中验证是不成立的
    # 项目放弃
    pass

def gasspasswd():
    passwd = getPasswd()
    gasspwd = gassProcess(passwd)
    print(passwd, gasswd)
```
