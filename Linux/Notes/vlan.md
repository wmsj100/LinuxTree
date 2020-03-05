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

- `cd /etc/sysconfig/network-scripts`
- `sudo cp ifcfg-enp5s0 ifcfg-enp5s0.10` 拷贝主网卡到一个子网配置文件
```ifcfg-enp5s0.10
PHYSDEV=enp5s0
VLAN=yes
TYPE=Vlan
VLAN_ID=10
REORDER_HDR=yes
GVPR=no
MVRP=no
BOOTPROTO=none
IPADDR=192.168.10.2
PREFIX=24
GATEWAY=192.168.10.1
DEFROUTE=yes
IPV4_FAILURE_FATAL=yes
NAME=enp5s0.10
ONBOOT=yes
```
- `nmcli c reload` 重新加载所有的网络配置文件
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

- [centos 创建vlan](https://blog.51cto.com/4153087/2089390)
