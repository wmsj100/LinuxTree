---
title: 八皇后
date: 2020-01-15 11:32:17
modify: 
tags: [Summary]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# 八皇后

## 概要

- 一个8*8的棋盘上放置皇后，皇后彼此不能水平或者垂直，并且不能处在彼此的对角线上，问一共由多少种放法

## 思路

- 因为要穷尽所有放法，就需要先给出所有的可能，包括正确和错误，
- 然后在其中删除不符合规则的放置方法，
- 剩下的就是正确的放法
- 比如是8个皇后，前面7个皇后随机放置，给出所有的可能性列表，然后从第八个皇后开始检测是否和规则冲突

## 代码

- 具体代码实现如下, 这段代码基本上就是照抄书本，其实还是没有理解python中关于生成器的机制，所以就理解不了else那一段代码为什么要那样写
```python
def conflict(state, nextX):
    nextY = len(state) # 获取下一个值的行高度
    
    for h in range(nextY):
        print(abs(nextX - state[h]), '====', nextY-h)
        if abs(nextX - state[h]) in (0, nextY - h):
        #if nextX == state[h] or abs(nextX - state[h]) == state[h] - h:
            return True
    return False


def queens(num=8, state=()):
    for pos in range(num):
        #print("pos is %d" % pos)
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result

print(list(queens(4))) #[(1, 3, 0, 2), (2, 0, 3, 1)]
```

## 参考

