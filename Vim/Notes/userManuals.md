---
title: 用户手册 
date: Sat 09 Dec 2017 10:14:55 AM CST
tag: [vim]
categories: Tools
author: wmsj100
mail: wmsj100@hotmail.com
---

## 常规命令
- set rtp? 查看vim的'runtimepath'路径字符串
- ctrl ] 跳转到目标链接
- ctrl o 回到上一次目标，回退
- ctrl t 撤销回退标签
- set showmode 显示vim当前模式
- Esc 回到普通模式

## vim 操作命令
- J 删除换行符
- ctrl r 回退
- u 撤销
- a/i 插入
- A 在行尾插入
- I 在行首插入
- o 在下一行插入
- O 在上一行插入
- 9k 向上移动9行
- 5dd 向下删除5行
- :e! 放弃修改重新装载原来的文件。
- 5w 向前跳过5个单词
- b 向后移动一个单词
- 5b 向后移动5个单词
- w 跳到下一个ie单词的词首
- e 跳到下一个单词的词末
- ge 跳到上一个单词的词末
- ^ 移动到一行的第一个非空字符
- 0 移动到当前行的第一个字符
- fx 在当前行向前查找第一个字符'x' f 是'find'查找的意思
- 3fx 在当前行查找第三个'x'字符
- Fx 向左查找第一个字符'x'
- tx 类似fx，只是移动到目标字符的前一个字符， t 是'to'到达的意思
- % 匹配配对的括号
- 33G 跳到33行
- %50 跳到中间位置
- %90 跳到文档90%
- H 'home' 跳到可视窗口的头部
- M 'middle' 跳到中间
- L 'last' 跳到可视末尾
