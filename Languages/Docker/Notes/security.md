---
title: security
date: 2020-03-07 22:42:50
modify: 
tags: [Notes]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# security

## 概要

- docker的安全是基于linux的安全策略来保证的,而且还进行了扩展

## 安全策略

### Linux安全策略

- Namespace命名空间,用于资源隔离,保证安全
- Control Group,用于资源使用的配额分配,控制资源使用
- Capability: 允许用户暂时提升为root权限来执行特点任务,比如修改文件所有权,绑定socket到系统端口号,提升进程优先级,重启系统
- MAC强制访问控制:比如SElinux技术
- Seccomp安全计算,限制容器对宿主机内核发起系统调用

### Docker平台安全技术

- Swarm模式
	- 是Docker未来的趋势,支持用户集群化管理多个Docker主机
	- 同时还能通过声明式的方式部署应用
	- 每个swarm都由管理者和工作者节点构成
	- 节点可以是linux或者windows
	- 管理者节点构成了集群中的控制层,并负责集群配置以及工作负载分配
	- 工作节点就是运行应用代码的容器
- Swarm模式提供很多开箱即用的安全特性,同时还设置了合理的默认值
	- 加密节点ID
	- 基于TLS的认证机制
	- 安全准入令牌
	- 支持周期性证书自动更新的CA配置
	- 加密集群存储(配置DB)
	- 加密网络
- TLS和双向认证
	- 每个加入swarm的管理者或者工作者都需要发布自己的客户端证书.这个证书用于双向认证.
	- 证书中定义了节点相关信息
	- `docker swarm update --cert-expiry 720h` 设置CA证书过期时间为30天
	- `docker swarm ca` 查看ca
- 集群存储
	- 保存了集群配置和状态数据
	- 基于etcd的某种实现,并且会在swarm内所有管理者之间进行自动复制
	- 存储默认也是加密的.
	- swarm模式在docker规划中占据重要地位,如果不是用swarm模式运行docker,很多docker特性无法使用.
- Docker安全扫描
- Docker内容信任
- Docker密钥

## 参考

