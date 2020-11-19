---
title: profile
date: 2020-04-07 10:19:01
modify: 2020-11-19 11:48:37  
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# profile

## 概要

- `/etc/profile` 这个文件是bash最开始加载的配置文件，root的bash只从这个文件加载环境变量
- 这个文件会加载`/etc/profile.d`内部的shell文件，自定义的配置文件可以在`/etc/profile.d`目录内部创建自定义脚本来添加自己的环境变量
- `/etc/profile.d/colorls.sh` 这个文件可以设置alias
- `~/.profile`会做一些配置，比如添加PATH，而且优先级是放到默认PATH前面的，
	- 这种影响尤其是在多python版本中的pip调用位置会出现问题，所以可以直接屏蔽掉该文件中关于PATH的配置

## 加载顺序

- `/etc/profile/` 加载`/etc/profile.d/*.sh 该文件为系统的每一个用户设置环境信息，是所有的环境变量的父亲
- `~/.bash_profile` 加载`~/.bashrc`
- `~/.bashrc` 加载 `/etc/bashrc`
- `/etc/bashrc` 加载 `/etc/profile.d/*.sh`

## 参考

