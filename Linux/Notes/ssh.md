---
title: ssh
date: 2020-04-09 11:23:59
modify: 2020-06-30 10:06:44  
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# ssh

## 概要

- ssh是用来链接或者执行远程命令的工具，
- `yum install openssh-client` 可以安装，
- `yum install openssh-server`
- `systemctl start sshd.server` 启动服务，然后就可以通过其他主机就可以通过ssh来链接这个服务器
- 这样就可以使用ssh,scp

## 配置文件

- `/etc/ssh/sshd_config` 这个是ssh的服务端配置文件，一般通过这个配置文件来开启客户端的root链接权限
- `/etc/ssh/ssh_config` 这个是客户端链接到服务端的配置文件，如果连接服务端失败很可能是这个文件的错误导致的。

## 总结

- `/etc/ssh/ssh_config: line 70: Bad configuration option: clientaliveinterval`
- 这个错误就是ssh_config的配置错误导致，直接注释掉这俩行就可以了。

## 参考

- [ssh_config错误参考](http://www.vuln.cn/2782)
