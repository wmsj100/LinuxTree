---
title: test
date: 2019-04-12 17:25:03	
modify: 
tag: [test]
categories: Shell 
author: wmsj100
mail: wmsj100@hotmail.com
---

# test测试

## 概述
- test命令检查某个条件是否成立，可以进行数值/字符/文件三个方面的测试
- test 通常在`if`条件中使用，相当于`if`的中括号的作用

## 数值测试
- eq/gt/lt/ge/le/ne

```shell
#!/bin/bash
a=100
b=200

if test $[a] -eq $[b]
then
    echo 'a is equal b'
else
    echo 'a is not equal b'
fi
```

## 字符串测试
- =/!=/-z/-n

```shell
#!/bin/bash
a='asdf'
b='qwer'

if test $a = $b
then
    echo "a is equal b"
else
    echo "a is not equal b"
fi

if test -z $a
then
    echo "a is zero"
else
    echo "a is not zero"
fi

if test -n $a
then
    echo "a is not empty"
else
    echo 'a is empty'
fi
```



## 参考
- []()
