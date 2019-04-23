---
title: until循环
date: 2019-04-12 18:14:45	
modify: 
tag: [until]
categories: Shell 
author: wmsj100
mail: wmsj100@hotmail.com
---

# until循环

## 概述
- until循环和while循环类似，只不过和while相反
- until判断条件为假，则继续循环，否则跳出循环
- 使用关键字`do/done`包裹循环体

## 范例
```sh
#!/bin/bash
num=0

until [ ! $num -lt 10 ]
do
    echo "cur num is $num"
    if test $num -lt 1
    then
        num=`expr $num + 1`
    else
        num=`expr $num \* 2`
    fi
done
echo "complete"
```

## 参考
- [until](http://c.biancheng.net/cpp/view/7009.html)
