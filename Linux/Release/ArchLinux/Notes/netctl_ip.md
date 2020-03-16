---
title: netctl_ip
date: 2020-03-16 09:32:57
modify: 
tags: [Notes]
categories: ArchLinux
author: wmsj100
email: wmsj100@hotmail.com
---

# netctl_ip

## 概要

- arch的笔记本的ip是通过wifi-menu来设置并连接的
```
Description='Automatically generated profile by wifi-menu'
Interface=wlp3s0
Connection=wireless
Security=wpa
ESSID=wmsj100
IP=static
Address=('192.168.0.101/24')
Gateway='192.168.0.1'
DNS=('192.168.0.1')
Key=wifipasswd
```
- 如果不设置dns,无法进行域名解析,直接去ping baidu.com,第一次会失败,但如果是去ping一个远端ip,然后再ping baidu.com可能就ping通了
- 应该是dns的表通不下来了.
- 最好还是设置dns,这样肯定可以ping通域名,

- arch的默认是dhcp方式
```
Description='Automatically generated profile by wifi-menu'
Interface=wlp3s0
Connection=wireless
Security=wpa
ESSID=wmsj100
IP=dhcp
Key=wifipasswd
```

## 参考

- [arch wiki](https://wiki.archlinux.org/index.php/Netctl_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))
