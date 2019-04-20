#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019  <@wmsj100>
#
# Distributed under terms of the MIT license.

"""
date: 2019-04-09 16:49:49 
desc: 自动填充，这个的使用场景是搜索引擎的搜索框，在输入值的时候动态回显推荐值，
- 我之前在做前端时候也有碰到这种场景，当时是对于列表一把查询回来，然后通过浏览器处理存储到本地，然后再列表的搜索框输入值的时候动态显示，
- 这种情景只适用于少量数据，而且对于列表必须一次把所有值全部查询回来，如果列表是按照分页触发的，其实这种自动回显的意义就大打折扣了，因为只能显示当前分页有的值，
- 如果数据量很大的时候就需要通过后台来处理了，需要重新创建一张表，再服务器不忙碌的时候来执行这样的操作，
- 现在真实的场景也确实是这样做的，只不过添加了纠错/汉字拼音这样的转换功能。
- 而且推荐值是有限制的，比如只显示10个或者15个，可以添加判断，如果len(dict[key]) > 10 就不再处理了
- 用集合的好处是可以保证集合中的值没有重复的，不需要进行判断当前值是否已经再集合中
- 这种处理思路的核心就是用空间换时间，因为当前存储的价格远低于实时计算所耗费的电力
"""
query_log = ['alice', 'any', 'alias', 'bob',
             'bomb', 'bill', 'there', 'their', 'them']

dict = {}
for word in query_log:
    for i in range(1, len(word) + 1):
        key = word[0:i]
        if key not in dict:
            dict[key] = set([])
        dict[key].add(word)
print dict.keys()

while True:
    value = raw_input("\n")
    if value == 'exit':
        break
    else:
        if value in dict:
            print dict[value]

