---
title: awk
date: 2020-02-26 20:34:55
modify: 2020-11-26 16:59:49  
tags: [Note]
categories: Shell
author: wmsj100
email: wmsj100@hotmail.com
---

# awk

## 概要

- 排版工具

## 参数

- `$NF` 获取最后一列
- `NF` 获取列数

## 常用命令

- `grep -nrw 'blog' . | awk -F ':' '{print $1}'` 找出所有包含blog的文件，并且按照分隔符':'打印第一列。
- `grep -nrw 'blog' . | awk -F ':' '{print $1} | sort | uniq`
- `sed -i 's/blog/yiqin/g'  `grep -rw 'blog' | awk -F ':' '{print $1}' | sort | uniq`` 去重并且用sed进行替换
- `echo $a | awk -F ' ' '{print $(NF-1)}'` 获取倒数第二列
- `awk '!/^#/ { if ($4 == 1) print $1 }' /proc/cgroups` 打印/proc/cgroups文件中排除`#`开头的文件并且第四列等于1的第一列

## 参考

