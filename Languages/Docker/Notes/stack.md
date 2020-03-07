---
title: stack
date: 2020-03-07 18:04:31
modify: 
tags: [Notes]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# stack

## 概要

- stack是docker内嵌的用来管理集群多应用部署的方案
- 之前service用来管理集群中的多个节点步骤一致的做一些动作,但是stack可以在不同节点部署不同应用,设置数据层的密钥
- stack是在service的基础上又进行的统筹管理,
- 使用stack就只需要修改`docker-stack.yml`配置文件就可以,剩下的操作docker会自动按照预期进行动作.
- 之前在service上做的操作现在stack全部接管了,但是还是可以通过`docker service ls/ps/scale`等进行操作,只是不建议那样,所有的改变都要在配置文件中作出然后重新部署升级

## 常用命令

- `docker stack ls`
- `docker stack deploy -c docker-stack.yml seastace` 部署一个stack
- `docker stack ps seastack` 查看stack的详情
- `docker secret create` 创建密钥
- `docker stack rm seastack` 删除
- `docker stack deploy seastack` 按照配置文件进行升级操作

## 参考

