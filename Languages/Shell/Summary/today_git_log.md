---
title: today_git_log
date: 2020-10-18 12:16:27
modify: 
tags: [Summary]
categories: Shell
author: wmsj100
email: wmsj100@hotmail.com
---

# today_git_log

## 概要

- 查看今天提交的git的简短log信息

## 代码

```shell
data=$(git log --pretty=oneline --after='$(date \"+%Y-%m-%d 00:00\")')
for item in "$data"
do
    echo "$item"
done
```
## 参考

