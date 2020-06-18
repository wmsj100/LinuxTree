---
title: jenkins-2.241-dockerfile
date: 2020-06-18 20:42:49
modify: 
tags: [Summary]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# jenkins-2.241-dockerfile

## 概要

- 这是我制作的第一个docker镜像，这个镜像制作很不容易，因为刚开始跑的make，需要验证所有的测试用例，结果很多都跑不过。
- 因为官方最新版本只到了2.86，而现在要制作2.241，版本差太多了，还有很多x86的二进制，需要一行一行的过，
- 幸运的是这个jenkin的构建的docker内容不多，只有100行左右，而且Dockerfile的语法其实很简单，熟悉之后就很容易修改了。
- 最大的困难是安装git-lfs失败，在本地是成功的，但是在容器中是失败的，一直很难定位，最后定位肯定是源的问题，然后就对比主机的repo文件，发现多了一个EPEL源
- 查询这个知道是fedora的源
- `yum install epel-release`然后就解决了。
- 纪念我第一次制作镜像文件

## 参考

