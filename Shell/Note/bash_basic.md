---
title: bash_basic.md
date: Sun 03 Dec 2017 06:48:34 PM CST
tag: []
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

- 创建一个shell脚本后有以下几种方式来执行
	- sh test.sh
	- bash test.sh
	- source test.sh
	- 修改脚步权限，添加执行 chmod u+x test.sh ./test.sh
		- 可执行文件会绿色显示。

## 实例
'''bash
#!/bin/bash
echo "Hello World" > my.txt
'''
- 执行脚本会在脚本所在路径生成my.txt文件

- 利用“/dev/null”创建清楚日志的脚本
'''bash
#!/bin/bash
LOG_DIR=/var/log
cd $LOG_DIR
cat /dev/null > wtmp
echo "Logs cleaned up."
exit
'''

## 总结
- cat /dev/null > /var/log/wtmp 提示权限不足
- sudo cat /dev/null > /var/log/wtmp sudo只能让cat命令以sudo权限执行，而对于“>“并没有sudo权限
- sudo sh -c "cat /dev/null > /var/log/wtmp" 这样整个命令都具有sudo权限
