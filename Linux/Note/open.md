---
title: open
date: 2019-05-10 00:59:12 Friday
modify:
tag: [open]
categories: C
author: wmsj100
mail: wmsj100@hotmail.com
---

# open

## 概述
- open会创建一个新的文件描述符
- open建立一条到文件或设备的访问路径
- 如果调用成功，它将返回一个可以被`read/write`的文件描述符。
- 这个文件描述符是唯一的，不会与任何运行总的进程共享
- 如果俩个程序同时打开同一个文件，它们会分别得到俩个不同的文件描述符
- 如果它们都对文件进行写操作，那么它们各写各的，分别接着上次离开的位置继续写，数据不会交织在一起，而是彼此互相覆盖
- 俩个程序对文件的读写文件偏移值不同。
- 可以通过使用文件锁功能来防止出现冲突

## 用法
- int open(const char *path, int oflags);
- int open(const char *path, int oflags, mode_t mode);
- open调用成功时返回一个新的文件描述符(一个非负数)，在失败时返回`-1`，
- 新文件描述符总是使用未用的描述符的最小值。
- 这个特征在某些情况下非常有用，如果一个程序关闭了它的标准输出，然后再次调用open，文件描述符1就会被重新使用，并且标准输出将被有效的重定向到另一个文件或设备。

## 范例
- 一个文件复制的范例
```c
#include<unistd.h>
#include<stdlib.h>
#include<stdio.h>
#include<fcntl.h>
#include<sys/stat.h>

int main()
{
	char c[20];
	int in, out;
	in = open("file.in", O_RDONLY);
	out = open("file.out", O_WRONLY|O_CREAT, S_IRUSR|S_IWUSR);
	printf("num is %d %d\n", in, out);
	int num = read(in, &c,10);
	printf("read num is %d char is %s\n", num, c);
	int num2=write(out, &c, num);
	printf("write num is %d\n", num2);

	exit(0);
}
```
## 参考
- []()

