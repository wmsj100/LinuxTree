---
title: 异常处理
date: 2019-04-10 11:51:35	
modify: 
tag: [exception]
categories: Python
author: wmsj100
mail: wmsj100@hotmail.com
---

# 异常处理

## 概述
- 程序的健壮性由异常处理来决定，因为不能因为碰到异常就导致程序挂了，必须要捕获到异常，然后进行处理
- 异常的类都必须继承自`Exception`
- 捕获异常时候如果不清楚异常具体是什么类型的，可以抛出`Exception`这个是基类的异常，所以肯定会触发
- 异常通常是要配合日志`logging`来打印的，真正调试代码不建议使用`print`或者打断点来查看，直接输出日志就可以

## 范例

```python
import logging

logging.basicConfig(filename='./error_emp_log.log',level=logging.INFO,format="%(asctime)s [line:%(lineno)d] %(message)s")

class InvaidInputException(Exception):
    def __init__(self, message):
        super(InvaidInputException, self).__init__(message)
        self.message = message


class DependException(Exception):
    def __init__(self, message):
        super(DependException, self).__init__(message)
        self.message = message


class InternalException(Exception):
    def __init__(self, message):
        super(InternalException, self).__init__(message)
        self.message = message


hot = ['paper', 'fish', 'brash', 'oil']
u_dct = {
    1: ['game mouse', 'game jianpan'],
    2: ['kou hong', 'xiang shui']
}
geo_dct = {
    '1_1': ['huo guo', 'la jiao'],
    '1_2': ['san wen yu', 'ba jiao'],
    '1_3': ['black pip', 'good meat']
}


def getData(uid, jid, wid):
    u_val,g_val = [], []
    try:
        u_val = u_dct[uid]
    except Exception as e:
        logging.error('get u_val error: %s' % e)
    try:
        g_val = geo_dct['%d_%d' % (jid, wid)]
    except Exception as e:
        logging.error('get g_val error: %s' % e)
    res = hot + u_val + g_val
    return res


def getWebsite(uid, jid, wid):
    res = []
    try:
        res = getData(uid, jid, wid)
    except Exception as e:
        logging.error('getData error: %s' % e)
    return {uid: res, 'status': 200}


if __name__ == "__main__":
    res = 'error'
    try:
        res = getWebsite(1, 1,5)
    except Exception as e:
        logging.error('getWebsite error: %s' % e)
    print res
```

## 参考
- []()
