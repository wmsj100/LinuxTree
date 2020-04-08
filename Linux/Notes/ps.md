---
title: ps
date: 2019-05-11 22:56:35 Saturday
modify: 2020-04-08 11:23:44 
tag: [basic,ps]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

# ps

## 概述

- ps为我们提供了进程的一次性的查看，它所提供的查看结果并不动态连续；
- 如果想对进程长时间监控，应该用top工具。
- 通常ps结合grep来使用

## 用法

- ps aux 查看详细进程，罗列所有的进程信息
- ps axjf 查看进程时连同进程树显示出来
- ps -l 显示当前bash相关的进程
- pstree 查看进程的相关性
	- pstree -up 同时逻辑出进程的账户名称和PID

## ps aux 解释

```
[root@87283aa8325b /]# ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0   9280  6272 ?        Ss   Apr07   0:00 /usr/lib/systemd/systemd --system --deserialize 17
root        77  0.0  0.0   5312  1728 ?        Ss   Apr07   0:00 /usr/lib/systemd/systemd-logind
```
- USER: 进程拥有者
- PID: pid
- %CPU: 占用cpu使用率
- %MEM: 占用内存使用率
- VSZ: 占用虚拟内存大小
- RSS: 该进程占用的固定内存量(KB)驻留中页的数量
- TTY: 终端的次要装置号码
- STAT: 进程的状态
	- D: 不可中断(通常IO的进程)
	- R: 正在运行中在队列中可执行的
	- S: sleeping
	- T: 停止或被追踪 traced or stopped
	- Z: 僵死
	- <: 优先级高的进程
	- N: 优先级较低的进程
	- L: 有些页被锁进内存
	- s: 进程的领导者(在它之下有子进程)
	- l: 多线程，克隆线程
	- +: 位于后台的进程组
- TIME: 执行时间
- COMMAND: 所执行的指令

## 参考

- [ps 解析](https://blog.csdn.net/WuLex/article/details/88775232)
- [ps 讲解](https://www.cnblogs.com/mydriverc/p/8303242.html)
