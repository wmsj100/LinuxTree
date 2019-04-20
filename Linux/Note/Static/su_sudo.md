---
title: 切换用户/用户权限
date: Sun 25 Feb 2018 12:52:22 PM CST
tag: [linux]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

# 切换用户 su && sudo

## su 切换用户
- su 不加参数默认切换到root用户,之前的用户环境不变
- su - 切换到root角色，同时把bash环境切换到root的自定义设置
- 
- su - user1 切换到user1的bash环境 
- 使用su进行用户切换都需要输入切换用户的密码，root例外

## sudo 使用其它用户身份执行命令
- sudo并不是切换了用户，而是使用其它用户的身份和权限执行了命令
- sudo passwd user11 使用root身份修改用户user1密码
- visudo root角色通过这个角色进入sudo文件进行编辑
    - wmsj100 ALL=(ALL) ALL 允许wmsj100可以执行任何命令
    - %wmsj100 ALL=(ALL) ALL 允许属于wmsj100用户组的用户可以执行任何命令
    - %wmsj100 ALL=(ALL) NOPASSWD:ALL 允许所有属于wmsj100用户组的用户执行sudo命令时候不需要输入密码   默认执行sudo需要输入当前登陆用户密码
    - wmsj100 ALL=(ALL) NOPASSWD: ALL 允许wmsj100用户不输入密码执行sudo命令
    - 将最后一个参数设置为ALL是很不安全的，因为这样用户和root的权限是一样的。
    - wmsj100 ALL=(ALL) NOPASSWD:/sbin/shutdown,/usr/bin/reboot 用户wmsj100可以执行重启或者关闭服务的权限
