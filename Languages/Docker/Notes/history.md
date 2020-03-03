---
title: history
date: 2020-03-03 20:07:21
modify: 
tags: [Notes]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# history

## 概要

- 可以查看docker执行某一动作

## 操作

- `docker image history web:latest` 查看构建镜像的过程中执行的指令
```
(py3env) ubuntu:~/Code/Docker/psweb-master$ docker image history web:latest
IMAGE               CREATED             CREATED BY                                      SIZE                COMMENT
dc892471b2f2        10 hours ago        /bin/sh -c #(nop)  ENTRYPOINT ["node" "./app…   0B
56b9d9277efa        10 hours ago        /bin/sh -c #(nop)  EXPOSE 8080                  0B
c1698e9fa23c        10 hours ago        /bin/sh -c npm install                          20.6MB
6c3f22c5d14d        11 hours ago        /bin/sh -c #(nop) WORKDIR /src                  0B
7028b220feb8        11 hours ago        /bin/sh -c #(nop) COPY dir:b1f9394c10dca7723…   2.29kB
eaa316212f7a        11 hours ago        /bin/sh -c apk add --update nodejs nodejs-npm   49.9MB
86b5d91abc93        11 hours ago        /bin/sh -c #(nop)  LABEL maintainer=nigelpou…   0B
e7d92cdc71fe        6 weeks ago         /bin/sh -c #(nop)  CMD ["/bin/sh"]              0B
<missing>           6 weeks ago         /bin/sh -c #(nop) ADD file:e69d441d729412d24…   5.59MB
```
- 从上面可以看到只有4个指令创建了了镜像层，就是那些`size`不为零的
- created by对应的是dockerfile文件的每一行

- 使用From指令引用官方基础镜像是一个很好的习惯，这是因为官方的镜像通常会遵循一些最佳实践，并且能规避一些已知问题。
- 使用from时候引用一个较小的镜像文件通常也能规避一些潜在的问题。

## 参考

