---
title: iconv语言编码转换
date: Mon 19 Feb 2018 12:04:06 PM CST
tag: [linux]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

- iconv 可以进行语系编码转换
    - f from 原来的编码格式化
    - t to 新编码的格式
    - o 后面的文件是新编码的文件名
- iconv -f big5 -t utf8 vi.big5 -o vi.utf8  把vi.big5从big5编码转换为utf8并且存储为vi.utf8

- 转换后可以通过file命令来查看文件的格式
