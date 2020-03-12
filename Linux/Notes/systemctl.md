---
title: systemctl
date: 2020-03-12 08:48:19
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# systemctl

## 概要

- 监视和控制systemd的工具,可以查看系统状态和管理系统及服务

## 单元

- 一个单元配置文件可以描述如下内容之一:
	- 系统服务.service
	- .mount 挂载点
	- .sockets 
	- .device 系统设备
	- .swap 交换分区
	- .path 文件路径
	- .target 启动目标
	- .timer 计时器
- systemctl控制单元时,通常需要使用单元文件的全名,包括扩展名(sshd.service)
	- 如果无扩展名,默认扩展名当作`.service`
	- 挂载点会自动转化为相应的`.mount`单元,例如`/home` == `home.mount`
	- 设备自动转化为相应的`.device`,'/dev/sda2' == 'dev-sda2.device'
- 单元常用命令
	- `systemctl status sshd.service` 查看单元运行状态
	- `systemctl start sshd`
	- `systemctl stop sshd`
	- `systemctl restart sshd`
	- `systemctl reload sshd` 重新加载配置
	- `systemctl is-enabled sshd` 查看单元是否配置为自动启动
	- `systemctl enable sshd` 开机启动单元
	- `systemctl enable --now sshd` 设置单元为自动启动并立即启动这个单元
	- `systemctl disable sshd` 取消开机自动启动
	- `systemctl mask sshd` 禁用一个单元,禁用后,间接启动也是不可能的
	- `systemctl unmask sshd` 取消禁用一个单元
	- `systemctl help sshd` 显示单元手册
	- `systemctl daemon-reload` 重新载入`systemd`系统配置,扫描单元文件的变动
- 电源管理
	- `systemctl reboot`
	- `systemctl poweroff`
	- `systemctl suspend` 待机
	- `systemctl hibernate` 休眠
	- `systemctl hybrid-sleep` 混合休眠模式(同时休眠到硬盘并待机)

## 编写单元文件

- `systemctl show --property=UnitPath` 按照优先级从低到高显示加载目录
- `/usr/lib/systemd/system` 软件包安装的单元
- `/etc/systemd/system` 系统管理员安装的单元

## 常用命令

- `systemctl status` 显示系统状态
- `systemctl` 输出激活的单元
- `systemctl list-units` 同上
- `systemctl --failed` 显示运行失败的单元
- `systemctl --state=failed` 显示失败的单元
- `systemctl list-unit-files` 查看所有可用的单元文件,查看所有已安装服务
	- `/usr/lib/systemd/system`
	- `/etc/systemd/system/`
	- 后面的目录优先级更高
- `systemctl -H arch@192.168.0.101` 实现对其他机器的远程控制,该功能使用SSH连接

## 参考

- [arch systemctl讲解](https://wiki.archlinux.org/index.php/Systemd_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)#systemd_%E5%9F%BA%E6%9C%AC%E5%B7%A5%E5%85%B7)
