---
title: shell基础概念
date: Sun 03 Dec 2017 06:48:34 PM CST
tag: [shell]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

## shell功能
- 命令记忆功能
- 命令和文件名补全
- 命令别名设置alias
- 作业控制/前台/后台控制
- 程序脚本
- 通配符

- type 通过type可以知道命令是内置命令还是外部命令或者是命令别名

- 变量 可以用一个固定的字符表示变动的内容，比如Mail可以针对不同登陆用户获取到相应的邮件。

- 通过echo可以读取到变量的名称
- 变量赋值时等号左右不能有空格
- 变量值可以用双引号或单引号包裹，但是双引号内的$变量名可以获取到值
    - info="$name's ens is $LANG" 这样时可以读取到正确的内容的，如果换作单引号时就不生效了。

- 在命令行中输入其它命令有俩种方法，
    - info=$(uname -r)
    - info=`uname -r`
- 如果要增加变量的内容时候有下面方法：
    - name="$name":home   内容不能输入空格
    - name=$name:mail  这样效果同上
    - info="${info} also is good"  这样的方式内容可以输入空格
- export 这个操作会让变量成为环境变量，可以在子进程中获取到。因为一般情况下父进程中的自定义变量时无法在子进程内使用的。
    - export info
    - bash 进入子进程
    - echo $info
- 系统变量使用大写，用户自定义变量使用小写
- unset 取消变量，
    - unset info  这样再去读取变量info时候就是空
- test=$(pwd) 这样就把当前目录保存在变量test中，之后就可以使用`cd $test`来进入目录了。

## shell脚本执行方式

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

- 利用“/dev/null”创建清除日志的脚本
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
