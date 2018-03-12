---
title: awk字符串连接操作
date: 2018-03-12 23:23:26 Mon
tag: [awk]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

# awk数值转换

## 字符串转换为数字 +
- + 只需要将变量用‘+’连接，自动强制把字符串转化为数字进行运算

### 范例
- awk 'BEGIN{a="100";b=2;print a+b}' // 102

## 数值转换为字符串
- “” 只需要将变量与“”符号连接起来运算即可

### 范例
- awk 'BEGIN{a=1;b=2;print(a""b)}' // ab
