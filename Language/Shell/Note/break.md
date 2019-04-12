---
title: break & continue
date: 2019-04-12 19:35:13	
modify: 
tag: [basic]
categories: Shell 
author: wmsj100
mail: wmsj100@hotmail.com
---

# break & contine

## 概述
- break 跳出循环，和其他语言类似
- break num 表示跳出几层循环
- continue 表示跳过当前循环

## 范例
```shell
#!/bin/bash

for val1 in 1 2 3
do
    for val2 in 5 6 7
    do
        if test $val1 -eq 2 -a $val2 -eq 6
        then
            break 2
        fi
        echo $val1,$val2
    done
done
```

## 参考
- [break](http://c.biancheng.net/cpp/view/7010.html)
