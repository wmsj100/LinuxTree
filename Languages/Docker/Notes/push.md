---
title: push
date: 2020-03-05 09:38:33
modify: 
tags: [Notes]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# push

## 概要

- 推送镜像到远端docker hub中

## 流程

- 推送之前需要先登录docker hub用户
- `docker login` 输入用户名/密码，等待登录成功
- 给要push的镜像打合适的标签
- `docker image tag web_rasp:latest wmsj100/web_rasp:latest` 打标签到自己的域下
- `docker push wmsj100/web_rasp:latest` 开始推送镜像，等待上传成功
```
(py3env) ubuntu:~/Code/Docker$ docker image push wmsj100/web_rasp:latest
The push refers to repository [docker.io/wmsj100/web_rasp]
8eaa41667fe6: Pushed
6de209fb5f45: Pushed
a8e3a752a9ec: Pushed
2f1fbf8a0932: Pushed
latest: digest: sha256:4df31fa9eb8abc3760498ecab264b566a6255fb12c79367a870cf4c77285fe22 size: 1159
```
- 等待上传成功后就可以使用search功能查找了，这个有一个延迟，需要等待一会儿才可以看到
- 删除本地镜像后可以尝试下载镜像
```
(py3env) ubuntu:~/Code/Docker$ docker pull wmsj100/web_rasp:latest
latest: Pulling from wmsj100/web_rasp
3a2c5e3c37b2: Pull complete
53f9ec9a51a9: Pull complete
66685153b949: Pull complete
a38438b09ae2: Pull complete
Digest: sha256:4df31fa9eb8abc3760498ecab264b566a6255fb12c79367a870cf4c77285fe22
Status: Downloaded newer image for wmsj100/web_rasp:latest
docker.io/wmsj100/web_rasp:latest
```

## 参考

