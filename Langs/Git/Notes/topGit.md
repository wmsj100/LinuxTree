---
title: git高阶知识
date: Mon 25 Dec 2017 11:53:05 PM CST
tag: [git,kill]
categories: Git
author: wmsj100
mail: wmsj100@hotmail.com
---

# git 高阶知识

## branch分支的提交记录找回
- 问题描述，分支new有提交记录，但是分支被删除了，怎么找回提交记录
	- git checkout -b new
	- echo "hello" > file 7
	- git add .
	- git commit -m "hello"
	- git checkout master
	- git fsck --lost-found   这会展示一些commitID 列表
	- git show commitId  找出自己想要恢复的内容
	- git rebase commitID  进行恢复
	- git log 查看是否时想要恢复的内容
	- git reset --hard HEAD^  把刚才恢复的提交删除
	- git fsck --lost-found
	- git merge commitID 使用合并命令恢复

## 子模块 （有待学习）
