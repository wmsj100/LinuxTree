---
title: cat查看文件
date: 2018-02-07
tag: [linux]
categories: Linux
---

#查看文件

- cat命令的功能是将文件或标准输入组合输出到标准输出。
- 常用来显示文件内容，或者是将几个文件连接起来显示，或者是从标准输入中读取内容并显示，常常搭配重定向符号配合使用。
	- A --show-all 显示所有符号
	- b --number-nomblank 对非空输出行编号
	- n --number 对输出的所有行编号，
	- s 有连续俩行以行的空白行，就代换为以行空白行

'''shell
cat -A << EOF
> 'ls -l'
> EOF
'''

- cat -n file 查看文件，并显示行号，
- date | cat /dev/stdin > f3  这样就可以把输入到屏幕的时间存储到文件f3
- tac 逆序显示文件

- head/tail 只显示头/尾10行
- tail -n 1 /etc/passwd 显示最后一行文件

- tail -f 这个参数可以实现不停的读取某个文件的内容并显示，这可以让我们动态查看日志，达到实时监视的目的。

- file finename/directoryname 查看文件类型，可以是文件/目录/链接/可执行文件

- linux不是通过后缀来识别文件类型的，文件类型是通过“file”来查看的。

- cat /dev/stdin  读取标准输入流的数据,

- paste f1 f2 | cat -A /dev/stdin 这样就通过屏幕打印出来了标准输入流的内容。
- cat > h1   会在界面输入内容，直到按下 ctrl + d   结束输入，
- cat h1 h2 > h3 把h1, h2俩个文件的内容输入到文件h3中

## cat make 
- cat ~/Download/ubanto.iso >> /dev/sdb4
- [make u pan](https://blog.csdn.net/longerzone/article/details/12941727)
