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

- `sudo apt install docker.io` 这样安装的版本较低
- `wget -qO- https://get.docker.com/ |sh` 这样安装的是官方的最新版本，建议按照这个安装，而且这样安装的是社区版本。
- sudo curl -sSL https://get.docker.com | sh

- `sudo usermod -aG docker pi` 把当前用户添加到docker组

- sudo systemctl daemon-reload
- sudo systemctl restart docker
- `vi /etc/docker/daemon.json`
```json
{ 
"registry-mirrors": ["https://docker.mirrors.ustc.edu.cn"] 
}
```

## 参考

