---
title: 基础知识 
date: 2018-07-08 16:02:16	
modify: 2019-06-10 22:22:29 Monday	
tag: [sed]
categories: Linux 
author: wmsj100
mail: wmsj100@hotmail.com
---

# 基础知识

## 概述
- `cat *.file | sed '/^$/d' > out.file` 删除文件的空行
- `cat *.file | sed 's/^/- &/g' > out.file` 在文件的每一行插入`- `
- sed -i "s/wmsj100/WMSJ100/g" `grep -nrw "wmsj100" | awk -F : '{print $1}'`

## 参考
- []()
