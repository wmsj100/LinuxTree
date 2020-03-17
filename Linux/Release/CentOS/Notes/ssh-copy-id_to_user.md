---
title: ssh-copy-id_to_user
date: 2020-03-17 11:35:26
modify: 
tags: [Notes]
categories: CentOS
author: wmsj100
email: wmsj100@hotmail.com
---

# ssh-copy-id_to_user

## 概要

- 腾讯云的centos主机默认是root登陆的,然后需要自己创建一个普通用户出来
- `useradd --create-home --shell /bin/bash --groups wheel wmsj100`	这样创建用户并且添加到wheel祖中,
- 如何实现ssh-copy-id到wmsj100呢,如果直接发送会提示
- `root@111.229.241.222: Permission denied (publickey,gssapi-keyex,gssapi-with-mic).` 没有权限操作
- 想来应该是centos不允许通过这样的方式直接添加密钥过去吧
- 我刚刚在树莓派上试了一下发现还是没有权限,之前以为是因为`wmsj100`的`.ssh`目录没有`authorized_keys`,通过root创建修改属主后发现还是无法添加公钥上去,所以应该是这个权限被锁死了.
- 然后是用root用户把自己目录`/root/.ssh/authorized_keys`复制到`/home/wmsj100/.ssh/`目录
- 然后就可以远程ssh登陆了.
- pi也需要这样操作才可以.
- 把pi的公钥通过ubuntu上传到centos上,然后在centos上主动把公钥添加到`authorized_keys`文件,然后就可以通过pi来ssh登陆centos了.

## 参考

