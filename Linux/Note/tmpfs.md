---
title: tmpfs
date: 2019-05-11 22:34:33 Saturday
modify:
tag: [basic,fs,tmpfs]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

# tmpfs

## 概述
- `tmpfs`是临时文件系统的意思，但它又不是普通的文件系统，因为它不是物理磁盘上的空间，占用的是内存空间，但以物理磁盘分区的方式展示给用户，让用户操作这块空间
- tmpfs不需要用`mkfs`来格式化，这是它与文件系统的区别
- 默认情况下最大占用物理内存的一半空间

## 用法
- 几乎所有程序都会产生临时文件，在硬盘上大量不写临时文件会影响系统性能，于是人们开始把临时文件写入`tmpfs`来提高程序运行性能
- `tmpfs`是`Linux2.4`内核版本引入的全新的文件系统
- 它可以直接使用内存，也可以使用`swap`交换分区
- `tmpfs`使用xu虚拟内存子系统的页面来存储文件，它不管这些页面到底在物理内存还是在交互内存分区中，具体存储位置完全交给虚拟内存管理。
- 这和普通用户进程使用的虚拟内存一样

- `mount tmpfs /tmp -t tmpfs -o 4096M` 挂载临时文件系统到目录，并且指定目录大小

## 范例

## 参考
- [tmpfs临时文件系统](https://blog.csdn.net/tales522/article/details/78756356)

