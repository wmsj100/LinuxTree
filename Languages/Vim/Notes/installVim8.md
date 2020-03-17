---
title: 安装vim8
date: 2018-05-07 00:43:22 Mon
modify: 2020-03-17 13:09:21 
tag: [update]
categories: VIM
author: wmsj100
mail: wmsj100@hotmail.com
---

# 安装vim8

## 概述

- 之前很多次都想要升级vim8，因为我使用的版本太低了，安装的插件无法使用，但是之前是苦于无法下载vim8，
- 现在vim已经转移到了github，所以下载就完全不是问题了。
- cd vim/src
- ./configure --with-features=huge --enable-pythoninterp --with-python-config-dir=/usr/lib/python2.7/config/ --enable-python3interp --with-python3-config-dir=/usr/local/lib/python3.6/config-3.6m-x86_64-linux-gnu/ --enable-multibyte --enable-cscope --enable-gui=auto --enable-xim --with-x --enable-fontset --disable-selinux
- centos x86_64架构,安装方式
- `./configure --with-features=huge --enable-pythoninterp --with-python-config-dir=/usr/lib64/python2.7/config/ --enable-python3interp --with-python3-config-dir=/usr/lib64/python3.6/config-3.6m-x86_64-linux-gnu/ --enable-multibyte --enable-cscope --enable-gui=auto --enable-xim --enable-fontset --disable-selinux`
- sudo make
- export PATH=/usr/local/bin:$PATH

## 编译报错

- `You need to install a terminal library; for example ncurses.`
- `sudo yum install ncurses-devel` 安装这个库就可以编译成功了.

