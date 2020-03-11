---
title: basic
date: 2019-09-15 19:08:48 Sunday
modify:
tag: [basic]
categories: Docker
author: wmsj100
mail: wmsj100@hotmail.com
---

# basic

## 概述

- docker的基础知识

## 安装

- `wget -qO- https://get.docker.com/ |sh` 这样安装的是官方的最新版本，建议按照这个安装，而且这样安装的是社区版本。
- 镜像源安装
	- `https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/raspbian/dists/buster/pool/stable/armhf/`
	- 分析这个目录,一般选版本Linux/raspbian/dists/buster/pool/stable/armhf/ 这样就是镜像
	- 安装过程的顺序是containerd.io > docker-ce-cli > docker-ce
	- 安装时候都选最新版本安装
	- `wget https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/raspbian/dists/buster/pool/stable/armhf/containerd.io_1.2.6-3_armhf.deb`
	- `https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/raspbian/dists/buster/pool/stable/armhf/docker-ce-cli_19.03.7~3-0~raspbian-buster_armhf.deb`
	- `https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/raspbian/dists/buster/pool/stable/armhf/docker-ce_19.03.7~3-0~raspbian-buster_armhf.deb`

- 证书可选可不选,因为框架一般不需要那么频繁升级,手动添加docker证书
	- curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
	- sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
	- sudo apt update

- `sudo usermod -aG docker pi` 把当前用户添加到docker组

- sudo systemctl daemon-reload
- sudo systemctl restart docker
- `vi /etc/docker/daemon.json`
```json
{ 
"registry-mirrors": ["https://docker.mirrors.ustc.edu.cn"] 
}
```

## 查看运行状态

- `service docker status`
- `systemctl is-active docker` active

## 参考

