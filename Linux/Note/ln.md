----
title: ln
date: Mon 19 Feb 2018 09:29:02 AM CST
tag: [linux]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

- ln -s /var/tmp   ./tmp   在当前目录内创建一个快捷方式，指向/var/tmp
- ln  是创建软连接的意思。
- 虽然软连接指向的是一个目录，但是通过 rmdir 来删除软连接会报错，所以知道软连接本身是一个连接文件，
