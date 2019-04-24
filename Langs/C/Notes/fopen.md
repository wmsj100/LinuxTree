---
title: fopen
date: 2019-04-24 22:16:06	
modify: 
tag: [file,basic]
categories: C
author: wmsj100
mail: wmsj100@hotmail.com
---

# fopen

## 概述
- 打开文件，返回一个`FILE`结构体
- 搭配`fclose(fp)`来关闭文件

## 文件打开模式
- r 只读 文件必须存在
- r+ 读写，文件必须存在
- w/w+ 只写，文件不存在就创建，覆盖写
- a/a+ 追加写，文件不存在就创建
- b 以二进制方式打开文件
- t 以文本形式打开文件

## 参考
- []()
