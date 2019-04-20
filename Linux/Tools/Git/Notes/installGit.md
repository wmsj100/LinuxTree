---
title: 安装git
date: Mon 25 Dec 2017 11:53:05 PM CST
tag: [git,install]
categories: Git
author: wmsj100
mail: wmsj100@hotmail.com
---

# 安装git
- 通过地址[https://www.kernel.org/pub/software/scm/git/](https://www.kernel.org/pub/software/scm/git/);
- tar -xzvf git.tar.gz -C /path
- cd path
- ./configure
	- error: [处理办法](http://blog.csdn.net/konga/article/details/41383543)
	- yum install zlib
	- yum install zlib-devel
- make
	- error: [处理办法](http://blog.csdn.net/w_yunlong/article/details/70047050)
	- 解决，安装 install perl-ExtUtils-CBuilder perl-ExtUtils-MakeMaker 即可：
	- yum install perl-ExtUtils-CBuilder perl-ExtUtils-MakeMaker
- make install 
	- error 提示权限不足，给wmsj100添加root权限
	- sudo make install 
- make clean 删除编译时候生成的临时文件
