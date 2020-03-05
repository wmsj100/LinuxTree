---
title: network
date: 2020-03-05 12:49:06
modify: 
tags: [Notes]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# network

## 概要

- docker的网络支持CNM标准(container network model)
- libnetwork是对CNM的实现
- 驱动时网络的数据层，内置bridge/overlay等网络
- docker创建容器时默认创建Bridge(单机桥接网络)，每个docker主机都有一个默认的单机桥接网络。
- 创建容器时如果不指定网络默认都接入该网络
- 默认的`bridge`网络被映射到内核中为`docker0`的linux网桥。

## 常见操作

- `docker network inspect uber-net` 查看当前网络的详情
- `docker network create --driver bridge localnet` 这样可以创建一个bridge驱动的localnet网络
- `sudo apt install brctl`
- `brctl show` 可以看到当前bridge的所有网络类型
```
(virtualenv) pi@raspberrypi:~ $ brctl show
bridge name     bridge id               STP enabled     interfaces
br-654b5e7c1685         8000.0242353834ce       no
docker0         8000.02427e9234ca       no
docker_gwbridge         8000.0242f9a07e05       no              vethdcdd6e3
```
- 上面br-654b5e7c1685就是和localnet对应的网桥
- `docker container run -d --name c1 --network localnet alpine sleep 1d` 接入localnet的一个容器
- `docker network inspect localnet`可以看到containers里面由c1这个容器接入。

## 注意

- docker默认的Bridge网络是不支持通过Docker DNS服务进行域名解析的，但是自定义的网络可以
- 比如上面在localnet网络中创建了俩个容器c1/c2,在c2容器中是可以ping c1的
```
/ # ping c1
PING c1 (172.20.0.2): 56 data bytes
64 bytes from 172.20.0.2: seq=0 ttl=64 time=0.166 ms
64 bytes from 172.20.0.2: seq=1 ttl=64 time=0.138 ms
64 bytes from 172.20.0.2: seq=2 ttl=64 time=0.141 ms
```

## 端口映射

- 桥接网络中的容器只能于相同网络中的容器通信
- 通过端口映射把容器的端口和主机的端口进行映射，这样所有发送到主机指定端口的流量，都会被全部转发到容器对应的端口上
- `docker container run -d --name web --publish 5000:80 --network localnet nginx:latest` 创建一个nginx的容器，把主机的5000端口映射到容器的80端口上
- 其实从上面这个操作就可以看出容器的可能性了，之前是通过在主机部署一个nginx来接管指定端口，现在可以通过指定端口分别来部署不同的nginx，而且还可以通过部署多个nginx容器来组成负载均衡，这样就给出了很多可能性。
- `docker port web`来查看web使用的端口
- 从上面端口映射我已经看到了很多可能性，但是文章说这很局限，只适用于本地开发或者是很小的应用，因为一个端口被一个容器占用后就不能被另外的容器占用了。

## 参考

