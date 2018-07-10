---
title: rebase
date: 2018-07-10 09:57:07
modify: 
tags: [skill]
categories: Git
auth: wmsj100
email: wmsj100@hotmail.com
---

# rebase

## 概述
- `git rebase` 把当前分支`dev`里的每个提交(commit)取消掉，并且把它们临时保存为补丁(patch)(这些补丁文件放置在'.git/rebase'目录中)，然后把`dev`分支更新为最新的`origin`分支，最后把保存的这些补丁应用到`dev`分支上

- `conflict` 在`rebase`过程中，如果遇到冲突，`Git`会停止`rebase`并要求去解决冲突；在解决完冲突后，用`git -add`更新内容到索引`index`，然后不需要执行`git -commit`，只需要执行`git rebase --continue`;这样git会继续应用(apply)余下的补丁。

- `git pull --rebase` 把本地的当前分支里的每个提交取消掉，并且把它们临时保存为补丁，然后把本地当前分支更新为最新的`origin`分支，最后把保存的这些补丁应用到本地当前分支上。

## 总结
- 使用`rebase`的最大好处就是代码的提交记录会保持一致，不会出现分支合并的情况，很方便代码回退等操作。
- 使用`rebase`后，自己本地的提交记录会调整到最新的带提交记录。
- `gitk` 通过这个命令可以查看图形化的分支合并路线。
