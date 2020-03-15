---
title: ss
date: 2020-03-15 21:30:25
modify: 
tags: [Notes]
categories: NetWork
author: wmsj100
email: wmsj100@hotmail.com
---

# ss

## 概要

- ss: Socket Statistics 用来获取sockets的统计信息
- 它用来替代netstat
- 优势在于能够提供更多更详细的有关TCP和连接状态的信息,
- ss比netstat快速的原因在于它利用了TCP协议栈中的tcp_diag

## 常用命令

- -h --help  this message
- -V --version output version information
- -n --numeric don't resolve servise names
- -r --resolve resolve host names
- -a --all display all sockets
- -l --listening display listening sockets
- -o --options show timer information
- -e --extended show detailed socket information
- -m --memory show socket memory usage
- -p --processes show process using socket
- -i --info show internal TCP information
- -s --summary show socket usage summary
- -4 --ipv4 display only IP version 4 sockets
- -6 --ipv6 display only IP version 6 sockets
- -0 --packet dispaly PACKET sockets

## 参考

- ss -h 帮助文档
- man ss
