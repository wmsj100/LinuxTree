---
title: 重复输入和外置命令
date: 2017-12-14 10:19:12
tags: [vim]
categories: Linux
---

## 重复

- gv 在可视模式下编辑的文本，通过这个命令可以重新选中刚刚选中的文本，不管当前光标是否有选中文本
  - v select word
  - :s/2000/2002/g
  - gv
  - :s/2003/2001/g

- ctrl a 递增
  - /19[0-9][0-9]\|20[0-9][0-9] 按下enter来查找到年份，
  - ctrl a 在找到的值按下'ctrl a'，会在当前值上面递增1，重复按'.'可以继续递增
  - 9ctrl a 在当前值的基础上递增9
- ctrl x 递减
  - 9 ctrl x 在当前值基础上递减9

## 多个文件替换内容
- :args *.c 把当前目录的所有'.c'文件添加到列表
- :argdo %s/\<hello\>/HELLO/ge | update 
  - 对于所有的列表文件使用全局替换，'e'即使文件内没有要替换的目标也不会中断，
  - | 分隔俩条命令，
  - update 将那些有改动的文件存盘
- :windo 这个命令作用与所有当前窗口打开的文件，然后执行要替换的命令

## 编辑标准流中的内容
- ls | vim - 这个命令会把'ls'命令输出的标准流通过'vim'直接开始编辑，这省去了重新创建一个文件，然后把标准流的内容重定向到文件中

## 编辑外置vim批处理命令
"change.vim"
```shell
  %s/\<hello world\>/<h1>Hello World<\/h1>/g
  write tempfile
  quit
```
- cat *.md | vim -S change.vim - 通过这个命令来从标准输入中读取文本并且处理

