---
title: case
date: 2019-04-12 17:48:34	
modify: 
tag: [case]
categories: Shell 
author: wmsj100
mail: wmsj100@hotmail.com
---

# case

## 概述
- case 类似其他语言中的`switch case`
- 必须有关键字`in`
- 判断条件使用圆括号分隔
- 条件结束使用俩个分号`;;`
- `*` 使用这个字符匹配无法匹配的条件
- case可以对判断条件进行合并匹配模式 `y|Y|yes|YES)`
- case的条件中也可以执行多条命令，需要把俩个分号换行
- case 还可以进行可选字符匹配判断 `[Yy][Ee][Ss]`

```sh
#!/bin/bash
read num

case $num in
    1)  echo "select 1"
        ;;
    2)  echo "select 2"
        ;;
    3)  echo "select 3"
        ;;
    *)  echo "not gass"
        ;;
esac
```

- 合并模式范例
```sh
echo "input yes/no for curtime"
read curtime
case $curtime in
    y|Y|yes|YES) echo "morning";;
    n*|N*) echo "afternoon";;
    *) echo "error input";;
esac
exit 0
```

- case 执行多命令
```sh
echo "yes/no fro curtime"
read curtime
case "$curtime" in
    y | yes | Y| Yes )
        echo "curtime time is morning"
        echo "Up bright and early this morning"
        ;;
    N* | n* )
        echo "Good Afternoon"
        ;;
    * )
        echo "Sorry, answer is not recognized"
        echo "Please anser yes or not"
        exit 1
        ;;
esac
exit 0
```

- case 可选字符判断
```sh
echo "yes/no for curtime"
read curtime
case "$curtime" in
    [Yy] | [Yy][Ee][Ss] )
        echo "Good morning"
        echo "bright sunshine"
        ;;
    [Nn] | [Nn][Oo][Tt] )
        echo "afternoon"
        echo "night is will come"
        ;;
    * )
        echo "Sorry, error input"
        echo "please input yes/no"
        exit 1
esac
exit 0
```

## 参考
- [shell case](http://c.biancheng.net/cpp/view/7006.html)
