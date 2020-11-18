---
title: code_confuse
date: 2020-11-18 17:15:53
modify: 
tags: [Libs]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# code_confuse

## 概要

- 代码混淆工具

## Intensio-Obfuscator

- https://github.com/Hnfull/Intensio-Obfuscator.git
- 一个代码混淆工具，混淆级别可以自己调整，可以做代码变量的字符串替换，替换机制可以做str转换的长度，24、48等
- 还可以转换文件名为随机值
- 可以把所有代码转换为hex值，这样转过的文件完全不可读。

### 使用

- `python intensio_obfuscator.py -i webapp/ -o dist/ -mlen lower -ind 2 -rts`
- `python intensio_obfuscator -h` 查看帮助

## 参考

