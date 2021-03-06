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
- `docker stack service seastack` 查看当前stack的具体service部署情况
```
ubuntu@wmsj100:~/Templates/atsea-sample-shop-app$ docker stack services seastacks
ID                  NAME                        MODE                REPLICAS            IMAGE                                                     PORTS
1x22smaeuitj        seastacks_database          replicated          1/1                 dockersamples/atsea_db:latest
b32uws8etc8j        seastacks_appserver         replicated          2/2                 dockersamples/atsea_app:latest
ipm2cl43y49z        seastacks_payment_gateway   replicated          1/1                 dockersamples/atseasampleshopapp_payment_gateway:latest
nbbtr59nrk6n        seastacks_visualizer        replicated          1/1                 dockersamples/visualizer:stable                           *:8001->8080/tcp
z82pyvp4iko5        seastacks_reverse_proxy     replicated          1/1                 dockersamples/atseasampleshopapp_r
```

## 总结

- 使用stack技术完全不用单独去设置环境,包括网络和挂载卷,这些都是在配置文件写好然后执行时候自动创建和卸载网络,
- 但是使用service不同,需要单独配置网络,事后也需要单独去清除环境
- stack完全是自动化的过程

## 参考

