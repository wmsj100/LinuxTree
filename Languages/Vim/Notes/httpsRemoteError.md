---
title: Unable to find remote helper for 'https'
date: 2018-10-02 22:21:48	
modify: 
tag: [summary]
categories: Git
author: wmsj100
mail: wmsj100@hotmail.com
---

# Unable to find remote helper for 'https'

## 概述
- 通过git进行clone时候提示这个报错,这个是因为path路径缺失git的一个模块
- 在`/etc/bashrc`中的末尾添加`PATH=$PATH:/usr/libexec/git-core`

## 参考
- []()
