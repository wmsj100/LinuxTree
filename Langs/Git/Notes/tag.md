---
title: 标签tag
date: Sun 25 Feb 2018 03:29:04 PM CST
tag: [git,basic]
categories: git
author: wmsj100
mail: wmsj100@hotmail.com
---

# git标签

## 概述
- 发布一个版本时，我们通常先在版本库中打一个标签，这样，就唯一确定了打标签时刻的版本。将来无论什么时候，取某个标签的版本，就是把那个打标签的时刻的历史版本取出来。所以，标签也是版本库的一个快照。
- git的标签虽然是版本库的快照，但其实它就是指向某个commit的指针，所以创建和删除标签都是瞬间完成的。

## 基础
- git tag || git tag -l 查看当前git库的标签列表
- git tag -n 查看当前所有标签的信息描述
- git tag -a v2.0.0 -m '版本v2.0'
- git push --tags || git push origin --tags 推送本地所有标签到服务器
- git tag -d tagName 删除tagName 标签名称
- `git show <tagname>`可以查看tag的信息；
- `git push origin <tagname>`可以推送一个本地标签；
- `git push origin  :refs/tags/<tagname>`可以删除一个远程标签。
