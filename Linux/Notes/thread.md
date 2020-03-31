---
title: 线程
date: 2020-03-28 09:47:30
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# 线程

## 概要

- 线程:是操作系统能够进行运算调度的最小单位,大部分情况下它被包含在进程之中,是进程中的实际运作单位.
- 一条线程指的是进程中一个单一顺序的控制流,一个进程中可以并行多个线程,每条线程并行执行不同任务.
- 线程是独立调度和分派的基本单位,线程可以为操作系统内核调度的内核线程;有用户进程自行调度的用户线程;或由内核和用户进程进行混合调度.
- 同一进程中的多个线程将共享该进程的全部系统资源,如虚拟地址空间,文件描述符和信号处理等,
- 但同一进程中的多个线程有各自的调度栈,自己的寄存器环境,自己的线程本地存储.
- 一个进程可以有很多线程,每个线程执行不同的任务.
- 在多核或多CPU,或支持Hyper-threading的CPU上使用多线程程序设计的好处是显而易见的,即提高了程序执行的吞吐率.
- 在单CPU单核的计算机上,使用多线程技术,也可以把进程中负责IO处理,人机交互而常被阻塞的部分与密集计算的部分分开来执行.编写专门的workhouse线程执行密集计算,从而提高了程序执行效率.

## 参考

- [wikipedia thread](https://zh.wikipedia.org/wiki/%E7%BA%BF%E7%A8%8B)