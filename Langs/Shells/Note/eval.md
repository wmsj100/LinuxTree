---
title: eval
date: 2019-05-02 09:26:27	
modify: 
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

## 范例
- 生成变量
```sh
a=10
b=a
eval y='$'$b
echo $y
```

## 参考
- []()
