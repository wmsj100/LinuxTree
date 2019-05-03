---
title: tr 更改字符
date: Wed 21 Feb 2018 11:47:49 AM CST
tag: [linux]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

# tr 更改字符

- 它是基于字符的查找和替换, 把字母从一个字母转换为另一个字母的过程
- 从标准输入中替换/ 缩减/ 删除字符，并将将结果写道标准输出中
- 只能通过stdin，无法通过命令行参数来接收输入
- 是translate的缩写

## 命令格式
- tr [选项] set1 set2

## 参数
- d 删除匹配set1的内容，并不做替换
- s 替换掉重复字符

## 实例
- cat f1 | tr 'a-z' 'A-Z' 将f1文件中的小写字母转换为大写字母
- cat tel | tr -d '0-9' 删除tel文件中的数字
- cat /etc/passwd | tr -d ':' 删除冒号
- echo "asadaf" | tr -s a t // "tstdtf"

- ROT13 是一种简单的替换暗码的加密类型，就是把每个字符在字母表中向前移动13位，再次执行这个算法就可以解密。
	- echo "hello world" | tr 'a-z' 'n-za-m' | tr 'a-z' 'n-za-m' 通过俩次完全一样的命令就可以解密。
