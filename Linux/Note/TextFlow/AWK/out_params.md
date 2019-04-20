---
title: awk获取外部变量
date: 2018-03-12 22:21:28 Mon
tag: [awk]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

# awk 获取外部变量

## BEGIN && END
- 在awk中有俩个特别的表达式，`BEGIN`, `END`，作用是给程序赋予初始状态和在程序结束后执行一些扫尾工作。
- 任何在BEGIN之后列出的操作(在{}内)将在awk开始扫描输入之前执行；
- 任何在END之后列出的操作在扫描全部的输入之后执行。
- 通常使用BEGIN来显示变量和预置变量
- 使用END来输出最终结果

## awk '{action}' 变量名=变量值
- test="awk test"
- echo | awk '{print test}' test="$tes" // "awk test"

## BEGIN程序块中变量
- awk -v 变量名=变量值 'BEGIN{action}'
- 用'-v'传入变量在三种类型的action中都可以获取

### 范例
- test="awk test"
- name="wmsj100"
- echo | awk -v test="$test" -v name="$name" 'BEGIN{print test,name}'
- echo | awk -v test="$test" -v name="$name" '{print test,name}'
- echo | awk -v test="$test" -v name="$name" 'END{print test,name}'

## 获取环境变量
- 只需要调用awk的内置变量`ENVIRON`，就可以直接获取环境变量，它是一个字典数组，

### 范例
- export name="wmsj100"
- awk '{print ENVIRON["name"]}'
- awk 'BEGIN{for（i in ENVIRON) {print i"="ENVIRON[i]}}'
