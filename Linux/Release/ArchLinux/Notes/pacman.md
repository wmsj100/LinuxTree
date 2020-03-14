---
title: pacman
date: 2020-03-14 08:33:49
modify: 
tags: [Notes]
categories: ArchLinux
author: wmsj100
email: wmsj100@hotmail.com
---

# pacman

## 概要

- pacman是Archinux的官方软件包管理程序,本身也是bash程序
- 它将一个简单的二进制包格式和易用的构建系统结合
- 通过和主服务器同步软件包列表来进行系统更新.
- pacman用C语言编写,使用tar打包格式
- `/etc/pacman.conf` pacman的配置文件

## 使用

### 安装软件包

- 在arch下安装软件包时,未更新系统前,不要更新软件包数据库,因为可能某些软件包不再出现在官方库
- `sudo pacman -Syu docker` 更新系统并安装软件包

### 查询软件包

- `pacman -Qe` 所有明确安装的软件包,即自己安装的软件包
- `pacman -Qent` 所有明确安装的,存在于数据库而且不是直接或可选依赖的软件包
- `pacman -Qm` 所有外部安装的软件包,通常是手动下载安装或者已经从数据库中删除
- `pacman -Qn` 所有从数据库中安装的软件包
- `pacman -Qs` 按照正则表达式查询软件包

### 升级软件包

- `sudo pacman -Syu` 升级整个系统
- `sudo pacman -Syu docker` 升级系统时安装其他软件
- `sudo pacman -Sw tomcat9` 下载而不安装软件包
- `sudo pacman -U /path/to/package/package_name-version.pkg.tar.xz` 安装一个本地软件包
- `sudo pacman -U file://path/to/package/package_name-version.pkg.tar.xz` 安装一个远程包

### 查询包数据库

- `pacman -Q` 查询本地软件包数据库
- `pacman -S` 查询远程同步的数据库
- `pacman -Ss firmware` 在包数据库中查找软件包,查询位置包含了软件包的名字和描述
- `pacman -Qs docker` 查询已安装的关于docker的所有软件包
- `pacman -F docker` 按照文件名查询软件库,可能需要先下载软件库`sudo pacman -Fy`
- `pacman -Si docker` 显示软件包的详细信息
- `pacman -Qi docker` 查看本地安装包的信息信息,包含了被谁依赖
- `pacman -Ql docker` 查看已安装软件包含的文件列表
- `pacman -Fl docker` 查询远程库中包含的文件列表
- `pacman -Fy` 同步文件数据库
- `pacman -Qk screenfetch` 查看软件包文件是否都在
- `pacman -Qet` 罗列所有不被依赖的软件包

### 删除软件包

- `sudo pacman -Rs $(pacman -Qtdq)` 删除孤立软件包,如果没有孤立软件包会报错,是正常的
- `pacman -Rs lsb-release` 递归删除软件包,及其没有被其他程序使用的依赖
- `pacman -Rsc package` 递归删除软件包和所有依赖这个软件包的程序
- `pacman -Rdd package` 删除软件包,但是不删除依赖这个软件包的其他程序

### 显示所有软件包及其大小

- 借助expac软件包来管理输出
- `sudo pacman -S expac`
- `expac -H M '%m\t%n' | sort -h` 输出所有软件包占用空间并且按照大小排序
- `expac -S -H M '%k\t%n' docker` 查询软件包的下载大小,不写package默认查询全部
- `expac --timefmt='%Y-%m-%d %T' '%l\t%n' | sort | tail -n 20` 查询最近安装的20个软件包
- 查找不属于任何软件包的文件,通常这些文件是第三方程序使用一般方式安装(./configure;make;make install)
- `pacman -Qq | grep -Fv -f <(pacman -Qqm)` 仅显示正式安装的软件包

### pacman缓存

- `/var/cache/pacman` pacman的所有缓存都保存在这里,直接共享这个目录既可以
- `sudo pacman -Sc` 清理软件包缓存,会删除所有当前机器上未安装的软件包
	- 仅会保留软件包当前有效版本,旧版本的软件包被清理
- `sudo pacman -Scc` 清理所有缓存,除非空间不足,否则不要这样做
- `comm -23 <(pacman -Qeq|sort) <(pacman -Qmq|sort) > pkglist` 生成系统上安装的非本地(从官方仓库获取)软件包列表
- `pacman -S $(< pkglist)` 安装自己的所有软件包

### 重新安装所有软件

- `pacman -Qeq | pacman -S -` 
- `pacman -Qdq | pacman -S --asdeps -`

## 参考

