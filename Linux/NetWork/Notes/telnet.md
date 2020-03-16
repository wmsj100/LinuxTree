---
title: telnet
date: 2020-03-16 17:14:03
modify: 
tags: [Notes]
categories: NetWork
author: wmsj100
email: wmsj100@hotmail.com
---

# Telnet 协议

- 时Internet远程登陆服务的标准协议和主要方式，基于TCP，端口号23
- 终端使用者在本地电脑使用telnet程序，用它连接到服务器，在telnet程序中输入的命令，这些命令会在服务器上运行，就像直接在服务器的控制终端输入一样。
- telnet已经被ssh替代,因为它使用明文传输文件,可以被检测到

## 使用条件

- 在本地安装包含telnet协议的客户程序
- 必须知道远程主机的IP或域名
- 必须知道登陆标识和口令

- telnet 192.168.1.1  可以进行连接主机

- 感觉有点像XShell连接后台的方法，比如使用
ssh: 192.168.0.1
然后输入用户名和密码连接后台。

## 安装

- `sudo apt install openbsd-inetd`
- `sudo apt install telnetd`
- `/etc/init.d/openbsd-inetd restart`
- `ss -nltp` 查看23端口是否有监听
```
ubuntu@Ubuntu:~/Documents/Github/LinuxTree/Linux/NetWork/Notes$ ss -nltp
State    Recv-Q    Send-Q             Local Address:Port         Peer Address:Port
LISTEN   0         128                      0.0.0.0:22                0.0.0.0:*
LISTEN   0         128                      0.0.0.0:23                0.0.0.0:*
```
- `telnet 192.168.20.1` 然后就会通过telnet的协议登陆到主机,执行主机的命令,其实和ssh功能类似,只是ssh是加密协议更安全,现在已经被ssh取代了

## 范例

### 测试telnet是明文传输

- 通过telnet登陆主机,然后查看当前主机的内核版本
- 在另一个控制台开启对于23端口的监听
- `sudo tcpdump -nn -i eth0 port 23`
- `telnet 192.168.20.2`
- `uname -a`
- 查看tcpdump的打印
```
17:19:30.634355 IP 192.168.20.1.23 > 192.168.20.2.52160: Flags [P.], seq 11:125, ack 10, win 509, options [nop,nop,TS val 2992065282 ecr 185071418], length 114
	0x0000:  4510 00a6 4ed6 4000 4006 4218 c0a8 1401  E...N.@.@.B.....
	0x0010:  c0a8 1402 0017 cbc0 56a5 b1d6 ffc7 48aa  ........V.....H.
	0x0020:  8018 01fd 7688 0000 0101 080a b257 4b02  ....v........WK.
	0x0030:  0b07 f73a 4c69 6e75 7820 5562 756e 7475  ...:Linux.Ubuntu
	0x0040:  2035 2e33 2e30 2d34 322d 6765 6e65 7269  .5.3.0-42-generi
	0x0050:  6320 2333 347e 3138 2e30 342e 312d 5562  c.#34~18.04.1-Ub
	0x0060:  756e 7475 2053 4d50 2046 7269 2046 6562  untu.SMP.Fri.Feb
	0x0070:  2032 3820 3133 3a34 323a 3236 2055 5443  .28.13:42:26.UTC
	0x0080:  2032 3032 3020 7838 365f 3634 2078 3836  .2020.x86_64.x86
	0x0090:  5f36 3420 7838 365f 3634 2047 4e55 2f4c  _64.x86_64.GNU/L
	0x00a0:  696e 7578 0d0a                           inux..
```
- 从面板可以找到内核的打印内容,`Linux Ubuntu 5.3.0-42-generic #34~18.04.1-Ubuntu SMP Fri Feb 28 13:42:26 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux`
- 这个需要自己拼接一下
- 所以telnet是不安全的协议

### 测试ssh是密文传输

- `sudo tcpdump -nn -i eth0 port 22`
- `ssh ubuntu@192.168.20.1`
- `uname -a` 去tcpdump的控制台想清空内容,然后在回车打印内核版本
- 去tcpdump的控制台查看内容,发现都是乱码
```
17:23:36.018379 IP 192.168.20.2.22 > 192.168.20.1.60056: Flags [P.], seq 2405:2505, ack 900, win 501, options [nop,nop,TS val 185316831 ecr 2992310666], length 100
	0x0000:  4510 0098 ba03 4000 4006 d6f8 c0a8 1402  E.....@.@.......
	0x0010:  c0a8 1401 0016 ea98 e102 1898 9b01 f498  ................
	0x0020:  8018 01f5 c514 0000 0101 080a 0b0b b5df  ................
	0x0030:  b25b 098a 1179 6fcc 84c4 dbaf e55f eec8  .[...yo......_..
	0x0040:  c218 41d7 f72d 59ea 0e68 70c0 1ba9 030d  ..A..-Y..hp.....
	0x0050:  cc79 c469 4339 94c2 578a ffbe 0ef1 8e32  .y.iC9..W......2
	0x0060:  ab07 2e01 399c fe2b 73c5 e5a9 a71e def7  ....9..+s.......
	0x0070:  5ad9 8e24 00b5 aa55 8403 2408 8353 ab94  Z..$...U..$..S..
	0x0080:  0712 5ad0 9d8e c256 fdf0 2a78 93a2 1174  ..Z....V..*x...t
	0x0090:  cb42 5cc4 363d c649                      .B\.6=.I
```
- 上面那些是用公钥加密过的内容,只有用私钥解密才可以读取内容
- 所以ssh是安全的协议

## 参考

- [telnet 使用](https://blog.csdn.net/weixin_44536709/article/details/86654718)
