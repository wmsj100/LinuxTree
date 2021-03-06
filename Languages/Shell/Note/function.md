---
title: 函数 
date: Tue 05 Dec 2017 11:23:15 PM CST
modify: 2020-06-01 21:13:32 
tag: [shell, function]
categories: Shell
author: wmsj100
mail: wmsj100@hotmail.com
---

## 概述

- 函数定义好之后调用只需要输入函数名就可以，不需要加括号。
- 函数的返回值可以通过'$?'来获取
- 所有函数在使用前必须先定义
- 调用函数时候可以传入参数，在函数内部，可以通过'$1, $2'来分别获取第1个和第2个参数。
- 如果参数超过9个过去参数需要使用`${10}`
- 函数的返回值只能是数值，通常0表示运行正常，其他值表示对应的异常
- 如果要函数返回字符串或其他值，可以先定义对应的变量来接收值，最后再返回值
- 函数定义可以直接写函数名，也可以通过关键字`function`来显示标识
- 函数内部如果没有显示的`return`值，那么就返回最后一条结果，如果结果不为数值，则返回0，所以推荐函数内部显示`return`
- 函数如果带参数，对于参数运算的结果需要通过外部参数来接收，或者函数直接`return`运算表达式，函数的运算结果通过`echo $?`接受

## 判断函数是否定义

```
if [ "$(type -t hello)" = "function" ];then 
	echo "hello is function"
fi
```

## 带参数函数

- 函数参数获取和脚本参数获取一致，通过$0 $1 $# $*
- $# 获取参数个数
- $* 获取所有参数
- $@ 获取所有参数

## 范例

- 不带参数
```sh
#!/bin/bash

add(){
    read num1 #过去键盘输入
    read num2
    return `expr $num1 + $num2`
}
add
echo $?
submit(){
    return $(($num1-$num2))
}
submit
echo $?

chen(){
    i=1
    sum=0
    while test $i -le $num2
    do
        i=`expr $i + 1`
        sum=`expr $sum + $num1`
    done
    return $sum
}
chen
echo $?
```

- 函数带参数，且接受运算结果
```sh
data=0
bar(){
    data=`expr $1 + $2`
    return 0
}

foo(){
    read num1
    read num2
    return $((num1 * num2))
}
bar 3 5
echo $data
foo
a=$?
echo $a
```
