---
title: iotop
date: 2020-05-11 15:32:48
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# iotop

## 概要

- 这个工具类似top，是用来查看IO占用情况的

## 使用

- `yum install iotop`
```
Total DISK READ :       0.00 B/s | Total DISK WRITE :       0.00 B/s
Actual DISK READ:       0.00 B/s | Actual DISK WRITE:       0.00 B/s
  TID  PRIO  USER     DISK READ  DISK WRITE  SWAPIN     IO>    COMMAND
16384 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % docker-containerd-shim-current 5fb74fb5dd12b11523adc~f00330bfbe3a /usr/libexec/docker/docker-runc-current
    1 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % systemd --switched-root --system --deserialize 22
    2 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [kthreadd]
    3 be/0 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [rcu_gp]
    4 be/0 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [rcu_par_gp]
    6 be/0 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [kworker/0:0H-kblockd]
16391 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % docker-containerd-shim-current 6a6561afbc640f5b9425b~d16f4ac6254f /usr/libexec/docker/docker-runc-current
    8 be/0 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [mm_percpu_wq]
    9 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [ksoftirqd/0]
   10 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [rcu_sched]
   11 rt/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [migration/0]
   12 rt/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [watchdog/0]
   13 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [cpuhp/0]
   14 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [cpuhp/1]
   15 rt/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [watchdog/1]
   16 rt/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [migration/1]
   17 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [ksoftirqd/1]
   19 be/0 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [kworker/1:0H-kblockd]
```

## 参考

- [iotop](https://man.linuxde.net/iotop)
