---
title: remote
date: 2019-04-20 11:04:13	
modify:
tag: [remote,basic,git]
categories: Git
author: wmsj100
mail: wmsj100@hotmail.com
---

# remote

## 概述
- git远端地址
- git remote -v 查看源列表
- git remote add origin git@github.com:wmsj100/LinuxTree.git
- git remote rename origin githua 重命名
- git remote renove origin 移除地址源
- git push --set-upstream origin master 设置默认提交remote源
- git@gitlab.com:wmsj100/HelloWorld.git
- git remote set-url origin --push --add git@gitlab.com:wmsj100/HelloWorld.git 同时push多源

## 多源提交
- 先删除所有源
- git remote add origin git@....
- git remote -v 可以看到添加的源，有俩个push/fetch
- git remote set-url --add origin git@gitlab.com:wmsj100/HelloWorld.git 给origin源再添加一个源地址
- git push --set-upstream origin master 设置默认提交分支

## 参考
- [git多分支](https://segmentfault.com/a/1190000011294144)
