#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019  <@wmsj100>
#
# Distributed under terms of the MIT license.

"""
python 基础教程 page 96
"""

def lookup(data, label, name):
    return data[label].get(name)

def store(data, full_name):
    names = full_name.split()
    if len(names) == 2: names.insert(1, '')
    labels = 'first', 'middle', 'last'
    for label, name in zip(labels, names):
        people = lookup(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]

def init(data):
    labels = 'first', 'middle', 'last'
    for label in labels:
        data[label] = {}

MyNames={}
init(MyNames)
store(MyNames, 'wang hao')
store(MyNames, 'wang qiang')
store(MyNames, 'zhang bao')
print lookup(MyNames, 'first', 'zhang') # ['zhang bao']
