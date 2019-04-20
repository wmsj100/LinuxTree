---
title: paste 添加一个或多个文本到文件 
date: Tue 20 Feb 2018 10:35:46 PM CST
tag: [linux]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

#paste 添加一个或多个文本到文件中

- 与cut命令正好相反，它会添加一个或多个文本到文件中，而不是从文件中抽取文件，然后把文件值中的字段整合成单个文本流，输入到标准输出。

## 参数
- s 将每个文件合并成行而不是按行粘贴
- d 自定义分割符，默认为制表符
- - 代表stdin

## 实例
- paste f1 f2 按照每一行拼接俩个文件
- paste -d ':' f1 f2 按照：把俩个文件在每一行连接起来
- paste -s f1 f2 将俩个文件各自拼接为一行  总共是俩行内容
- cat /etc/group | paste /etc/passwd /etc/shadow - | head -n 3
