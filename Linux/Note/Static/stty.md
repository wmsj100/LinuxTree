---
title: stty终端机的环境设置
date: Wed 21 Feb 2018 09:31:40 AM CST
tag: [linux,conf,sys]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

## stty
- stty (setting tty)设置终端机环境
- stty -a 列出所有的环境信息;^ 表示ctrl
    - eof ctrl+d  end of file 结束输入
    - erase ctrl+? 向后删除字符
    - kill ctrl+u 删除目前命令行上的所有文字
    - start ctrl+q 在某个进程停止后，重新启动它的输出
    - stop ctrl+s 停止目前屏幕的输出

## set 
- set 终端机添加自定义设置
- set -u 当使用未定义的变量时会显示错误

- 这些设置一般不建议修改
