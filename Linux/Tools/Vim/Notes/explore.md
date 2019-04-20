---
title: 目录和缓冲区
date: 2017-12-13 15:15:15
tags: [vim]
categories: Linux
---

## 目录状态命令
- mb bookmark 书签一个目录
- d make a new Directory
- D Deleting Files or Directory
- i  chagne Listing style 切换展示样式，是否显示或隐藏文件时间信息
- o browsing with a horizontal split 水平分割展示文件
- v 竖向分割窗口并显示文件
- t 在新标签页中打开文件
- s 反复按s，会改变文件排序的方式，
- R 为光标下文件改名
- p use preview window 在预览窗口查看内容
- P edit in previous window 在预览查看编辑
- r reversing sorting order 是否逆序展示文件列表

- :cd 切换当前目录
- :pwd 查看当前目录
- :lcd 只要不发出'lcd'目录，所有窗口共享同一个当前目录。在一个窗口执行过一次':cd'命令，也同时改变其它窗口的当前目录。
  - 执行过'lcd'命令的窗口记得它特有的当前目录，在其它窗口执行':cd'或'lcd'目录对它毫无影响。
  - 在一个采用特有当前目录的窗口执行':cd'命令以后，该窗口就回头又采用共享的当前目录了。

## 缓存区列表
- :buffers 查看缓冲区列表
- :ls 功能类似于'buffers'也是展示缓冲区内容
- :hide edit 1.js 隐藏当前编辑文件打开新文件'1.js'，当前文件加入缓冲区列表
- :buffer 2 更具id号打开缓冲区文件
- :sbuffer 3 在新窗口打开缓冲区文件
- :bnext 编辑下一个缓冲区
- :bprevious 编辑上一个缓冲区
- :bfirst 编辑第一个缓冲区
- :blast 编辑最后一个缓冲区
- :bdelete 3 删除缓冲区文件3，当从缓冲区删除文件时候，该文件也从窗口关闭了
