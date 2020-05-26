---
title: stats
date: 2020-05-26 11:16:50
modify: 
tags: [Notes]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# stats

## 概要

- 通过该命令可以查看容器的资源使用率

## 使用

- `docker stats` 进入交互式监控界面
- `docker stats --no-stream` 打印当前的容器使用率
```
CONTAINER           CPU %               MEM USAGE / LIMIT       MEM %               NET I/O             BLOCK I/O           PIDS
30e409be4452        866.48%             1.064 GiB / 15.38 GiB   6.92%               1.01 kB / 1.01 kB   152 MB / 117 MB     40
449086a3cb58        0.00%               52.25 MiB / 15.38 GiB   0.33%               873 MB / 11 MB      1.16 GB / 469 MB    1
47e6365170bc        0.00%               67 MiB / 15.38 GiB      0.43%               66 MB / 1.6 MB      1.04 GB / 18.7 MB   4
f5dbe4b56ca1        0.00%               15.06 MiB / 15.38 GiB   0.10%               10.1 kB / 1.29 kB   5.18 MB / 0 B       2
```
- 参数解析
	- `CONTAINER` 容器的短ID
	- `CPU` CPU使用率
	- `MEN USAGE` 内存使用量
	- `LIMIT` 可以使用的总内存量
	- `MEM` 内存使用率
	- `NET` 网络使用率
	- `IO` 磁盘IO
	- `PIDS` PID号码

## 参考

- [docker stats](https://www.cnblogs.com/sparkdev/p/7821376.html)
