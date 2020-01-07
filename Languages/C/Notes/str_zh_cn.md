---
title: 中文
date: 2019-04-15 20:28:55	
modify: 
tag: [string]
categories: C
author: wmsj100
mail: wmsj100@hotmail.com
---

# 中文

## 概述
- 中文占用的字节2~4，用`char`不能表示
- 对于汉语/日语/韩语等要使用宽字符的编码方式。
- 常见的宽字符编码有'UTF-16'和'UTF-32'，他们都是基于`Unicode`字符集的，能够支持全球语言

## wchar_t
- 宽字符使用这个关键字定义，表示wide char type;
- wchar_t类型位于`<wchar.h>`头文件中，它使代码具有良好的移植性;
- `L`: 字符前加上L表示宽字符； `wchar_t a = L'A'`

## 宽字符串
- wchar_t a[]
- wchar_t *b  \*
## 输出
- putwchar/wprintf
- setlocale(LC_ALL, "zh_CN"): 宽字符在输出之前需要向使用这个函数进行本地化
- setlocale位于`<locale.h>`头文件中
- 通常不会这样设置，因为不会安装额外的字符集
- wprintf(L"%lc %lc", a,b);
## 参考
- [字符](http://c.biancheng.net/cpp/html/3424.html)
