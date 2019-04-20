---
title: declare声明变量类型
date: Tue 20 Feb 2018 12:13:21 PM CST
tag: [linux]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

- declare 类似于`typeset` 声明变量类型。
- 后面没有接任何参数,那么bash就会主动将所有的变量调出来，就像使用`set`一样。
    - declare -a var 将变量var定义为数组array类型
    - declare -i var 将变量定义为整数integer类型
    - declare -x var 与export类似，将变量转为环境变量
    - declare +x var 可以把环境变量var转换为自定义变量
    - declare -r var 将变量设置为readonly类型，变量不可重设或修改
    - declare -p var 显示变量var的类型详情

## 范例
- 整数类型
    - sum=12+2-1 默认声明的时文字类型
    - echo $sum / 12+2-1
    - declare -i sum=12+2-1 声明为整数类型参与计算
    - echo $sum / 11
- 导出环境变量
    - declare -x sum
    - export | grep sum // declare -ix sum="11"
- 设置数组变量
    - a[1]="asdf"
    - declare -p a // declare -a a='([0]="3.10.0-693.17.1.el7.x86_64" [1]="adsf")'
    - echo ${a[1]} // "adsf"
