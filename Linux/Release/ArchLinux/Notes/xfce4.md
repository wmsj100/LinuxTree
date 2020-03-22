---
title: xfce4
date: 2020-03-22 09:48:57
modify: 
tags: [Notes]
categories: ArchLinux
author: wmsj100
email: wmsj100@hotmail.com
---

# xfce4

## 概要

- archLinux安装桌面,准备当作主力笔记本使用
- 安装桌面和输入法
- 桌面: xface4
- 输入法: ibus-libpinyin

## 流程

- 安装Xorg
	- `sudo pacman -S xorg` 安装xorg软件包,所有软件全部安装
	- `sudo pacman -S xorg-xinit` 安装X.Org的初始化程序,提供了`xinit/startx和默认的xinitrc文件
- 安装登陆管理器
	- `sudo pacman -S lightdm lightdm-gtk-greeter`
	- `sudo systemctl enable lightdm.service` 设置开机启动
- 安装桌面
	- `sudo pacman -S xfce4`
	- `sudo pacman -S xfce4-goodies`
	- `cp /etc/x11/xinit/xinitrc ~/.xinitrc`
	- `vi ~/.xinitrc`
		- 注释最后一行内容
		- `exec startx`
- 安装中文字体
	- `sudo pacman -S wqy-microhei`
	- 至此桌面安装完成,直接reboot重启,后面还需要安装中文输入法

## 参考

- [ArchLinux 安装xfce4](https://www.cnblogs.com/freerqy/p/8508395.html)
