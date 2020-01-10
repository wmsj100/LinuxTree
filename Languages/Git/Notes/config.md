---
title: config
date: 2019-11-30 21:14:42 Saturday
modify: 2020-01-10 11:31:20
tag: [config]
categories: Git
author: wmsj100
mail: wmsj100@hotmail.com
---

# config

## 概述

- 这是git的配置文件,可以添加参数`--glocal`来使这个参数在全局生效

## 修改默认编辑器

- `git config --global core.editor vim` 修改git的默认编辑器为vim,是全局生效的
- `vi .git/config`,在`core`中添加`editor=vim`,只是针对当前的git库作出修改.
- `git config --global log.date iso-strict-local` 修改log的日期显示为"Date:   2020-01-10T09:01:34+08:00"

## 参考
- [修改git的默认编辑器](https://blog.csdn.net/qwaszx523/article/details/79622844)
