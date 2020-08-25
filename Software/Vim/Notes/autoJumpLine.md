---
title: 自动跳到上次文件位置
date: 2020-08-25 11:58:40
modify: 
tags: [Notes]
categories: Vim
author: wmsj100
email: wmsj100@hotmail.com
---

# 自动跳到上次文件位置

## 概要

- vim 自动跳到文件上次打开位置

## 配置

- `vim ~/.vimrc`
```vim
if has("autocmd")
  au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif
endif
```

## 参考

- [vim auto jump](https://blog.csdn.net/linhai1028/article/details/79745054)
