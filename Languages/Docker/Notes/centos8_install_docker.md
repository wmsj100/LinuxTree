---
title: centos8安装docker
date: 2020-03-04 20:58:17
modify: 
tags: [Notes]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# centos8安装docker

## 概要

- centos8安装docker没有Ubuntu安装顺畅，需要手动安装

## 步骤

- `sudo yum install docker-ce` 报错，提示container.io版本太低，需要手动安装
- `sudo yum install -y yum-utils  device-mapper-persistent-data  lvm2` 安装依赖
- `sudo yum-config-manager  --add-repo   https://download.docker.com/linux/centos/docker-ce.repo` 添加docker的源
- `sudo yum install docker-ce docker-ce-cli containerd.io` 安装还是报错说containerd.io版本太低
- `sudo dnf install https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/centos/7/x86_64/stable/Packages/containerd.io-1.2.6-3.3.el7.x86_64.rpm` 这是清华源，先安装containerd.io
- `sudo dnf install https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/centos/7/x86_64/stable/Packages/docker-ce-cli-19.03.7-3.el7.x86_64.rpm` 再安装最新版本的docker-ce-cli，因为docker-ce依赖这个，所以需要先安装
- `sudo dnf install https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/centos/7/x86_64/stable/Packages/docker-ce-19.03.7-3.el7.x86_64.rpm` 最后安装docker-ce
- 这样docker就安装好了，
- `sudo systemctl start docker`
- `sudo systemctl enable docker` 设置开机自启
- `sudo docker version` 可以看到docker已经成功安装

## 参考

- [centos8 docker install](https://www.cnblogs.com/zbseoag/p/11736006.html)
