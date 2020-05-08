---
title: Yum
date: 2020-03-31 15:08:20
modify: 
tags: [Notes]
categories: CentOS
author: wmsj100
email: wmsj100@hotmail.com
---

# Yum

## 概要

- Yum: Yellow Dod Updater, Modified
- 是一个在Fedora/RedHat/CentOS中的Shell前端软件包管理器。
- 基于RPM包管理，能够从指定的服务器自动下载RPM包并且安装，可以自动处理依赖性关系，并且一次安装所有依赖的软件包，无须繁琐地一次次下载、安装。
- yum提供了查找、安装、删除某一个、一组甚至全部软件包的命令，而且命令间接而又好记。
- yum的一切信息都存储在一个`/etc/yum.repos.d`目录下的配置文件中，这个目录有很多文件，通常以`.repo`结尾
- repo文件是yum源的配置文件，通常一个repo文件定义了一个或多个软件仓库的细节内容，例如需要从哪里下载需要安装和升级的软件包，该文件将被yum读取和应用。

## repo配置解析

```
[base]
name=CentOS-$releasever - Base
mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=os&infra=$infra
#baseurl=http://mirror.centos.org/altarch/$releasever/os/$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
       file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7-aarch64
```

- `[base]`: yum的ID，必须唯一，本地有多个yum源的时候，这里必须唯一
- `name=CentOS-$releasever - Base`: 具体的yum源名字，其实相当于对它的描述信息，
- `mirrorlist`: 是镜像服务器的地址列表，里面有很多服务器地址，
- `baseurl`: 和mirrorlist都是指向yum源的地址，不同点是包含地址的多少，如果是自己写，一般只写一个地址，直接用baseurl就行。
- `gpgcheck=1` 要不要验证呢，0取消验证，1，使用公钥检验rpm的正确性。
- `gpgkey`: 如果`gpgcheck=1`则使用gpgkey提供的密钥进行校验下载的rpm包。

## 使用

- `yum install -q` quite install 静默安装
- `yum clean packages` 清除缓存目录下的软件包，清空的是(/var/cache/yum)下的缓存
- `yum clean headers` 清除缓存目录下的headers
- `yum clean oldheaders` 清除缓存目录下的旧headers
- `yum clean all` 清除缓存目录下的软件包
- `yum list` 显示所有已经安装和可以安装的程序包
- `yum list installed` 查看所有已经安装的包
- `yum list tree` 显示安装包信息
- `yum info tree` 显示tree的详细信息
- `yum install -y httpd` yum自动安装
- `yum remove httpd` 删除程序包
- `yum deplist which` 查看程序rpm依赖情况
- `yum check-update` 检查可更新的程序
- `yum update` 全部更新，升级所有包，以及升级软件和系统内核`
- `yum update tree` 更新指定程序包
- `yum upgrade tree` 升级指定程序包
- `sudo yum install --downloadonly --downloaddir=/home/redhat/download vim` 通过yum只是下载到指定目录，这种适用于离线安装包

## yum解决依赖的原理

- yum是基于C/S架构，C指客户端，S指服务器，
- 所有的yum源里面都有`repodata`它里面有XML格式文件，里面说明需要什么包，
- 下载的时候就会去当前系统检查是否有依赖包，或者版本是否匹配，否则就重新安装。

## yum组管理

- yum进行安装的时候可以一组一组的安装，
- `yum groups list` 显示当前已经安装的组

## 参考

- [yum 解析](https://www.cnblogs.com/liunaixu/p/10125487.html)
