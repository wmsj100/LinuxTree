---
title: top
date: 2020-03-28 10:55:45
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# top

## 概要

- top是linux下常用的系统性能分析工具,能够实时显示系统中各个进程的资源占用情况,
- top是一个动态显示过程,可以通过用户按键来刷新当前状态,如果在前台执行该命令,它将独占前台,直到用户终止该程序为止.
- top提供了实时的对系统处理器的状态监视,它将显示系统中CPU最敏感的任务列表.
- 可以按cpu/内存/执行时间来进行排序

## top面板内容解析

- `top - 11:02:08 up  1:52,  1 user,  load average: 0.75, 0.77, 0.55` 第一行
	- `11:02:08` 当前系统时间
	- `up 1:52` 系统已经运行了1:52小时
	- `1 user` 当前有1个用户登陆
	- `load average: 0.75 0.77 0.55` load average后面的三个数值分别是1分钟,5分钟,15分钟的负载情况
		- load average数据是每隔5s检查一次活跃的进程数,然后按照特定算法计算出的数值,如果这个数值除以逻辑CPU的数量,结果高于5的时候就表明系统在超负荷运转了.
- `Tasks: 147 total,   2 running, 145 sleeping,   0 stopped,   0 zombie` 第二行进程
	- 当前系统共有147个进程,其中处于运行的只有2个,145个在休眠,stop状态的0个,僵尸状态的0个
	- 一般运行态的进程不能超过cpu的数量,如果超过了就说明是问题
- `%Cpu(s):  4.9 us,  1.4 sy,  0.0 ni, 92.2 id,  0.8 wa,  0.5 hi,  0.2 si,  0.0 st` 第三行cpu状态信息
	- `4.9 us` 用户空间占用cpu的百分比
	- `1.4 sy` 内核空间占用cpu的百分比
	- `0.0 ni` 改变过优先级的进程占用cpu的百分比
	- `92.2 id` 空闲cpu百分比
	- `0.8 wa` IO等待占用cpu的百分比
	- `0.5 hi` 硬中断(Hardware IRQ)占用cpu的百分比
	- `0.2 si` 软中断(Sofeware Interrupts)占用cpu的百分比
	- `0.0st` 虚拟机占用百分比
- `MiB Mem :   1913.6 total,    258.5 free,   1195.0 used,    460.1 buff/cache` 第四行 内存
	- 物理内存总量2G,
		- 指当前系统内核控制的内存数,不一定和物理内存匹配
	- 空闲258.5M,
		- 空闲内存总量是内核还未纳入其管理范围的数量,
		- linux中的free会越来越少页不用担心,有很多是之前创建的但现在还可以被重新使用,所以未交还空间
	- 使用1195.0M
		- 内核纳入管理范围的数量,
		- 纳入内核管理的内存不见的都在使用中,还包括过去使用过的现在还可以被重复利用的内存,
		- 内核并不把这些可以被重新使用的内存交到free中,
	- 缓存的内存量 460.1M
		- 用作内核缓存的内存量
- `MiB Swap:   4096.0 total,   4044.0 free,     52.0 used.    524.0 avail Mem ` 第五行 swap交换分区
	- 交换分区总量 4096M
	- 空闲 4044M
	- 使用 52M
	- 缓冲区 524M
		- 内存中的内容被换出到交换区,而后又被换入到内存,但使用过的交换区尚未被覆盖,该数值即为这些内容以存在与内存中的交换区的大小,
		- 相应的内存再次被换出时可不必再对交换区写入.
- `PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND`
	- `PID` 进程ID
	- `USER` 进程所有者
	- `PR` 进程优先级
	- `NI` nice值,负值表示高优先级,正值表示低优先级
	- `VIRT` 进程使用的虚拟内存的总量,单位kb
	- `RES` 进程使用的,未被换出的物理内存大小,单位kb
	- `SHR` 共享内存大小,单位kb
	- `S` 进程状态
		- D 不可中断的睡眠状态
		- R 运行
		- S 睡眠
		- T 跟踪/停止
		- Z 僵尸进程
	- `%CPU` 上次更新到现在的CPU时间占用百分比
	- `%MEM` 进程使用的物理内存百分比
	- `TIME+` 进程使用的CPU时间总计,单位为1/100秒
	- `COMMAND` 进程名称

## 使用技巧

- top界面操作命令
	- `1` 可以切换多核cpu的状况
	- `b` 高亮显示当前的运行进程,就是显示的第二行的running
	- `x` 默认是按照CPU的占用量来排序的,x可以高亮排序列f
	- `shift </>` 可以调整排序列
	- `s` 调整top刷新时间
	- `i` 忽略闲置和僵死进程
	- `m` 切换显示内存信息
	- `t` 切换显示cpu信息
	- `c` 切换显示完整commang命令信息
	- `M` 根据驻留内存排序
	- `P` 根据cpu百分比进行排序
	- `T` 根据累积使用时间进行排序
- top 参数
	- `top -c` COMMAND列显示完整的命令
	- `top -b` 以批处理方式显示程序信息
	- `top -S` 以累积模式显示程序信息
	- `top -n 2` 设置top的更新次数
	- `top -d 5` 设置top的更新时间,默认是3s


## 参考

- [linux top解析](https://www.cnblogs.com/peida/archive/2012/12/24/2831353.html)
