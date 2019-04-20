---
title: 安装vim8
date: 2018-05-05 23:51:21 Sat
modify: 2018-05-05 23:51:21 Sat
tag: [vim]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

# 安装vim8

## 概述
- yum install vim 这样只能安装到vim7,如果使用插件，会提示版本低
- 升级gcc
- sudo yum install centos-release-scl -y
- sudo yum install devtoolset-3-toolchain -y
- sudo yum install gcc-c++
- sudo scl enable devtoolset-3 bash
- yum install ncurses-devel

## 下载vim
- git clone https://github.com/vim/vim.git
- cd vim/src
- ./configure --with-features=huge -enable-pythoninterp --with-python-config-dir=/usr/lib/python2.7/config
- sudo make
- sudo make install
- export PATH=/usr/local/bin:$PATH

- [参考资料](https://blog.csdn.net/nzyalj/article/details/75331822)

