---
title: 重定向
date: 2018-02-07
tag: [linux,shell]
categories: Linux
---

- cat > h1   会在界面输入内容，知道按下 ctrl + d   结束输入，
- cat h1 h2 > h3 把h1, h2俩个文件的内容输入到文件h3中

- 管道可以把一个命令的输出作为另一个命令的输入；

- tee 它把输出的一个副本输送到标准输出，另一个副本拷贝到相应的文件中
- who | tee who.out  同时有标准输出和输出到文件who.out

## 重定向  
- 标准输入的默认关联是键盘
- 标准输出的默认关联是屏幕
- 标准错误输出的默认关联也是屏幕
- 可以通过 > >> 进行重定向
- > h4  创建一个长度为0的空文件，如果文件存在，清空文件
- ll | grep ^d >> file.out 
- cat < file.out 以文件 file.out 作为标准输入
- sort < file.out 对文件的内容进行排序

- find ./ -name "*.txt" | xargs rm -rf {} \; 2 > /dev/null  把命令的错误消息丢弃

- find /etc -name "shadow" -print 1>ok.file 2>error.file  查看/etc目录下的shadow文件，如果标准输出是正确的，重定向到ok.file; 如果标准输出是错误的，输出到error.file

- cat < 1.txt > 2.txt

- find /etc/ -name "shadow" >> ok.1 2>&1  把正确和错误的标准输出都重定向到ok.1文件
- 2>&1 把标准错误重定向到标准输出

- && 一个命令执行成功另一个命令才会继续执行
- cp ./pub ./lib && rm -fr ./pub    执行复制操作执行成功，才会执行删除操作
- || 左边的命令执行失败，才会执行右边的命令
- cp /root ./ || echo "not has deal"

- ll /root || echo "error" | mail testuser; exit    读取/root 目录，如果失败，就发送一封邮件给testuser，并且退出当前shell。

## 匹配文本或过滤文本时候
- * 匹配零个或多个前面的字符
- ll | grep "er*or"   可以匹配  eor , eror, error, errrrrrrror 

- 可以使用正在表达式的三剑客
- grep , awk , sed
