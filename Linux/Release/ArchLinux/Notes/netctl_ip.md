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

### 网卡设置静态IP

- netctl的所有配置文件模板在example在目录中可以找到,所以根据自己的目的拷贝一个,然后修改相关参数就可以,比如ip/网卡
```
Description='A basic static ethernet connection'
Interface=enp5s0
Connection=ethernet
IP=static
Address=('192.168.20.3/24')
#Routes=('192.168.0.0/24 via 192.168.1.2')
#Gateway='192.168.20.1'
DNS=('192.168.20.1')

## For IPv6 autoconfiguration
#IP6=stateless

## For IPv6 static address configuration
#IP6=static
#Address6=('1234:5678:9abc:def::1/64' '1234:3456::123/96')
#Routes6=('abcd::1234')
#Gateway6='1234:0:123::abcd'
```
- 配置文件中的`Gateway`不能配置,因为如果是双网卡,都添加Gateway之后,路由就会有俩个default,这样就会冲突,默认选择第一个,可能就无法ping通外网了.
- 所以这个内网的网卡不需要设置gateway

## 参考

- [arch wiki](https://wiki.archlinux.org/index.php/Netctl_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))
