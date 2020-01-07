---
title: fg_bg_jobs
date: 2019-05-11 22:56:25 Saturday
modify:
tag: [basic,fg,bg,jobs]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

# fg_bg_jobs

## 概述
- 用来切换前后台进程

## 用法
- jobs 查看被停止并放置在后台的工作。
- fg %2 把后台运行的number号尾2的提取到前台
- ctrl z 把工作停止放置在后台，
- bg %2 可以让后台的进程继续运行
- kill 1% 删除进程
- top 实时查看进程的状态
- ps 静态查看当前进程的状态信息
- nice 静态优先级，是用户空间的一个优先级值，去值范围是-20～19，值越小，表示优先级越高，-20优先级最高，19优先级最低。
- 进入top界面后，
	- i 忽略闲置和僵死的进程，一个开关式命令。


## 范例

## 参考
- []()

