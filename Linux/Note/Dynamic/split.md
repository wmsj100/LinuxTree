---
title: split
date: Wed 21 Feb 2018 09:41:03 PM CST
tag: [linux]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

## 基本概念
- split 切割文件
    - b 按照文件大小b,k,m切割文件
    - l 按照行数切割文件
- split [-bl] file prefix

### 合并文件
- 切割后的文件如何合并呢？
- 利用cat读入切割文件然后重定向生成完整文件
- cat file_split_* >> file_split 

## 範例
- split -b 300k file file_split_ 按照300k大小切割文件，文件的前缀名称为file_prefix
- ll -a | split -l 10 - lsroot 输出信息每10行记录成一个文件，
