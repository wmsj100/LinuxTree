---
title: 删除.git大文件
date: 2019-05-02 13:53:23	
modify:
tag: [.git,git]
categories: Git
author: wmsj100
mail: wmsj100@hotmail.com
---

# 删除.git大文件

## 概述
- 随着项目的进行，有很多废弃的大文件需要删除，虽然在当前目录删除了，但是在`.git`目录内部还是有保留

## 删除步骤
- `git rev-list --objects --all | grep "$(git verify-pack -v .git/objects/pack/*.idx | sort -k 3 -n | tail -5 | awk '{print$1}')" `
- 从历史中删除 target/ 这个文件夹 
- `git filter-branch --force --index-filter 'git rm -r  --cached --ignore-unmatch java/book/' --prune-empty --tag-name-filter cat -- --all`
- 执行仓库压缩
- `git gc --prune=now`
- 推送到远程仓库 
- `git push origin --force --all`

## 参考
- [.git目录瘦身](https://blog.csdn.net/qq_40233736/article/details/86668768)
