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

## expect 获取返回值

```shell
expectShell(){
expect <<EOF
	set timeout 3000
	spawn $@
	expect {
		"yes/no" { send "yes\n";exp_continue }
		"password" { send "$PASSWD\n" }
	}
	expect eof
	catch wait result
	exit [lindex \$result 3]
EOF
}
```
- 上面的result前面的`$`必须转义，否则会直接被shell翻译
- wait命令的返回值是一个"%d %s 0 %d"格式的字符串,第0个值是pid,第1个是spawn_id(不知道它具体带表了什么),第2个应当是代表脚本是否正常完成,第3个是子进程的返回值.
- result接收的是wait的返回值，lindex 表示取result的索引为3的值

## 参考

- [expect语法](http://xstarcd.github.io/wiki/shell/expect.html)
- [expect返回值](https://www.cnblogs.com/mthoutai/p/6807293.html)
