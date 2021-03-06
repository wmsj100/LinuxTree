---
title: submodule
date: 2020-03-11 21:17:13
modify: 
tags: [Notes]
categories: Git
author: wmsj100
email: wmsj100@hotmail.com
---

# submodule

## 概要

- 使用这个是想要在本地配置vim的环境`YouCompleteMe`插件时候发现需要下载很多
- 主软件包可以在码云上面加速下载,但是它里面包含了数十个子仓库,每次都是执行安装程序,然后自动触发报错,找到报错开始安装
- 原来git本来就支持这种父子项目

## 概念解释

- `git submodule`是一个很好的多项目使用共同类的工具,他允许库项目作为repository,子项目作为一个单独的git项目存在于父项目中,子项目可以有自己独立的commit/push/pull
- 父项目以`submodule`的形式包含子项目
- 父项目可以指定子项目header,提交时候会包含submodule信息
- 克隆父项目时候时候可以把submodule初始化

## 项目中添加submodule

- `git submodule add git@github.com:wmsj100/test1.git`
- `git status` 可以看到添加了文件`.gitmodules test1`
	- .gitmodules包含了submoudle的主要信息
	- test1 指定子项目的commit id,就能指定到对应的git header上面
	- 这俩个文件都需要提交到父项目的git中

## 更新submodule

- `git submodule update --init --recursive` 可以直接批量递归把所有的submodule下载,这个在第一次使用,可以让所有submodule的状态重置到当前父项目记录的commit id
- `git submodule foreach --recursive git pull origin master` 这样是在持续更新submodule
- `git pull` 进入每一个submodule中执行更新命令
- 如果submodule有新的commit id产生,需要在父项目产生一个新的提交
- 对于submodule的更新是需要父项目主动来控制子项目的commit id是否要更新,不会因为子项目已经更新了,主项目就自动跟随更新,这样的设置是合理的.
- `git clone git@gitee.com:wmsj100/subtest1.git --recursive` 直接按照递归的方式下载整个项目
- 依次递归更新每一层级的项目
	- `git clone git@gitee.com:wmsj100/subtest1.git` 下载主项目
	- `cd subtest1`
	- `git submodule init` 初始化submodule
	- `git submodule update` 下载当前层级的submodule,不是递归下载,只是下载当前层级所有的submodule,如果要继续,需要在分别进入子submodule中执行`git submodule init/git submoudle update`

## 参考

- [git submodule简介](https://segmentfault.com/a/1190000003076028)
