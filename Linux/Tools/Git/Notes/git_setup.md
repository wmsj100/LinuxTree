---
title: Git设置及GitHub的使用
date: 2016-08-05
tags: [Tools]
categories: Language
---

http://www.cnblogs.com/peterzd/archive/2012/04/22/2465230.html

`cd ~/.ssh` -- 检查是否存在密钥
`ssh-keygen -t rsa -C "email"` -- 生成一个新密钥
`ssh -T git@github.com` -- 测试密钥是否连接成功

git config --global user.name "username"

git config --global user.email "email"