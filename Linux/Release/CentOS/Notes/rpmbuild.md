---
title: rpmbuild
date: 2020-04-01 07:50:54
modify: 
tags: [Notes]
categories: CentOS
author: wmsj100
email: wmsj100@hotmail.com
---

# rpmbuild

## 概要

- 这个文件会指引你在CentOS下安装及设置一个用来创建RPM的环境
- 切勿以root身份来创建RPM,这个工作应该永远在一个没有特殊权限的户口内执行.以root的身份来创建RPM可能会损坏系统.

## 命令

- `sudo yum install rpm-build` 安装rpm-build
- `rpmbuild --showrc`
- `rpmbuild --version` 查看版本
- `rpm -q redhat-rpm-config` 大部分以CentOS作为重建目标的SRPM亦需要特点的rpmbuild创建宏及辅助脚本，他们都收录在redhat-rpm-config组件内。
- `sudo yum install redhat-rpm-config`

## 参考

- [centos rpmbuild wiki](https://wiki.centos.org/zh/HowTos/SetupRpmBuildEnvironment)
