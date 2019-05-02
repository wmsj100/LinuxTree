---
title: local 
date: 2019-05-02 08:18:51	
modify: 
tag: [local]
categories: Shell 
author: wmsj100
mail: wmsj100@hotmail.com
---

# local

## 概述
- 限制当前变量是局部变量
- 对变量的修改只在当前函数内有效
- 函数内对全局变量的修改对全局生效

## 范例
- 限制全局变量为局部变量
```sh
a=1
b="wmsj100"
foo(){
        local a="hello world"
        b=12
}
echo "$a, $b" # 1 wmsj100
foo
echo "$a, $b, $c" #1 12
```

## 参考
- []()
