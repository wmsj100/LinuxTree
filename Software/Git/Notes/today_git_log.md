---
title: today_git_log
date: 2020-10-15 17:32:30
modify: 
tags: [Notes]
categories: Git
author: wmsj100
email: wmsj100@hotmail.com
---

# today_git_log

## 概要

- 想要查看今天的git提交记录是一个刚需，之前需要手动输入很长的一个命令行
- 通过alias可以设置快捷键

## 配置

```bashrc
today_zero=$(date "+%Y-%m-%d 00:00")
alias today-git-log="git log --pretty=oneline --after='${today_zero}'"
```
- 这样就可以直接在命令行输入`today-git-log`来查看今天的git提交记录

## 参考

