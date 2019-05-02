---
title: stash
date: 2019-05-02 13:59:27	
modify:
tag: [stash]
categories: Git
author: wmsj100
mail: wmsj100@hotmail.com
---

# stash

## 概述
- 当工作只进行到一半的时候，还没发提交，预计还得一天时间。但是，必须要在俩个小时内修复bug，怎么办？
- git stash——可以把当前工作现场“存储”起来，等以后恢复现场后继续工作：`git stash`
- 只需要输入`git stash`即可把当前的工作状态存储起来。当完成bug修复并且切换会自己的分支时候`git checkout wmsj100`，然后输入命令`git stash list`可以查看存储的版本，然后使用`git stash apply`来恢复，但是恢复后，stash内容并不删除，而通过命令`git stash drop`来删除存储。
- 另一种方式是通过输入命令`git stash pop`恢复的同时把stash内容也删除了；

- git branch -D wmsj100——强行删除一个分支；
 - 开发一个新feature，最好新建一个分支；
 - 如果要丢弃一个没有合并过得分支，可以通过`git branch -D wmsj100`强行删除。

## 参考
- []()
