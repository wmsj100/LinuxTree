---
title: last
date: 2020-04-09 10:01:55
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# last

## 概要

- last是用来查看登录记录的工具，查看之前登录当前主机的ip

## 总结

- 如何修改last信息，last的信息存储在/var/log/wtmp，但这个文件是一个二进制文件
- `utmpdump /var/log/wtmp > /tmp/wtmp.file`
- `vi /tmp/wtmp.file` 修改信息
- `utmpdump -r < /tmp/wtmp.file > /var/log/wtmp`
- 这样修改之后，history中还有记录，这个也需要清除

## 参考

- [last](https://blog.csdn.net/chuzhenge9382/article/details/100907642)
