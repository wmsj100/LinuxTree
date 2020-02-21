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

## 参考

- [oss ram](https://ram.console.aliyun.com/overview)
