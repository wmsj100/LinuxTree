#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019  <@wmsj100>
#
# Distributed under terms of the MIT license.

"""
幂计算
"""
def mi(n, m):
    result = 1
    for i in range(m):
        result *= n
    return result

def mi1(n, m):
    result = 1
    if m == 0:
        result = 1
    else:
        result = n * mi1(n, m-1)
    return result

print mi(2, 8) # 256
print mi1(2, 8) # 256
