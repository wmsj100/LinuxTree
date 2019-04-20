---
title: 用户信息
date: Tue 20 Feb 2018 10:35:46 PM CST
tag: [linux,user,sys]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

# 用户信息

## useradd 创建用户
- useradd test1 
- useradd -g group1 test1

## usermod 修改用户信息
- usermod 就是对 /etc/passwd 和 /etc/shadow 文件做一些修改
- 常用参数
    - d 新家目录文件夹 需要搭配 -m 使用
    - g 重新定义用户的用户组
    - G 给用户添加用户组
    - l 修改用户名
    - L lock 锁定用户
    - m move-home 移动家目录
    - p 修改秘密
    - s 修改shell
    - u 修改用户uid
    - U unlock 接锁用户
- usermod -g 2000  testuser 这个命令会把testuser原来的组删除，重新加入2000
- usermod -G 2000 testuser  这个命令会保留原来的组信息，重新添加组2000
- id testuser  查看testuser的详情
- usermod -d /home/test1_new/ -m test1 移动test1的家目录为test1_new
- usermod -l test2 test1 修改用户名为test2
- usermod -L test1 锁定用户，用户无法登陆 锁定用户后，/etc/shadow文件用户的密码第二列以！开头
- usermod -U test1 解锁定用户

## userdel 删除用户
- 从数据安全方面考虑默认删除用户并不会删除家目录和邮件信息
- userdel -r test1 删除家目录和邮件
