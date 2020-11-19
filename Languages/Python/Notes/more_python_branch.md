---
title: more_python_branch
date: 2020-11-18 19:27:02
modify: 2020-11-19 11:51:05  
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# more_python_branch

## 概要

- python的版本管控可以通过pipenv来切换，但前提是当前系统有按照对应的python版本
- python版本可以通过编译安装，
- 按照多个python版本后通过`pipenv --python 3.6`来分别实例化对应的python环境，这样不会互相影响

## pip

- 多python版本通过pipenv来切换，但是默认会在`~/.local/bin`目录中添加可执行文件，比如`pipenv/pip/pip3`等，
- 即便是切换了python版本，比如python3.6可能使用的pip版本还是链接到python3.8的，
- 这是因为`.profile`文件中指定了PATH把`~/.local/bin`目录配置的优先级最高导致的，
- 删除该PATH的配置就可以

## 参考

