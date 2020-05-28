---
title: find
date: 2019-04-20 09:11:55	
modify: 2020-05-28 16:39:48 
tags: [find]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# find

- find命令的主要作用是沿着文件层次的结构向下遍历，匹配符合条件的文件，并执行相应的操作。

- print find将匹配的文件输出到标准输出
- exec find命令对匹配的文件执行该参数所给出的shell命令
- name 按照文件名查找
- type 查找某一类型的文件
- prune 使用这一选项可以是find命令不再当前指定的目录中查找
- user 按照文件属主来查找
- group 按照文件所属组来查找文件
- mtime -n +n 按照文件的更改时间来查找文件
	- -n 表示文件更改时间距离现在小于n天
	- +n 表示文件更改时间距离现在大于n天
- atime ctime
- path 路径， find . -type f ! -name "*.md" ! path "./.git/*" 在当前路径下搜索不是.md结尾的文件，并且过滤掉.git目录
- find . -newer test_exit.sh ! -path "./.git/*" -type f 查找一个文件，比`test_exit.sh`新，且不包含`.git`目录，且是文件

## 练习

- find . -print 打印当前目录下的文件目录列表，递归打印
- find -name "*.txt" -print 打印当前目录下的所有以“.txt”结尾的文件
- find -iname "*.txt" 忽略大小写
- find . \( -name "*.txt" -or -name "*.pdf" \) 打印当前目录下所有以".txt"/ ".pdf"结尾的文件名
- find . ! -name "*.txt" 打印当前目录下所有不以txt结尾的文件
- find -maxdepth 0 -name hello   在当前目录查找hello文件或目录
- find -name "[a-z0-9]*.txt"  在当前目录查找字母或数字名称的txt文件 \*
- find -empty  查找空白文件
- find -type f   查找当前目录下的文件
- find -size +100k -size -1024k 返回文件尺寸大于100k 小于1M的文件
- find -user testuser  查找文件属主是testuser 的文件或目录
- find -group 2000 查找文件组的属主是2000的文件或目录
- find -nouser  查找文件属主在/etc/passwd 中无法查找的文件
- find -nogroup 查找文件组属主在/etc/group 中无法查找的文件
- --这种文件是删除用户时候没有删除掉用户创建的文件时候产生的--
- find -perm 444 查找文件权限是444的
- find -perm +444 查找文件权限大于444的
- find -mtime 0 查找今天修改过的文件
- find -mtime 0 -name "*.js" -exec rm -fr {} \;  删除今天修改过的js文件；
- find -user root 查找root角色的文件
- find ! -user root 查找不属于root角色的文件

- xargs  这个命令和 -exec类似，但是这个比后者强大，因为某些发行版-exec参数只能调用很少的shell命令，而且长度有限制，而且某些发行版会为find搜索到的每一个文件启用一个cmd进程，这样会严重影响系统的性能，
- xargs cmd 把从管道获取的参数作为一个参数列表一次传给cmd程序。
- find -user root | xargs chmod -o-w  查找root的文件并且取消others的w权限

- suse系统的history 文件是一个空文件，这应该是安全设置。
- 遇到一个不认识的命令时候，先不要急着百度，先可以man一下，看这个是什么意思。

## 逻辑操作符
- and 俩边都为真，简写wei -a
- or 一个为真， 简写为-o
- not 匹配条件是假，简写为 ！
- () 显示的说明优先级，提高可读性，需要用反斜杠对括号进行转义

---

- find . -type l -name "*.txt" 打印当前目录下所有以txt结尾的符号链接 \*, 查找所有的软链接文件
- find . -type f -name "*.php" -perm 777 查找当前目录下的所有权限为777的php文件 \*
- find . -type f -user root 打印当前目录下所有root拥有的文件
- find . -type f \( ! -perm 777 -and ! -perm 644 \) 打印当前目录下所有权限不是777 和644的文件
- find . \( -newer test_export1.sh -or -name "test_f*" \) -type f ! -path "./.git/*" 查找文件比`test_export1.sh`新或者名称为`test_f`开头的类型是文件，且要过滤掉`.git`目录
- find -type f | egrep "\.(java|html)" 查找特定后缀的文件

## exec 高级命令
- find . -name "*.php" -exec ls -l {} \; 查找php文件并且显示其详情 \*
	- {} 是一个占位符，在find执行过程中会不断替换成当前找到的文件
	- \; 是-exec命令结束的标记，通过反斜杠进行转义。
- find . -newer test_func_return1.sh ! -path "./.git/*" -type f -exec ls -l {} \; \*
- find . -type f -user wmsj100 -exec cat {} \; > all.c 获取所有的wmsj100的文件并且输出到all.c
- find . -name "*.c" -exec ./command.sh {} \; 通常情况下-exec后面只能使用当个命令，如果使用多个命令，可以将多个命令写入sh文件，然后在-exec中使用这个脚本。

