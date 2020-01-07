---
title: permissionDenide.md
date: Sun 03 Dec 2017 07:05:42 PM CST
tag: [Bash]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

- cat /dev/null > /var/log/wtmp 提示权限不足
- sudo cat /dev/null > /var/log/wtmp sudo只能让cat命令以sudo权限执行，而对于“>“并没有sudo权限
- sudo sh -c "cat /dev/null > /var/log/wtmp" 这样整个命令都具有sudo权限
