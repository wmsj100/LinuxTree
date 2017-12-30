---
title: 字符串操作
date: Sat 30 Dec 2017 06:06:07 PM CST
tag: [python]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

- title 返回首字母大写
- upper 字母转换为大写
- lower 全部转为小写
- swapcase 大小写转换
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
