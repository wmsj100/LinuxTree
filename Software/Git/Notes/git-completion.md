---
title: git-completion
date: 2020-03-17 13:57:38
modify: 
tags: [Notes]
categories: Git
author: wmsj100
email: wmsj100@hotmail.com
---

# git-completion

## 概要

- 手动编译安装完成git后发现使用时候没有git的补全功能

## 解决

- `cp  git/contrib/completion/git-completion.bash  ~/.git-completion.bash`
- `在.bashrc中添加  source ~/.git-completion.bash`

## 参考

- [git completion](https://www.cnblogs.com/kinwing/p/11670577.html)
