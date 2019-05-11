---
title: write
date: 2019-05-09 23:47:59 Thursday
modify:
tag: [write]
categories: pi/Github/LinuxTree/Langs/C
author: wmsj100
mail: wmsj100@hotmail.com
---

# write

## 概述
- 用来写入文件内容的底层系统调用函数
- 只要涉及到写操作的命令底层调用的都是write方法
- 比如`cp,mv,scp`

## 用法
- `size_t write(int fildes, const void *buf, size_t nbytes);`
- 系统调用`write`的作用是把缓冲区`buf`的前`nbytes`个字节写入文件描述符`fildes`关联的文件中
- 它返回实际写入的字节数。
- 如果文件描述符有错或者底层的设备驱动程序对数据块长度比较敏感，该返回值可能小于`nbytes`
- 如果返回**0**表示没有写入任何数据
- 如果返回`-1`，表示调用中出现了错误，
## 范例
- 写入到标准输出
```c
#include<unistd.h>
#include<stdlib.h>
#include<stdio.h>


int main()
{
	int a=0;
	a=write(1, "Here is some data\n", 18);
	printf("a is %d\n", a);
	exit(0);
}
```

## 参考
- []()

