---
title: 字符串操作
date: Sat 30 Dec 2017 06:06:07 PM CST
modify: 2020-02-05 17:49:57 
tag: [python]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

## 概述

- `'''`这样可以接上字符串
- `r'asdf\ae\nasdf'` 原始字符串，反斜杠不会被转移,原始字符串最后一个值不能是反斜杠，除非对反斜杠转义
- `u'你好'` Unicode字符串，使用u做前缀
- repr/str 输出字符串

## 常用方法

- str.ljust(35, '-') 字符串左对齐，长度为35，并且填充符为'-'
- str.rjust(35, '-')
- str.center(35, '-')
- str.startswith('a') 字符串是否以a开头
- str.endswith('a') 字符串是否以a结尾，返回布尔值
- title 返回首字母大写
- upper 字母转换为大写
- lower 全部转为小写
- swapcase 大小写转换
- str.strip('-') 去除左右'-'，如果不指定，默认是去除空格
- str.lstrip()
- str.rstrip()
- isalnum 全部是字母和数字，
- isalpha 全部为字母
- split 分割字符串，默认的分割符是空格
- join 用制定的符号连接列表，
    - join 不是列表的方法，只有字符串有这个方法，
    - '-'.join("shi yan lou".split())
- strip 剥离字符串，可以有一个参数，这个参数表示剥离的字符
    - "shi yan lou".strip('his '); // "yan lou"
    - 表示剥离字符'h'/'i', 's', ' '
- lstrip 剥离字符串左边的值
- rstrip 剥离字符串右边的值
- find 查找字符出现的位置 `a.find('ou'); /12
    - 没有找到就返回‘-1’
    - 类似与 a.index('a')
- startwith 检查字符串是否以指定的字符开始；`a.startwith('shi'); // True
- a[::-1] 反转字符
- len 获取字符长度
- str() 返回字符串
- repr() 等效于str

- print(r"\nasdf") 输出原始字符串，这时候反斜杠不会被当做转义字符进行处理，原始字符是以小写字母'r'开头的。
---

- raw_input python3中并没有这个方法，所以不建议使用，它只是把所有用户输入的值转换为字符串而以。建议使用input代替

---

## 格式化输出

- 字符串格式化使用'%'，这是早期的方法，现在推出了`format`
- 
