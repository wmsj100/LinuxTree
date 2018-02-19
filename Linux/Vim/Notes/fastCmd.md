---
title: 快速命令
date: Mon 11 Dec 2017 11:47:06 PM CST
tag: []
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

## 命令行的移动，通常搜索或替换时候的命令行
- ctrl B 命令行行首
- ctrl E 命令行行尾
- shift/ctrl Left shift或ctrl加方向左键，作移动一个单词
- shift/ctrl Right 右移动一个单词
- ctrl w 删除光标前的一个单词
- ctrl u 删除命令行的全部文字
- q: 打开命令行窗口，里面存放的是刚刚输入的命令，

## vim会话
- vim会话存放着所有跟编辑相关的信息，包括诸如文件列表/窗口布局/ 全局变量/ 选项/ 以及其它信息。
- :mksession vimbook.vim 创建会话文件在当前目录
- :source vimbook.vim 使用会话文件
- vim -S vimbook.vim 启动vim时候还原会话

## 视图
- 视图会存储窗口的设置信息，比如时候显示行号，时候要折叠代码等
- :mkview 1 参加视图1
- :loadview 1 加在视图1 通过这个命令可以在托个视图间切换
- :mkview ~/.vim/main.vim 把视图存储到文件中
- :source ~/.vim/main.vim 还原视图
