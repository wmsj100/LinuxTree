---
title: trojan
date: 2020-03-23 18:26:24
modify: 2020-07-13 09:37:28  
tags: [Storage]
categories: Ubuntu
author: wmsj100
email: wmsj100@hotmail.com
---

# trojan

## 概要

- 翻墙使用的是这个软件,
- 通常的翻墙软件是通过加密内容来骗过GFW,比如常用的shadowstack等,但是现在GFW已经很先进,可以识别那些流量并进行拦截
- 通常的流量都是通过隧道,开专门的端口访问,比如VPS,但是现在行不通了.
- trojan的思路是把要访问的内容伪装成443端口的HTTPS内容,就是把访问谷歌的流量从隧道转成正常的流量来骗过防火墙

## ubuntu安装

- ubuntu的软件库没有这个软件,即便执行添加软件源也无法通过`sudo apt install trojan`来安装,所以只能通过在线脚本来安装
- `sudo bash -c "$(curl -fsSL https://raw.githubusercontent.com/trojan-gfw/trojan-quickstart/master/trojan-quickstart.sh)"`
- `sudo bash -c "$(wget -O- https://raw.githubusercontent.com/trojan-gfw/trojan-quickstart/master/trojan-quickstart.sh)"` 
- 上面俩个很可能会在下载过程中下载失败,所以可以单独执行,先下载脚本,然后手动把之前下载好的包放到/tmp的临时目录内
	- `sudo bash trojan-quickstart.sh`
- 修改配置文件
	- `sudo vi /usr/local/etc/trojan/config.json` 把自己的trojan的配置内容替换
	- `sudo systemctl start trojan.service` 启动这个服务
	- `sudo systemctl enable trojan.service` 设置开机启动
- 浏览器安装`switchomega`插件,然后进行倒入配置文件,既可以直接访问谷歌

## ArchLinux安装

- 这个发行版是最好安装的,因为所有软件更新最快
- `sudo pacman -S trojan`自动就会安装好
- `sudo vi /etc/trojan/config.json` 用自己的trojan进行替换就好
- `sudo systemctl start trojan.service`
- `sudo systemctl enable trojan.service`
- 浏览器进行配置并启动switchomega插件
- 也可以在控制台手动出发软件`trojan`

## 日志

- `sudo systemctl start trojan` 这样启动的trojan日志被系统收集在`journalctl`中,可以通过该命令来查看当前的访问日志.

## 通用方法

- 下载二进制包,解压到目录,并进入目录
- 解压之后进去配置`config.json`文件,是trojan的一个配置
- `sudo ./trojan` 就可以执行了,执行过程中可以配合火狐浏览器的插件`omega`,就按照自动的插件配置就好.这样可以在界面实时查看访问日志

## 端口占用

- windows启动trojan客户端时候直接闪退，不管是不是以管理员权限启动，报错` fatal: bind: 以一种访问权限不允许的方式做了一个访问套接字的尝试。`
- 查询资料是端口占用
- `netstat -nao` 看到`1080`端口是被占用的，trojan默认监听的是1080端口
- 重新修改配置文件，修改端口到1104，然后重启trojan，启动成功。

## 参考

- [trojan github指导安装](https://github.com/trojan-gfw/trojan/wiki/Binary-&-Package-Distributions)
