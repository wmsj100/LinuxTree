---
title: join
date: Tue 20 Feb 2018 10:35:46 PM CST
tag: [linux,sys,conf]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

# join 

- 会往文件中添加列，
- 将俩个文件中指定栏位相同的行连接起来，即按照俩个文件中共同拥有的某一列，将对应的行拼接成一行。
- 和uniq一样，只能用于排过序的数据
## 参数
- j 指定一个域作为匹配字段
- 1 以f1中的字段进行匹配
- 2 field 以f2中的fileld字段进行匹配
- t 自定义分割符

## 实例
- join -1 3 -2 3 c.txt d.txt 指定俩个文件的第三个字段尾匹配字段。 
- join -t ':' -1 4 /etc/passwd -2 3 /etc/group 
