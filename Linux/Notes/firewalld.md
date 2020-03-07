---
title: firewalld
date: 2020-03-05 10:18:35
modify: 2020-03-07 13:07:34  
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# firewalld

## 概要

- centos7之前默认的防火墙软件是iptables,之后版本就默认成了`firewalld`
- 默认是关闭所有的端口接入的，可以请求端口，但是不能通过端口接入

## 常用命令

- `sudo systemctl start firewalld.service` 开启防火墙
- `sudo enable firewalld.service` 防火墙开机启动
- `sudo systemctl stop firewalld.service` 关闭防火墙
- `sudo firewall-cmd --state` 查看防火墙状态
- `sudo firewall-cmd --reload` 重载配置
- `sudo firewall-cmd --get-zone-of-interface=wlp3s0` 查看当前网卡/接口所属的域，默认返回`public`
- `sudo firewall-cmd --zone=public --list-ports` 查看当前域开发的端口，默认是空
- `sudo firewall-cmd --zone=public --add-port=2377/tcp --permanent` 给public域添加端口白名单，通过设置permanent来让设置持久化，否则重启firewall就失效了
- `sudo firewall-cmd --zone=public --add-port=8012-8022/tcp` 添加多个连续的端口区间
- `sudo firewall-cmd --zone=public --remove-port=8022-8012/tcp` 删除多个端口,可以反过来,firewall会自动识别
- `sudo firewall-cmd --add-rich-rule="rule family="ipv4" source address="192.168.0.102" port protocol="tcp" port="8011" accept"` 针对某一个ip放开端口
- `sudo firewall-cmd --remove-rich-rule="rule family="ipv4" source address="192.168.0.103" port port="22" protocol="tcp" accept"` 删除针对ip的规则
- 再次查看public域开发的端口就会发现已经有一个端口开发了
- firewall默认的zone是public，这是不信任的网络，如果是在局域网中，所有连入的机器都是授信的，可以设置zone为`trusted`
- `	/etc/firewalld/firewalld.conf`修改`DefaultZone=trusted`模式

## 参考

- [centos firewall常用操作](https://www.cnblogs.com/inos/p/10985042.html)
