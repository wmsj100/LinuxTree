---
title: RPM
date: 2020-03-31 14:52:21
modify: 2020-05-27 16:25:07 
tags: [Notes]
categories: CentOS
author: wmsj100
email: wmsj100@hotmail.com
---

# RPM

## 概要

- RPM: Red-Hat Package Manager
- 虽然打上了RedHat的标志，但其原始设计理念是开发的，现在包括OpenLinux,suse,turbo Linux等Linux发行版都有采用，可以算是公认的行业标准。
- RPM遵循GPL规则且功能强大方便，因而广受欢迎。
- RPM套件管理方式的出现，让Linux易于安装，升级，间接提升了Linux的使用度。

## 用法

- `rpm -ivh your-package` 直接安装
- `rpm --force -ivh your-package` 强制安装
- `rpm --force --nodeps -ivh your-package` 强制安装，并且忽略依赖
- `rpm -ql which` 查询
- `rpm -e which` 卸载
- `rpm -qa` 列出所有安装过的包
- `rpm -q which` 获取软件包的文件全名 `which-2.20-7.el7.aarch64`
- `rpm -qf /usr/bin/sudo` 返回当前文件所属的rpm包
- `rpm -qif /usr/bin/sudo` 返回软件包的有关信息
- `rpm -qlf /usr/bin/sudo` 返回软件包的所有文件列表

## 范例

- `rpm -ql $(rpm -qa | grep mysql) | grep "etc/"` 查找mysql的所有配置文件

## 参考

- [rpm 讲解](https://www.cnblogs.com/ftl1012/p/rpm.html)
