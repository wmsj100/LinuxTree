---
title: vlan
date: 2020-03-05 16:14:20
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# vlan

## 概要

- vlan: virtual local area network 虚拟局域网
- 是一组逻辑上的设备和用户，相互之间通信就像在同一个网段一样，不受物理位置限制。
- vlan就是一个广播域，vlan之间的通信是通过第三层路由器来完成的

## 创建vlan

- `modprobe --first-time 8021q` 确认已经载入该模块
- `modinfo 8021q` 显示该模块信息
- `/etc/sysconfig/network-scripts/ifcfg-enp5s0` 该文件配置上级接口
```ifcfg-enp5s0
TYPE=Ethernet
PROXY_METHOD=none
BROWSER_ONLY=no
BOOTPROTO=dhcp
DEFROUTE=yes
IPV4_FAILURE_FATAL=no
IPV6INIT=yes
IPV6_AUTOCONF=yes
IPV6_DEFROUTE=yes
IPV6_FAILURE_FATAL=no
IPV6_ADDR_GEN_MODE=stable-privacy
NAME=enp5s0
UUID=89dafce6-9998-4539-a47d-0d66e68a8e23
DEVICE=enp5s0
ONBOOT=no
```
- `/etc/sysconfig/network-scripts/ifcfg-enp5s0.10` 配置vlan接口
```ifcfg-enp5s0.10
DEVICE=enp5s0.10
BOOTPROTO=none
ONBOOT=yes
IPADDR=192.168.10.1
PREFIX=24
NETWORK=192.168.10.0
VLAN=yes
VLAN_ID=10
```
- `sudo nmcli connection reload` 重载全部配置文件
- `sudo ip link add link enp5s0 name enp5s0.10 type vlan id 10` 在以太网接口enp5s0中创建名为vlan10，id为10的802.1Q VLAN接口
- `ip -d link show enp5s0.10` 查看vlan
- `ip link delete enp5s0.10` 删除vlan
- `ifconfig enp5s0.10`
```
[wmsj100@localhost network-scripts]$ ifconfig enp5s0.10
enp5s0.10: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        inet 192.168.10.2  netmask 255.255.255.0  broadcast 192.168.10.255
        ether 00:23:54:ab:88:27  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

## 参考

- [centos 配置vlan](https://www.cnblogs.com/wangmo/p/11714387.html)
