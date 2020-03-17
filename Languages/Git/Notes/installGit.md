---
title: 安装git
date: Mon 25 Dec 2017 11:53:05 PM CST
modify: 2020-03-17 13:47:04 
tag: [git,install]
categories: Git
author: wmsj100
mail: wmsj100@hotmail.com
---

# 安装git

- 通过地址[https://www.kernel.org/pub/software/scm/git/](https://www.kernel.org/pub/software/scm/git/);
	- tar -xzvf git.tar.gz -C /path
- 通过github下载git
	- `git clone git@gitee.com:mirrors/git.git` 这是国内码云一个加速镜像
- cd git
- `make configure` 编译configure文件
- ./configure --prefix=/usr/local/git --with-iconv=/usr/local/libiconv
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
