---
title: ossutil
date: 2020-02-21 14:26:12
modify: 
tags: [Notes]
categories: OSS
author: wmsj100
email: wmsj100@hotmail.com
---

# ossutil

## 概要

- 这是一个命令行的oss管理工具

## 安装

- wget http://gosspublic.alicdn.com/ossutil/1.6.10/ossutil64       
- chmod 755 ossutil64    
- 可以把该工具放置到path路径的文件夹内部，直接执行ossutil64命令

## 配置

- ./ossutil64 config
- 输入配置文件名，默认在~/.ossutilconfig
- 输入endpoint bucket的外网url
- 输入accessKeyID
- 输入accessKeySecret
- 输入stsToken 不输入，直接回车
- 然后就会生成配置文件

## 常用命令

- 增加
	- appendfromfile 将本地文件内容以追加上传的方式上传到bucket的object内
- 查看
	- ossutil64 cat oss://wmsj100-python-test/python-notes/updateVersion.md 查看文件的内容，只查看文本文件内容
- 查看占用空间
	- du
	- ossutil64 du oss://wmsj100-python-test
	- ossutil64 du oss://wmsj100-python-test/image
- hash 
	- ossutil64 hash .bashrc --type=md5
	- ossutil64 hash .bashrc
- 查询
	- ossutil64 ls oss://wmsj100-python-test/python-notes -s 简单输出
	- ossutil64 ls oss://wmsj100-python-test/python-notes -d 只输出目录
	- ossutil64 ls oss://wmsj100-python-test/python-notes -s --limited-num=5 限制输出5条
- 创建buckte存储空间
	- ossutil64 mb oss://wmsj100-test1 bucket名称必须唯一
- mkdir 创建目录
	- ossutil64 mkdir oss://wmsj100-test1/test2/test3
- rm 删除操作,删除bucket、object、file
	- ossutil64 rm -b oss://wmsj100 删除空的bucket，bucket在所有用户中共享
	- ossutil64 rm -rb oss://wmsj100 如果删除的bucket不为空，可以通过r递归删除，危险操作
	- ossutil64 mkdir oss://wmsj100/test4 删除单个object 只能删除空的object
	- ossutil64 rm -r oss://wmsj100/test4 递归删除test4对象的所有文件，
		- 因为oss没有目录层级的概念，所以其实上面的操作就是删除所有前缀的文件
	- ossutil64 rm -r oss://wmsj100-python-test/python-notes/ --exclude "README.md" 不包括文件删除全部
	- ossutil64 rm -r oss://wmsj100-python-test/python-notes/ --include "README.md" 只删除文件
- cp 上传文件
	- ossutil64 cp .vimrc oss://wmsj100-python-test/ 上传单个文件进行复制
	- ossutil64 cp -r $python oss://wmsj100-python-test/notes 通过r进行递归上传文件夹到bucket的object
	- ossutil64 cp -r $python oss://wmsj100-python-test/notes --include "digui.md" 披露上传符合条件的文件
	- ossutil64 cp -r $python  oss://wmsj100-python-test/notes -u 添加-u参数只有文件有更新才替换，否则跳过目标文件
	- ossutil64 cp -r oss://wmsj100-python-test/notes /tmp/tmp 递归下载远端文件夹到本地目录
	- ossutil64 cp -r oss://wmsj100-python-test/notes /tmp/tmp -u 只有远端文件有更新才下载文件到本地
	- ossutil64 cp -r oss://wmsj100-python-test/ /tmp/tmp --only-current-dir 仅复制当前目录下的文件，忽略子目录

## 参考

