---
title: ulimit文件系统及程序限定
date: Tue 20 Feb 2018 04:24:10 PM CST
tag: [linux]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

- ulimit 可以限定用户的系统资源，比如打开的文件数量/ 使用的cpu时间/ 可以使用的内存总量。。
- ulimit -a 列出所有限定额度
- ulimit -f 设定可以创建的最大文件容量，如果一般用户一旦设定了这个值，则只能继续减小，不能增大。单位时KB；如果想要复原设置，最简单的方法就是注销再登陆。
