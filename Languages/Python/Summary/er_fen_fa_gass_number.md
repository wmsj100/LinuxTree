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
