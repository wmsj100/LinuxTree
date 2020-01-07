---
title: shift
date: 2019-05-02 11:44:07	
modify: 
tag: [shift]
categories: Shell 
author: wmsj100
mail: wmsj100@hotmail.com
---

# shift

## 概述
- shift左移命令，把参数变量左移一个位置，使`$2`变为`$1`,
- `$#`和`#@`也会同时变化
- 在扫描处理脚本的参数时候，进程要用到shift命令

## 范例
while test "$1" != ''
do
        echo $1
        shift
done
exit 0
```

## 参考
- []()
