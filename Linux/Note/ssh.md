---
title: ssh
date: 2019-05-16 22:58:14 Thursday
modify:
tag: [ssh]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

# ssh

## 概述
- ssh是一种通讯协议，可以实现安全远程登陆

## 用法
- `ssh-keygen -t rsa -C "wmsj100@hotmail"` 生成密钥
- `ssh-copy-id pi@192.168.1.103` 把客户端公钥发送给服务器，服务器会把公钥追加到服务端对应用户的`$HOME/.ssh/authorized_keys` 文件中
- 这样操作后就可以在客户端直接`ssh pi@192.168.1.103`登陆了，免密码操作

## 范例

## 参考
- [ssh客户端](https://blog.csdn.net/m0_37822234/article/details/82494556)

