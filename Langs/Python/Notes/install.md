---
title: CentOs7升级python3.6.3
date: 2018-10-02 07:00:41	
modify: 
tag: [basic]
categories: Python 
author: wmsj100
mail: wmsj100@hotmail.com
---

# CentOs升级Python3.6.3

## 概述
- CentOs系统默认安装的`Python2.7`,安装`Django`和`Flask`版本都太低了,所以需要手动下载安装包进行本地编译

## 步骤
- [python ftp](https://www.python.org/ftp/python/)地址选择下载的版本
	- `CentOs7.4`本地测试了好几个版本,最后测试的`Python 3.6.3`可以安装
	- [Python-3.6.3.tar.xz](https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tar.xz)
- `mkdir /home/software`在虚拟机创建下载目录
- `wget https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tar.xz`
- `tar -xvf Python-3.6.3.tar.xz`
- `cd Python-3.6.3`
- `./configure --prefix=/usr/loacl/python3`
- `./configure --enable-optimizations`
- `make` 
	- 这一步也可以`make && make install` 但我测试的总是失败,
	- 因为`make`这一步有测试的过程,测试的步骤有450多布,
	- 可能是我虚拟机的ssh连接设置有关系,等不到执行完成就自动断开连接了,
	- `top -i`命令查看`python`占用的cpu是不是从接近`100`到了`0`
	- 这个过程可能需要很久
- `make install`


## 参考
- [CentOS 7 安装Python3.7](https://www.cnblogs.com/linga/p/9442126.html)
