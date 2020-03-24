---
title: journald
date: 2020-03-24 20:02:35
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# journald

## 概要

- journalctl最常用的就是用来查看系统日志
- systemd最引入注目的优点是那些涉及过程和系统日志记录的优点.
- 使用其他工具时,日志通常分散在整个系统中,由不同的守护程序和进程处理,并且当它们跨越多个应用程序时可能很难解释.
- systemd试图通过提供集中式管理解决方案来记录所有内核和用户态进程来解决这些问题.
- 收集和管理这些日志的系统成为日志
- 日志有journald守护程序实现,该守护程序处理内核,initrd,服务等产生的所有消息.

## 大概的概念

- systemd日志背后的推动力之一是集中式管理日志,无论消息源自何处.
- 由于许多引导过程和服务管理都是由systemd进程处理的,因此有必要对日志的收集和访问方式进行标准化.
- 带`journald`守护程序从所有可用的源中收集数据,并将以二进制格式存储,以便于动态进行操作.
- 这给我们带来了显著的优势,通过使用单个实用程序与数据进行交互,管理员可以根据自己的需求动态显示日志数据.
- 以二进制格式存储日志数据还意味着可以根据当前的需要以任意输出格式显示数据.
- 例如,可以将日志每个条目作为JSON对象输出,以使其可以用于图形服务.由于数据不是以纯文本格式写入磁盘,因此当需要按需格式化时,无需进行任何转换.
- journalctl除了收集类似`syslog`实现所能提供的来源中收集了更多的数据.
- 它包括早期引导过程,内核,initrd和应用程序标准错误以及退出的日志.

## 设定系统时间

- 使用二进制日志记录日志的好处之一是可以随意查看UTC或本地时间的日志记录.
- 默认情况下,systemd将以本地时间显示结果
- 因此在开始使用日志之前,需要确保时区设置正确.
- `systemd`套件附带了一个名为`timedatectl`的工具用来设置时区.

## 使用

- `journalctl` 查看当前所有的日志,如果`systemd`已使用了很长一段时间,则可能需要成千上万行,
- `journalctl --utc` 以UTC的时间戳来显示日志,日志默认时以本地时间来展示的.
- `journalctl -b` 只显示自最近重启以来收集的所有日志
- `/etc/systemd/journald.conf` journald的配置文件,通常情况下,发行版会启用保存以前的引导信息,但其他发行版也会禁用,可以修改该配置文件的`Storage=persistent`来启用持久化日志记录.
- `journalctl --list-boots` 列出当前服务器保存的以前的启动时记录,可以
	- `-11 7f6e3708dd63451c95af2121dc16a869 Mon 2020-03-16 23:12:26 CST—Mon 2020-03-16 23:25:45 CS`
	- 展示的格式如上,可以通过第一列的num,或者后面的id来查看具体日志
- `journalctl -b -3` 查看前3次的引导日志
- `journalctl -b 7f6e3708dd63451c95af2121dc16a869` 查看这个id对应的引导日志
- `journalctl --since "2020-03-23 17:15:00"` 查看自从指定的日期之后的日志内容
- `journalctl --since yesterday` 查看自从昨日以来的日志
- `journalctl --since 17:00 --until "1 hour ago"` 查看自从17:00之后,并且一小时之前的日志
- `journalctl -u nginx.service` 按照内容过滤,只查看`nginx.service`相关的日志
- `journalctl -u nginx.service --since today` 检查今天运行的nginx.service的日志
- `journalctl _PID=9111` 查看某个PID的日志
- `journalctl -u www-data` 查看这个用户组的信息
- `journalctl /bin/bash` 如果该路径指向可执行文件,则journalctl显示涉及该可执行文件的所有条目.
- `journalctl -k` 仅显示内核信息
- `journalctl --disk-usage` 查看日志在磁盘上的占用容量
- `journalctl --vacuum-size=1G` 删除旧日志,直到空间为指定大小为止
- `journalctl --vacuum-time=1years` 提供截止时间,超过该时间的条目会被删除.

## 参考

- [linux journalctl](https://www.digitalocean.com/community/tutorials/how-to-use-journalctl-to-view-and-manipulate-systemd-logs)
