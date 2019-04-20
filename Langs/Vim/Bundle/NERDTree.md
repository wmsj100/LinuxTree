---
title: NERDTree
date: 2018-05-06 12:44:45 Sun
modify: 2018-05-06 12:44:45 Sun
tag: [frame]
categories: Vim
author: wmsj100
mail: wmsj100@hotmail.com
---

# NERDTree

## 概述
- 这个是左树的操作控件
- 创建快捷键的映射F3
	- map <F3> :NERDTreeMirror<CR>
	- map <F3> :NERDTreeToggle<CR>

## 操作
- :! vim h1.md 在指定的当前工作目录创建文件
- o 打开目录
- O 递归打开当前目录下所有的目录
- /index.html 在当前目录的展开的文件中查找文件
- m 在当前目录中打开编辑命令窗口
	- a 添加文件，输入文件名回车
	- d 删除文件
- p 跳到当前文件的父目录
- P 跳到根目录
- t 在新Tab中打开选择文件并跳到新Tab
- T 在新Tab中打开选择文件，不跳到新Tab
- x 合拢选择文件的父目录
- C 将选中的目录设置为根节点显示
- u 将当前根节点的父目录设置为根结点并且合拢原根节点
- U 将当前根节点的父目录设置为根结点并且保持原根节点的展开状态
- r 递归刷新选中目录
- R 递归刷新根结点
- m 显示文件系统菜单
- cd 将CWD设置为选中目录
- I 切换是否显示隐藏文件

## 切换标签页
- tabs 查看所有的标签
- tabc 关闭当前的tab
- tabo 关闭其他的tab
- tabp 查看前一个tab
- tabn 查看后一个tab
- gt 切换到后一个tab
- gT 切换到前一个tab

## 展开和折叠
- zc 折叠内容
- zv 展开折叠
- zR 展开所有折叠
