---
title: service服务进程
date: Sun 25 Feb 2018 04:04:48 PM CST
tag: [service]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

# 服务进程

## 基础概念
- service crond status 查看crond服务状态
```
● crond.service - Command Scheduler
   Loaded: loaded (/usr/lib/systemd/system/crond.service; enabled; vendor preset: enabled)
   Active: active (running) since Sun 2018-02-25 09:29:10 CST; 6h ago
 Main PID: 1199 (crond)
   CGroup: /system.slice/crond.service
           └─1199 /usr/sbin/crond -n
```

- service crond start 启用服务
