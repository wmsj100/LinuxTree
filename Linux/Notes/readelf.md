---
title: readelf
date: 2020-04-13 12:19:30
modify: 2020-06-22 18:00:08 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# readelf

## 概要

- ELF Executable and Linking Format
- 定义了目标文件内部信息如何组成和组织的文件格式。
- 内核会根据这些信息加载可执行文件，内核根据这些信息可以知道从文件哪里获取代码，从哪里获取初始化数据，在哪里应该加载共享库
- `apt install binutils` 该软件是gun的工具包的一个工具，需要通过这种方式来安装

```
[root@ecs0005 lib64]# readelf -h libstdc++.so.6.0.19
ELF Header:
  Magic:   7f 45 4c 46 02 01 01 03 00 00 00 00 00 00 00 00
  Class:                             ELF64
  Data:                              2's complement, little endian
  Version:                           1 (current)
  OS/ABI:                            UNIX - GNU
  ABI Version:                       0
  Type:                              DYN (Shared object file)
  Machine:                           AArch64
  Version:                           0x1
  Entry point address:               0x5bdd0
  Start of program headers:          64 (bytes into file)
  Start of section headers:          1055272 (bytes into file)
  Flags:                             0x0
  Size of this header:               64 (bytes)
  Size of program headers:           56 (bytes)
  Number of program headers:         8
  Size of section headers:           64 (bytes)
  Number of section headers:         32
  Section header string table index: 31
```

- Class/Type/Machine可以知道该文件在AArch64上面。
- Entry point address: 知道当该程序启动时从虚拟地址的0x5bdd0开始运行。
	- 这个不是main函数的地址，而是_start函数的地址
	- _start由链接器创建，_start是为了初始化程序。
	- `objdump -d -j -.text libstdc++.so.6` 可以查看该库的_start函数
- Number of program headers: 知道该程序有8个段
- Number os section headers: 知道该程序由32个区
	- 区中存储的信息是用来链接使用的，主要包括:程序代码、程序数据(变量),重定向信息等。
	- Code section: 保存的是代码
	- data section: 保存的是初始化或未初始化的数据

## 参考

- [readelf 解析](https://blog.csdn.net/Linux_ever/article/details/78210089)
