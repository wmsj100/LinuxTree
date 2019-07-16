---
title: eval
date: 2019-05-02 09:26:27	
modify: 2019-07-16 23:26:41 Tuesday	
tag: [eval]
categories: Shell 
author: wmsj100
mail: wmsj100@hotmail.com
---

# eval

## 概述
- eval命令允许对参数进行求值，
- 是shell内置命令，
- eval命令有点像额外的`$`
- 它允许代码随时生成和运行
- eval在运行时会把`$`开头的变量全部替换成值
- eval的经典使用是在变量嵌套的过程中使用
- `eval b=$(echo \$$a)`

## 范例
- 生成变量
```sh
a=10
b=a
eval y='$'$b
echo $y
```

## 参考
- [eval嵌套使用](https://blog.csdn.net/u010154760/article/details/46051893)
