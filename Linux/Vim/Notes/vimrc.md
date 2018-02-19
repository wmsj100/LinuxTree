---
title: vimrc文件
date: Sat 09 Dec 2017 10:26:50 PM CST
tag: [vim,vimrc]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

## 简介
- set ruler 窗口右下角显示光标的位置
- map Q gq 设置键映射，用'Q'来完成'gq'
- :map \p i{<Esc>ea}<Esc> 使用'\p'来实现给单词添加'{}'功能
- set iskeyword& 如果搞乱了一个选项，可以在选项后面加上一个'&'来恢复到默认值。
- set nowrap 禁止折行
- set sidescroll=10 移动到不能显示的文字上时候，vim会自动向右滚动10个字符来显示内容。
