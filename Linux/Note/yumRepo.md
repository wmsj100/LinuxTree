---
title: yum添加第三方源
date: Sat 03 Mar 2018 03:23:42 PM CST
tag: [yum]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

## yum 添加第三方资源地址 [参考文献](http://www.cnblogs.com/roverliang/p/4743760.html)
- su - 进入root用户
- cd /etc/yum.repos.d
- mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup  # 备份系统自带镜像文件
- wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo  下载阿里云的yum配置文件
- yum clean all  # 清除缓存
- yum makecache

