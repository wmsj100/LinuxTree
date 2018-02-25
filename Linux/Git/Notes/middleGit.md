---
title: git中级技能
date: Mon 25 Dec 2017 11:53:05 PM CST
tag: [git,config]
categories: Git
author: wmsj100
mail: wmsj100@hotmail.com
---

# git中级技能

- .gitignore  git track（追踪）时候要忽略的文件
	- foo.txt  忽略foo.txt
	- *.html 忽略所有的html文件
	- !foo.html 这个文件例外
	- *.[oa] 忽略所有的.o和.a文件

- 存储队列
- git stash save "work in" 把当前的工作状态暂存，可以先执行其他修复工作
- git stash list  查看暂存列表
- git stash apply 恢复到以前的工作状态
- git stash apply stash@{1} 使队列中的任意一个存储
- git stash clear 清空暂存队列。

## 分支
- git clone 会自动在本地建立一个“master”分支，他是“origin/master”的追踪分支，可以使用"git branch"时添加“--track”参数。来手动创建一个追踪分支
- git branch --track test origin/test   这样时在本地直接创建一个origin/test的分支，可以直接执行 git pull test 就可以自动拉取并且合并到本地的test分支。

## 撤销
- git reset --hard HEAD^ 清空当前工作区的内容到上次提交记录
- git checkout -- hello.rb 回退hello.rb文件

## 修改提交内容
- git commit --amend  可以修改上次提交的提交注释或者时添加性文件

## 维护git
- 保证良好的性能
	- git gc 进行压缩操作
- git blame file1 查看file1 的修改记录
- git config --global alias.oneline 'log --pretty=oneline' 添加别名 git oneline 查看单行log
- git config --global alias.cm 'commit -m' git cm 提交代码

## 定制git
- 添加颜色	
	- git config --global color.branch auto
	- git config --global color.status auto
	- git config --global color.diff auto
	- git config --global color.interactive auto
- 把颜色全部打开
	- git config --global color.ui true
- git config format.pretty oneline 把日志一行显示


