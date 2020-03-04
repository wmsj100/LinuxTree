---
title: swarm
date: 2020-03-04 08:17:58
modify: 
tags: [Notes]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# swarm

## 概要

- swarm是docker提供的集群管理和业务编排功能
- 不包含在任何swarm中的docker节点被称为运行于单引擎模式，
- 加入swarm集群，则切换为swarm模式

## 使用

- `docker swarm init` 切换到swarm模式，并创建一个新的swarm，将自身设置为swarm的第一个管理节点。
- docker swarm默认监听2377端口，与swarm安全通信，这个端口是约定俗成的。
- `docker node ls` 查看swarm中的节点
- `docker swarm join-token worker` 获取添加新的工作节点到swarm
	- `docker swarm join --token SWMTKN-1-2cb1sz1gh9by9497ouqyx0cpaznb4yjb7yqcgf16jf9lu80a20-arq9p3z743i216pocjn5c0fsn 192.168.0.102:2377`
- `docker swarm join-token manager` 获取添加新的管理节点到swarm
	- `docker swarm join --token SWMTKN-1-2cb1sz1gh9by9497ouqyx0cpaznb4yjb7yqcgf16jf9lu80a20-ezia9m02gec7ozzk5nc0zfmej 192.168.0.102:2377`
- `docker swarm init --advertise-addr 111.229.241.222:2377 --listen-addr 172.17.0.13:2377`
	- 对于公有云这样的主题，在初始化swarm时候，需要配置地址ip和监听ip，
	- advertise-addr: 用来指定其他节点连接到当前管理节点的ip和端口，使用公网ip
	- listen-addr: 用来承载swarm流量的ip和端口，需要指定本机的局域网ip和端口
- `docker node ls` 查看swarm节点
```
(py3env) ubuntu:/tmp/tmp$ docker node ls
ID                            HOSTNAME            STATUS              AVAILABILITY        MANAGER STATUS      ENGINE VERSION
obtqji3qrbzqeqnakeflzlvec *   VM-0-13-ubuntu      Ready               Active              Leader              19.03.6
hyevys1afw0jdyacwrv4pd8v3     ip-10-23-186-31     Ready               Active                                  1.13.0
```
- `docker swarm update --autolock=true` 可以锁定主管理节点，这样重启管理节点后其他管理节点并不会自动结果管理权限，需要生成的key值来授信，重新在lock管理节点输入`docker swarm unlock`,然后输入lock生成的key值，这样可以重新接入swarm，执行`docker node ls`也可以重新看到节点信息了。

## 参考

