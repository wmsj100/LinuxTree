---
title: branch
date: 2016-03-24 12:18:58
modify: 2019-05-02 14:01:32	
tags: [Git]
categories: Frame
auth: wmsj100
email: wmsj100@hotmail.com
---

# branch

## 概述
- git branch -a 查看本地和远端所有分支信息
- git branch branchname 创建分支
- git branch -D branchname 删除分支
- git push origin --delete gh-pages 删除远端分支`gh-pages`
- `git remote -v`: 查看远程库信息，使用
- 本地新建的分支如果不推送到远程，对其他人就是不可见的；
- `git push origin branch-name`从本地推送分支，如果推送失败，先用`git pull`抓取远程的提交；
- `git checkout -b branch-name origin/branch-name`，在本地创建分支，本地和远程分支的名称建议保持一致；
- `git branch --set-upstream branch-name origin/branch-name` 建立本地和远端分支的联系
