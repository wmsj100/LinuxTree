---
title: 导出项目的log信息
date: 2020-01-10 11:13:52
modify: 
tags: [Summary]
categories: Git
author: wmsj100
email: wmsj100@hotmail.com
---

# 导出项目的log信息

## 概要

- 一个项目时间久了会由很多提交信息，如何统计和查看这些log呢，
- 可以直接导出log到一个文件，然后分析
- `git log --pretty=oneline >/tmp/log` 这样可以导出git的简略log信息
- `git log > /tmp/log` 导出完整的log信息

## 参考

