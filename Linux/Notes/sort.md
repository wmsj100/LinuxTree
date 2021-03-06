---
title: sort
date: 2020-03-12 11:36:27 
modify: 2020-11-30 17:02:29  
tags: [basic]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# sort 排序

## 参数

- n 根据数字值排序
- k 指定排序关键字
- b 默认情况下，从每行的第一个字符开始，这个选项将忽略开头的空白，从第一个非空白字符开始排序
- m 合并多个输入文件
- r 按相反顺序排序
- t 自定义分割符，默认为制表符

## 实例

- du -s /usr/share/* | sort -nr | head -10 获取share文件夹内占用空间最大的前10个文件
- ll | sort -nr -k 5 | head -10  对ll的详情按照文件大小从大到小顺序排序。打印前10个  
- `cat luna_pinyin_export.txt | awk -F ' ' '{print $1"\ " $NF}' | sort -nr -k 2| less` 按照空格拆分取第一列和最后一列，然后以最后一列的数值逆序排列

'''data.txt
a  5 20/10/2014
a  11 28/09/2014
b  2 01/12/2014
c  7 18/10/2014
'''

- sort -k 1,1 -k 2n data.txt  第一个字符按照字符排序，如果相同，第二个字符按照数字大小排序。
	- 第一个k指明只对第一个字段排序，1，1意味着始于并且结束于第一个字段。
	- 第二个k选项2n表示对第二个字段按数值排序

- sort -k 3.4nb data.txt 按照第3个字段的第4个字符顺序排序
	- 3.4 表示始于第3个字段的第4个字符，按照数值排序。
- `cat ~/Document/test1.dic | sort -k 3 -nr | less` 查看test文件,按照第3个字段数字从大到小排序导入到less管道
