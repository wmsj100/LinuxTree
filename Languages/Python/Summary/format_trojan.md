---
title: format_trojan
date: 2020-03-23 14:08:18
modify: 
tags: [Summary]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# format_trojan

## 概要

- 这是自己写的一个关于格式化配置文件并且按照要求重新输出文件的脚本

## 代码

```python
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 wmsj100 <wmsj100@UbuntuOS>
#
# Distributed under terms of the MIT license.

"""
格式化trojan的内容到配置文件存储
"""
import json
import sys
import os
import json

def get_template_json(jsonfile):
    result = dict()
    with open(jsonfile, 'r') as file:
        result = file.read()

    return result

def format_data(targetFile, template_str):
    result = dict()
    with open(targetFile, 'r') as file:
        for line in file.readlines():
            template_json = json.loads(template_str)
            struct_dict_from_line(line, result, template_json)
    
    return result

def write_to_file(result, filename):
    with open(filename, 'w') as file:
        file.write(json.dumps(result))


def struct_dict_from_line(line, result, template_json):
    line_list = line.split()
    if len(line_list) != 5:
        line_list.insert(1, 1)
    region = line_list[2]
    template_json["remote_addr"] = region
    cur_dict = {
        "port": line_list[3],
        "flow_rate": line_list[-1],
        "region_name": line_list[0],
        "region": region,
        "region_num": line_list[1],
        "trajon_conf": template_json
    }

    result[region] = cur_dict

def init():
    cur_path = os.path.dirname(os.path.abspath(__file__))
    template_json = dict()
    origin_file = "trojan.data"
    target_file = "trojan.json"
    default_json = os.path.join(cur_path, origin_file)
    struct_file = ''

    if (len(sys.argv) <= 1):
        print("Please input shadowstack.data for arguments")
        return False

    struct_file = os.path.join(cur_path, sys.argv[1])
    if not os.path.isfile(struct_file):
        print("Please make sure {} is exist".format(struct_file))
        return False

    if not os.path.isfile(default_json):
        print("Please make {} is exist".format(default_json))
        return False

    template_str = get_template_json(default_json)
    result = format_data(struct_file, template_str)
    write_to_file(result, target_file)

if __name__ == '__main__':
    init()
```

## 参考

