---
title: ssh-copy-id
date: 2020-03-14 22:43:36
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# ssh-copy-id

## 概要

- 这个命令是用来管理传输公钥给远端主机的,这样主机彼此连接就不用再进行密码验证了,可以直接scp/ssh连接
- 之前理解就是通过ip来验证的,假如我主机的ip变更了,密钥就得重新验证了.
- 刚刚通过网线连接了树莓派然后指定了树莓派的本地ip后才发现之前的理解是错误的
- 密钥是针对用户角色来定义的,而且验证也是去当前用户的家目录`/home/pi/.ssh/id_rsa.pub`去验证这个文件的,
- 通过ssh的协议访问是会用本地`/home/.ssh/id_rsa`私钥加密,然后服务器那边会查看自己的`/home/.ssh/authoized_keys`是否有合适的公钥可以解密,
- 如果遍历过之后发现有公钥可以解密,就告知客户端验证通过,可以访问服务器通过ssh协议
- 所以如果只是访问同一个服务器只是变更服务器ip地址,因为ssh访问时加密的私钥是相同的,所以公钥也是相同的,所以不同ipssh连接时候都可以验证通过.

## 命令

- `ssh-keygen` 创建密钥
	- `ssh-keygen -t dsa`
	- `ssh-keygen -t rsa`
	- `ssh-keygen -t rsa1`
