#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019  <@wmsj100>
#
# Distributed under terms of the MIT license.

"""
实现阶乘的俩种方法
"""

def fn(n):
    result = 0
    if n == 1:
        result = 1
    else:
        result = n * fn(n-1)
    return result


def fn1(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

print fn(10) # 3628800
print fn1(10) # 3628800
