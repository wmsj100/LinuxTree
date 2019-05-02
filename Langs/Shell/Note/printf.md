---
title: printf
date: 2019-05-02 10:10:21	
modify: 
tag: [basic]
categories: Shell 
author: wmsj100
mail: wmsj100@hotmail.com
---

# printf

## 概述
- 这是最新版本的命令，目标是用它来替换`echo`，当时现在很少人使用
- 和`C/C++`中的命令类似，都是用来格式化输出
- `%s`: 字符串
- `%d`: 整数，shell中支持整数，不支持浮点数
- `%c`: 字符
- `%%`: 输出%

## 范例
```sh
printf "the string is %s\nthe num is %d" "hello world" $((1+21))
```

## 参考
- []()
