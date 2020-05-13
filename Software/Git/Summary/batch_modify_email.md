---
title: batch_modify_email
date: 2020-03-08 23:27:05
modify: 
tags: [Summary]
categories: Git
author: wmsj100
email: wmsj100@hotmail.com
---

# batch_modify_email

## 概要

- 批量修改用户提交的邮箱

## 命令

- 该命令需要在`.git`目录所在位置执行
```
git filter-branch -f --commit-filter '
	if [ "$GIT_AUTH_EMAIL" = "wmsj100@hotmail" ];then
		GIT_AUTHOR_NAME="wmsj100";
		GIT_AUTHOR_EMAIL="wmsj100@hotmail.com"
		git commit-tree "$@";
	else
		git commit-tree "$@";
	fi' HEAD
```
- 这条命令会重新修改全部的`git log`记录,而且也不是无痕修改,会让用户叠加,谨慎操作

## 参考

- [git 批量修改邮箱](https://blog.csdn.net/LeoForBest/article/details/90313471#git_2)
