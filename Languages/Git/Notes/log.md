---
title: log
date: 2020-01-10 11:20:09
modify: 
tags: [Notes]
categories: Git
author: wmsj100
email: wmsj100@hotmail.com
---

# log

## 概要

- 如何查看log更多信息呢，因为是有这个需求的，不然查看提交的修改文件，或者直接查看修改的内容变更

## 命令

- `git log --stat` 查看log，并且呈现修改的文件
- `git log -p` 查看具体的修改内容
- `git log -p -2` 只查看最近俩次的提交内容变更
- `git log --pretty=oneline/full/fuller/short` 分别展示不同程度的log信息
- `git log --pretty=format:"参数"
	- %H 提交对象完整哈希值
	- %h 提交对象的简短哈希值
	- %an 作者名字
	- %ae 作者邮箱
	- %cd 提交日期
	- %s 提交说明描述
- `git log --pretty=format:"%h %an %ae %cd %s" --date=iso  自定义展示的log信息，并且日期格式是iso格式
- --date=(relative|default|local|iso|rfc|short|raw)
	- short 只展示年份，这个比较实用，我只关心提交的日期，具体提交的时间的重要性可能不高
- `git log --graph` 显示分支/合并历史
- `git log --shortstat` 只显示--stat最后的行数修改添加移除统计
- `git log --name-only` 仅显示已修改文件的清单
- `git log --name-status` 显示新增/修改/删除的清单
- `git log --abbrev-commit` 只显示简短的哈希值
- `git log --author=wmsj100` 只显示作者log
- `git log --grep="linux"` 只显示描述中包含`linux`的记录
- `git log -2` 仅显示最近2条提交记录
- `git log --after=2020-01-08` 仅显示2020-01-08之后的提交记录
- `git log --after=2020-01-08 --before=2020-01-09` 仅显示08/09俩天的提交记录

## 参考

- [git log文档](https://git-scm.com/book/zh/v2/Git-%E5%9F%BA%E7%A1%80-%E6%9F%A5%E7%9C%8B%E6%8F%90%E4%BA%A4%E5%8E%86%E5%8F%B2)

