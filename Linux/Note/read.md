---
title: read
date: 2019-05-10 00:00:34 Friday
modify:
tag: [read]
categories: pi/Github/LinuxTree/Langs/C
author: wmsj100
mail: wmsj100@hotmail.com
---

# read

## 概述
- 从文件描述符`fildes`相关联的文件中读入`nbytes`个字节的数据，并且把它们放到数据区`buf`中
- 也就是从文件中读取数据到内存中

## 用法
- `size_t read(int fildes, void *buf, size_t nbytes)`
- `buf`表示要接收读取到的内容
- 读取成功会返回实际读入的字节数，
- 如果返回`0`表示未读入任何数据
- 返回`-1`表示读入报错

## 范例
- 从标准输入读取数据
```c
#include<stdlib.h>
#include<unistd.h>
#include<stdio.h>

int main()
{
	char buffer[128];
	int nread;
	nread = read(0, buffer, 128);
	printf("nread is %d", nread);
	if(nread == -1)
	{
		write(2, "A read error occured\n", 26);
	}

	if((write(1, buffer, nread)) != nread)
	{
		write(2, "A write error has occured\n", 27);
	}
	exit(0);
}
//echo "hello there" | ./t2 #这样进行调用
```

## 参考
- []()

