---
title: 多窗口编辑
date: 2017-12-11 11:06
tags: [vim]
categores: Linux
---

- :split 把屏幕分成上下俩个窗口，并把光标置于上面的窗口中
- :close 关闭窗口，这个命令和':q'的区别在于如果只剩下一个窗口，':close'不会关闭，而其它关闭命令会关闭。
- :only 关闭除当前窗口外的所有其它窗口
- :split 1.html 用另一个文件'1.html'文件切割当前窗口
- :new 分隔一个空白窗口
- :3split alpha.c 创建一个只有3行高度的窗口
- ctrl w + 可以增加一行窗口的高度
- ctrl w - 可以减少一行窗口的高度
- 4 ctrl w + 可以增加4行窗口的高度
- 20 ctrl w _ 通过下划线可以指定窗口的高度
- ctrl w _ 尽可能大的扩大窗口
- :vsplit 打开垂直窗口
- :vsplit two.c 在垂直窗口打开文件'two.c'
- :vnew 或者 :vertical new 会打开一个新的空白垂直窗口
- ctrl w j 跳到下面的一个窗口
- ctrl w k 跳到上面的一个窗口
- ctrl w h 跳到左面的一个窗口
- ctrl w l 跳到右面的一个窗口
- ctrl w b 跳到最下面的一个窗口
- ctrl w t 跳到最上面的一个窗口
- ctrl w J 把当前窗口重新布局到最下面横向展示
- ctrl w H 把当前窗口重新布局到最左边展示
- ctrl w L 把当前窗口重新布局到最右边展示
- ctrl w K 把当前窗口重新布局到最上面展示
- :qall 关闭所有的窗口
- :wall 保存所有的窗口内容
- :wqall 保存所有修改过的文件并退出
- :qall! 放弃修改并强制关闭所有的窗口
- vim -o one.txt two.txt three.txt 为每一个文件打开一个窗口
- vimdiff one.c one.c.bak 查看俩个文件的差异
- :vertical diffsplit one.bak 在vim内部通过这个命令查看文件的区别

- zo 打开一个折叠
- zc 关闭一个折叠
- :set noscrollbind 取消滚动绑定
- ]c 跳到下一个不同的位置
- [c 跳到上一个不同的位置
- dp 把左边的内容拷贝到右边，消除差异

## 标签
- :tabedit thatfile 会创建一个新的标签，在新标签页中编辑文件'thatfile'
- gt 会在标签页中进行跳转 goto tab
- :tab split 会以当前编辑文件创建一个新的标签页，
- :2tabNext 跳到下俩个标签
- :-2tabNext 跳到上俩个标签
- :tabonly 关闭所有其它标签，
