---
title: exec
date: 2019-05-02 09:38:37	
modify: 
tag: [exec,func,basic,linux]
categories: Shell
author: wmsj100
mail: wmsj100@hotmail.com
---

# exec

## 概述
- 将当前shel替换成一个不同的程序
- exec后面的代码都不会被执行

## 范例
- 将当前shell替换成wall程序，wall程序是一个广播程序
```shell
echo "hello"
exec wall "this is a broadcase"
echo "exit over" # 该命令不会被执行，shell程序已经被切换成wall了，
```

## 参考
- []()
