---
title: xargs参数代换
date: Wed 21 Feb 2018 09:41:03 PM CST
tag: [linux]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

# xargs 参数代换

- 有些命令只能以命令行参数的形式接收数据，而无法通过stdin接收数据流，在这种情况下，无法通过管道将数据重定向给命令

- xargs命令可以从标准输入接收数据，并把输入转换为一个特定的参数列表

- xargs命令应该紧跟在管道操作符后面，因为它以标准输入作为主要的源数据流

## 参数
- n 指定每行最大的参数数量
- d 指定分割符
- p 在执行每个命令参数时都会询问用户
- e end of file 后面接一个字符，当xargs分析到这个字符串时候就停止

## 范例
- cat a.txt | xargs 将多行输入转换为单行输出
- echo "1 2 3 4 5 6" | xargs -n 3 将单行输入转换为多行输出
- echo "1i2i3i4i5i6i" | xargs -d i -n 3 将i作为分割符输出多行
- find . -name "f1" | xargs wc -l 寻找f1文件，如果找到多个，则计算出每个文件的行数。
- ls | xargs wc -l
- 找出/sbin下面具有特殊权限的文件名，并使用ls -l 列出详细属性
    - find /sbin -perm /7000 | xargs ls -l
    - find /sbin -perm /7000 | ls -l 这样只会列出当前目录的详情，错误
