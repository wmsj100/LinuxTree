---
title: expect
date: 2020-04-12 18:58:08
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# expect

## 概要

- 是实现shell交互式的功能,
- `yum install expect`
- 常用来连接远端主机ssh

## 命令

- `spawn` 连接ssh的命令
- expect 期望获取的字符串,是按照正则匹配的
- send 发送的命令
- 可以是单行命令,也可以是多行命令,如果多行命令需要以`\r`结尾

## 范例

```
expect <<EOF
	set timeout -1
	spawn ssh 192.168.1.1 
	expect {
		"yes/no" { send "yes\n";exp_continue }
		"password" { send "$PASSWD\n" }
	}
	expect "]#"
	send "ls /root\r"
	expect "]#"
	send "exit\r"
	expect eof
EOF
```

## 参考

- [expect语法](http://xstarcd.github.io/wiki/shell/expect.html)
