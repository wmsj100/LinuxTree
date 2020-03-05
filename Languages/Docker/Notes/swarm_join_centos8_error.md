---
title: swarm_join_centos8_error
date: 2020-03-05 10:14:57
modify: 
tags: [Notes]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# swarm_join_centos8_error

## 概要

- 在centos8主机创建swarm集群，然后通过树莓派来接入集群
- 接入集群时候报错
```
(virtualenv) pi@raspberrypi:~/Documents/Docker $ docker swarm join --token SWMTKN-1-5yfni7i29sw7sa4juzdcjwi7mmho8w6zbjfzh7gqgvz163clxb-d3pyiw1ex5tzdrqzbcqnn03w5 192.168.0.103:2377 --advertise-addr 192.168.0.102:2377 --listen-addr 192.168.0.102:2377
Error response from daemon: rpc error: code = Unavailable desc = all SubConns are in TransientFailure, latest connection error: connection error: desc = "transport: Error while dialing dial tcp 192.168.0.103:2377: connect: no route to host"
```
- 猜测应该是centos的端口没有放开，应该是防火墙的原因
- 在centos开启防火墙端口，然后重新连接就成功了

## 参考

