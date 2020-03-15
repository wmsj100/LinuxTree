---
title: iwconfig
date: 2020-03-15 15:06:46
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# iwconfig

## 概要

- 查看网卡的详细信息,可以用来查看wifi的详细信息

## 使用

```
ubuntu@Ubuntu:~/Documents/Github/LinuxTree/Linux/Notes$ iwconfig 
docker0   no wireless extensions.

lo        no wireless extensions.

docker_gwbridge  no wireless extensions.

wlx081079db1327  IEEE 802.11bgn  ESSID:"wmsj100"  Nickname:"rtl_wifi"
          Mode:Managed  Frequency:2.462 GHz  Access Point: B0:95:8E:C4:AE:1D   
          Bit Rate:150 Mb/s   Sensitivity:0/0  
          Retry:off   RTS thr:off   Fragment thr:off
          Power Management:off
          Link Quality=99/100  Signal level=74/100  Noise level=0/100
          Rx invalid nwid:0  Rx invalid crypt:0  Rx invalid frag:0
          Tx excessive retries:0  Invalid misc:0   Missed beacon:0

enp2s0    no wireless extensions.
```

## 参考

