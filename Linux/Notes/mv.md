---
title: mv
date: Mon 19 Feb 2018 09:29:02 AM CST
tag: [linux]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---
# mv 移动或更名文件或文件夹

- 经常用来备份文件或者目录
	- b --back 若覆盖文件，这覆盖前先进行备份
	- f --force 如果目标存在，不会询问直接覆盖
	- i --interactive 若目标存在会进行询问
	- u --update 若目标文件已经存在， 且源文件比较新，才会更新，就是用源文件替换目标文件
	- t --target 该选项用于移动多个源文件到一个目录的情况，此时目标文件在前，源文件在后。

- mv t2 t1
	- 若t1目录不存在，则将t2重命名为t1
	- 若t1目录存在，则将t2移动到t1目录内
