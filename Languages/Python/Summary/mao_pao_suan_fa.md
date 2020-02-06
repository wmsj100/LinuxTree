---
title: 冒泡算法 
date: 2020-02-06 20:55:54
modify: 
tags: [Summary]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# 冒泡算法 

## 概要

- 这算是比较基础的算法了，这个算法之前没有接触过，但听他们说过，我从没有自己实现过。
- 我是今天下午开始弄这个算法，后来就转移注意力了，然后又回来搞，最后弄出来了，

## 规则

1 比较相邻的元素，如果第一个比第二个大，就交互位置
2 从最开始的第一对到结尾的最后一对，对每一对相邻元素做步骤1所描述的比较工作，并将最大的元素放在后面。这样，当从最开始的第一对到结尾的最后一对都执行完成后，整个序列中的最后一个元素便是最大的数
3 将循环缩短，除去最后一个数(因为最后一个已经是最大的了)，再重复上面的步骤2，得到倒数第二大的数
4 持续做步骤3的操作，每次将循环缩短一位，并得到本次循环中的最大数。知道循环个数缩短为1，即没有任何一对数字需要比较，此时便得到一个从小到大排序的序列。

## 我的代码实现

- 没有考虑缩短循环次数
- 其实我有想到再循环过程中动态修改list的长度，然后把最后一个值pop出来，这样下一次循环时候list本身就便小了。
- js是可以这样动态修改循环中的list的，但是python是不可以的，我试过，仍然是以最开始的list长度循环的，
- 所以就放弃了这样动态修改list的想法了，就是简单的执行俩次循环，
- 其实我有想到再执行第二层次的循环时候应该减去2
```python
def sort_max_list(list):
    for index, num in enumerate(list):
        if index == len(list) - 1:
            break
        else:
            if num > list[index+1]:
                list[index], list[index + 1] = list[index+1], num
        print(list)

def sort_list(list):
    result = []
    for index in range(len(list) - 1):
        sort_max_list(list)
```

## 标准写法

- 再循环时候会逐渐缩短循环次数
```python
def mao_pao(list):
    for i in range(len(list) -1):
        for j in range(len(list) - i - 1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
            print(list)
```

## 参考

- [python冒泡排序](http://c.biancheng.net/view/vip_6006.html)
