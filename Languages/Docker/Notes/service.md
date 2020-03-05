---
title: service
date: 2020-03-04 15:21:48
modify: 
tags: [Notes]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# service

## 概要

- docker的service是基于swarm集群的
- service是用于集群中dockers节点的业务管理

## 操作

- `docker service ls` 查看当前集群中的service清单
- `docker service create --name web-fs -p 8011:8080 --replicas 3 wmsj100/web:latest` 在当前集群中创建一个service，保持3的容器运行，分布式部署
	- 映射主机端口8011到dockers的8080端口
	- service名称为web-fs,可以通过名称来查看service的其他信息，
	- replicas 3 同时保持3个docker容器，如果有一个容器异常挂机了，service会自动重新拉起一个容器来保证总数为3，
- `docker service ps web-fs` 查看当前service的细节
- `docker service rm web-fs` 删除service
- `docker service inspect --pretty web-fs` 查看服务的详细信息

## 全局模式

- service默认复制模式是副本模式，这种模式会部署期望熟练的服务副本，并尽可能均匀地将各个副本分布在这个集群上
- 全局模式: 每个节点上仅运行一个副本
- `docker service create --mode global` 这样创建的就是全局模式
- 全局模式不需要指定replicates

## 服务扩/缩容

- `docker service scale web-fs=10`可以把服务副本数从5个增加到10，

## 滚动升级

- `docker service update --image wmsj100/web:v2 --update-parallelism 2 --update-delay 20s web-fs`
- 升级service web-fs，每次升级俩个节点，每次升级间隔20s

## 指定覆盖网络创建服务

- `docker network create -d overlay uber-net`
- `docker network ls` 查看创建的覆盖网络
- `docker service create --name web-fs --network uber-net -p 8011:8080 --replicates 12 wmsj100/web:latest`
- 指定服务网络uber-net来创建service web-fs, 集群创建12个容器

## 日志

- `docker service logs web-fs` 查看当前service的日志

## 参考

