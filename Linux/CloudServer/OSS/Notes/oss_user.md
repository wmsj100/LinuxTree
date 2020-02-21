---
title: oss用户
date: 2020-02-21 18:08:47
modify: 
tags: [Notes]
categories: OSS
author: wmsj100
email: wmsj100@hotmail.com
---

# oss用户

## 概要

- oss的用户可以在阿里云进行管理

## RAM管理子用户

- 阿里云通过RAM创建子用户来管理用户的权限
- 先创建用户组，然后把用户添加到用户组进行权限继承
- 对于oss的所有操作都是通过ram的子用户身份进行，因为这种角色的用户权限是受限的且随时可以禁用和取消
- RAM用户对应一个操作实体

## sdk用户权限配置

- 创建用户会展示一个`accessKeyID`和`accessKeySecret`俩个关键字
- 只会展示一次，需要妥善保管。
- 可以配置`~/.ossutilconfig`中配置，也可以sdk访问时候配置。

## 参考

- [oss ram](https://ram.console.aliyun.com/overview)
