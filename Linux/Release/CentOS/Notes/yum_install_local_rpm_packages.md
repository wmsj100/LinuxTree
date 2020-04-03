---
title: yum安装本地rpm包
date: 2020-04-03 14:56:36
modify: 
tags: [Notes]
categories: CentOS
author: wmsj100
email: wmsj100@hotmail.com
---

# yum安装本地rpm包

## 概要

- 这种场景还是很常见的，比如服务器无法连接网络，需要在离线环境下安装软件包，此时如果手动安装rpm包会被各种依赖困扰死，尤其是对于依赖比较复杂的场景，直接手动安装就是噩梦。
- 解决方法如下：

## 解决

- `yum install --downloadonly --downloaddir=/home/redhat/download/ vim` 下载离线文件
- `createrepo /home/redhat/download/` 构建本地软件源，
	- `yum install createrepo` 如果提示没有createrepo文件，就安装
- `mv /etc/yum.repo.d/CentOS-Base.repo /etc/yum.repo.d/CentOS-Base.repo.bak` 移除现有软件源
- `vim /etc/yum.repo.d/CentOS-Media.repo`
	- `file:///home/redhat/download/` 在baseurl下面添加一行本地源
- `yum install vim` 就会从本地安装软件
```
[c7-media]
name=CentOS-$releasever - Media
baseurl=file:///media/CentOS/
        file:///media/cdrom/
        file:///media/cdrecorder/
    file:///home/redhat/download/
gpgcheck=1
enabled=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
       file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7-aarch64
```

## 参考

- [yum install local rpm](https://blog.csdn.net/lxw1005192401/article/details/86611991)
