---
title: 创建镜像文件
date: Sun 18 Feb 2018 11:09:24 PM CST
tag: [linux,static,cmd]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

- mkisofs 通过这个命令可以创建镜像文件，
- mkisofs -r -o git.iso -graft-point /home/wmsj100/Documents/git 通过这个命令就创建了git的镜像文件
- mount git.iso /media/img  通过这个命令就可以加载镜像文件，但是这样加载的文件系统是只读的，文件系统内部的文件是不可以被编辑或删除的。
