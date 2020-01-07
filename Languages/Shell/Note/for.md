---
title: for循环
date: 2019-04-12 17:58:39	
modify: 
tag: [for]
categories: Shell 
author: wmsj100
mail: wmsj100@hotmail.com
---

# for循环

## 概述
- for循环和其他语言类似，都是进行遍历
- 可以对字符串和数组进行遍历，遍历的元素是通过空格分隔的字符串或数组
- 如果是遍历数组，必须使用`${list[@]} | ${list[*]}` 来遍历数组的所有元素
- 使用关键字`do`开始，`done`结束循环

## 范例
```sh
#!/bin/bash
a=(1 23 45 678)
b="this is a test case"

for num in ${a[*]}
do
    echo "The num is $num"
done

for str in $b
do
    echo "The str is $str"
done
```

## 参考
- [shell for](http://c.biancheng.net/cpp/view/7007.html)
