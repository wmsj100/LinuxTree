---
title: while循环
date: 2019-04-12 18:06:52	
modify: 
tag: [while]
categories: Shell 
author: wmsj100
mail: wmsj100@hotmail.com
---

# while循环

## 概述
- while循环和for类似，都使用关键字`do/done`来组装循环体
- 如果while条件为真，会一直循环，
- while循环必须设置边界值，防止死循环

## 范例
```sh

#!/bin/bash
num=0
while [ $num -lt 5 ]
do
    echo "cur num is $num"
    num=$(expr $num + 1)
done
```

## 参考
- [while循环](http://c.biancheng.net/cpp/view/7008.html)
