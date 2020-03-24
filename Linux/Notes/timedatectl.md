---
title: timedatectl
date: 2020-03-24 20:15:28
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# timedatectl

## 概要

- 用来控制系统时间和日期,设置时区

## 用法

- `timedatectl list-timezones` 查看哪些时区可用,列出系统上可用的所有时区.
- `sudo timedatectl set-timezone Asia/Shanghai` 设置时区
- `timedatectl statue` 查看系统当前的时区和时间设定
```
wmsj100@UbuntuOS:~/Documents/GitHub/LinuxTree/Linux/Notes$ timedatectl status
                      Local time: Tue 2020-03-24 20:22:13 CST
                  Universal time: Tue 2020-03-24 12:22:13 UTC
                        RTC time: Tue 2020-03-24 12:22:13
                       Time zone: Asia/Shanghai (CST, +0800)
       System clock synchronized: yes
systemd-timesyncd.service active: yes
                 RTC in local TZ: no
```

## 参考

- [linux timedatectl](https://www.digitalocean.com/community/tutorials/how-to-use-journalctl-to-view-and-manipulate-systemd-logs)
