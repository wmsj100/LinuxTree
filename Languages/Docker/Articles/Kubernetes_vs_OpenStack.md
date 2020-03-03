---
title: Kubernetes vs OpenStack
date: 2020-03-03 23:58:42
modify: 
tags: [Articles]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# Kubernetes vs OpenStack

## 概要

前言

最近2年相信大家都听过kubernetes这种新容器编排工具，越来越多的公司也去学习相关技术，并运用它去解决公司的问题，它在开源社区也是非常火，大小不断的k8smeeting以及容器相关的会议。这火爆程度和在2011年到2016年之间非常火的Openstack非常相似，不论是社区还是公司都是积极的去推动。笔者处在互联网之中，也接触学习过这两套系统，对他们相关技术也是非常的热爱，也在慢慢的根据不同应用场景在公司去推动相关业务转型，如相关服务的容器化技术转型等等，我就在这表达一下自己的一些看法与意见。加深理解大家对openstack 和kubernetes相关体系的理解与学习。
趋势

先简单说下目前的趋势，目前来看Openstack整个项目趋向于稳定，活跃程度相比之前有所下滑，从整个发版速度来看，由原来的半年一个relase转为一年一个relase, 团队的整个核心也将更多精力放在关于系统的可用性和稳定性优化，不过这并不是说他已经过时了，他是经过了上万台服务器的检验，是一个非常好的云操作系统，还是有拥有大量的用户和热爱者，如ebuy, 沃尔玛，京东，美团以及相关的私有云企业服务。

而kubernetes则是业界的新宠，可以用如日中天来形容，首先是Google自家对它的大力支持，包括前段时间Google Cloud捐赠给kubernetes社区800万美元的捐赠就能看出重视程度;其次是开源社区和各大公司对其的热爱程度，它在开源社区击败了docker官方推出的swarm容器编排工具和其他等类似编排工具，成为容器平台的编排标准，同时各个公有云也推出了基于kubernetes和自身IAAS服务结合的云容器引擎，例如AWS, Aurze,阿里云，腾讯云和网易云等等。所以说从目前来看，大家对kubernetes的偏爱会更多一些，特别是受开发者的热爱。

给笔者的感觉是Openstack是一个相对完善的云操作系统，很多公司可以很方便利用他进行自己公司的资源管理，资源分配，是一个已经长大30岁成熟的老大哥，而kubernetes是一个初出茅庐富有活力的新青年，特别是大家的热爱与追捧，看起来有点像Python和Golang的关系。
他们是什么

openstack www.openstack.org/

是一个云操作系统，通过数据中心可控制大型的计算、存储、网络等资源池。所有的管理通过前端界面管理员就可以完成，同样也可以通过web接口让最终用户部署资源。

简单理解: 可以把它类比公有云，它将各种基础资源虚拟化，并提供简化的方式去管理。偏向IAAS服务

kubenretes kubernetes.io/

是用于自动部署、扩展和管理容器化（containerized）应用程序的开源系统。

简单理解: 容器编排，管理多机的容器状态. 偏向PAAS服务
区别
使用场景:

openstack

这里写图片描述
应用场景其实更偏向于是IAAS层，它有能力很好地对我们计算，存储，网络资源的管理，并且以标准服务的方式提供出来，例如在计算方向, 有nova，glance, cinder等相关服务，能很好的编排管理我们的物理机，虚拟机，甚至是容器。 网络方向，有Netruon这样的杀手级项目实现虚拟网络，能更好的管理我们的网络资源。存储的话，有自家的cinder, swift等等项目，还有更有很多其他的项目，像VPN, 负载均衡，数据库等等服务，提供我们可能需要的其他基础服务。从这些可以看出它能更好的做数据中心，它刚出来的时候，是想对标AWS，后来也对Vmware私有云造成了很大冲击。更重要的是它是开源的，像国内很多公司都是基用Openstack做内部的私有云，像传统企业移动，电信，互联网企业，美团和京东等等，公有云的话像Ucloud, 华为也用了很多Openstack的组件实现自身的需求。

Kubernetes

这里写图片描述
更像是一个云容器时代的一个杀手级应用，更偏向于PAAS，他的目的是高效的管理服务容器，是一个高效的容器编排引擎，它不仅实现了基本的容器调度，还实现了微服务调度框架，具体像集中的配置管理中心, ConfigMap, 服务发现与负载均衡 Service & Ingress, 服务调度编排, Controller, 服务动态缩,Heapster, Autoscaling， 容错和高可用, Health Check &resource isolation, Deployment。所以可以看出，kubernetes是一个能更好构建微服务的工具，在平台层解决了微服务的问题(其他Spring Cloud相关比较本文不与介绍)，能快速的将公司的架构服务化。像我们公司内部就用它解决了很多问题，比如系统的弹性，服务化，提高资源利用等等。

openstack : 难度相对高

有大量的组件依赖，包括依赖mysql, rabbitmq, apache, nova, nova-api, nova-conduction, nova-scheduler, cinder-api, cinder-scheduler, netruon等几十个项目，具体大家可以去官网看。其实也可以理解，目标是对标aws的项目肯定会不简单。

kubernetes : 简单

组件简单, kube-proxy, kubelet, kube-api, kube-shecduler, etcd, controller等10来个项目，所以可以看到它所依赖的组件不会太多，会更好维护。最关键的是kubernetes的很多项目都可以直接运行在容器中，这就意味着你可以不需要去管理你的系统，让系统自动的去解决问题，这一点是非常非常赞的。
系统架构

openstack : 各个项目设计简单，容易扩展和维护，存在较少的性能问题，不过所有项目整和起来会相对难运维。

这里写图片描述
openstack项目几乎都是基于服务化设计，项目都实现了REST http协议的api和暴露api，各个项目都是用的各自的数据库， 服务之间解耦用了消息队列，性能服务会用到内存数据库memcache, 这些设计在很大程度上提升整个系统的可用性和稳定行，你可以直接将应用分布式系统中的一些解决思路放在openstack项目中，像负载均衡，服务发现，熔断等等。不过所有项目加起来一起维护就会相对较复杂，需要做好系统架构，然后配合一套相对自动化的运维体系，最后还做好自身的监控告警等。

kubernetes: 各个项目设计简单，中心化设计相对较少，性能问题主要集中在etcd。

这里写图片描述
kubernetes自身的服务就比较简化， 服务之间设计主要通过grpc, http协议进行通信，也是进行服务化设计，会用到etcd去注册发现， 中心化服务相对好扩展。唯一相对严峻问题是大量主机(>5000)或大量Pods(>10万)级别下的etcd横向扩展的性能问题。当然单单从kubernetes的设计去考虑，也有其他的方式去解决问题。
网络

openstack : 实现了基于软件的虚拟化SDN网络

这里写图片描述
openstack虚拟网络(Neturon)是它非常核心的一个模块，完全用软件的方式实现了网络控制器，利用linux birdge, openvswitch等技术实现网络隔离与网络虚拟化，同时有高度的自定义功能，可以有多种vlan, vxlan, gre协议去可配置的实现overlayer网络，让用户自定义的去操作虚拟路由器，交换机等等, 在架构上它会有专门的网络节点做三层网络节点。

kubernetes : 利用开源组件实现overlay网络

这里写图片描述
kubernetes 利用开源组件实现了overlay, 网络不是它的专注核心，它重点关注的点是服务编排与调度，这有很多开源的网络插件像flannel, calico, weave等等很多，每个组件都有自己的优势，有通过vxlan, 有直接是基于二层路由协议的， 应用场景和性能也会有所不同。相对来说kubernetes没有指定某种实现，而主要去实现一种网络接口，让各大厂商或云可以利用各自的优势去实现不同的overlayer，所以他也不会有专门的网络节点。
存储

openstack : 提供对象存储，块存储

openstack 根据自己的需求实现了块存储和对象存储，自身的对象存储会用在像glance这样的镜像服务，块存储会用在vm之间的共享和自定义挂载，它的存储都是独立的项目，独立的去解决各自的问题，而且从最开始的设计思路就像标准化的存储去实现，可扩展强，支持分布式，对接相对容易，当然openstack 也能对接其他的存储，比如像ceph。

kubernetes : 不实现存储, 而是实现存储驱动和接口。

kuberntes 只是一个使用者的角度, kuberntes不是去实现一种针对容器较好的存储，而是去对接各个存储引擎。像比较主流的Nfs, Glusterfs, ceph, 以及像各个公有云的云存储组件。
资源隔离

openstack 隔离性相对较高

完善的多资源的多租户隔离，对vm是针对内核层面的隔离，网络是也有一些流量控制工具Linux Traffic Control, 存储也有各自的配额管理。

kubernetes 隔离性相对较低

隔离程度相对较低，不支持多租户，对资源池的管理基于resource, 和 namespace，隔离性相对较弱，对具体pods容器的管理基于cgroup,和namespace，不是基于内核层面。所有容器公用内核，隔离性相对较差。

看了这么多openstack与kubernetes的相关比较，看起来他们有很多不同，不管是从应用场景，还是系统架构都是不同的。不过他们并不是完全不相干的，他们也有很多共性，也有很多相互结合地方，他们都是为了更好的对资源进行管理。
结合

1 openstack 天生提供了多租户，这对于kubernetes来说是非常重要的，我们完全可以在openstack的环境中搭建Kubernetes服务，提供对多租户的服务支持，由openstack提供基础设施，包括基础服务vm, 负载均衡， 路由器，流量控制，租户管理等高级功能，由kubernetes实现容器编排。不过这种情况下，最好openstack 的网络模式用vlan隔离，否则相当于overlay上做overlay，网络性能会下降很多, 也可以让kubernetes网络模式走netruon，减少性能消耗。

2 openstack 服务用kubernets服务管理。 大家都知道openstack的服务默认是非容器化的，要运维好openstack就需要管理好他们的基础服务，包括mysql, mq, apache，网络组件等相关服务，这需要一套高效的自动化运维系统，而如果用kubernetes去管理opensetack基础服务，像mq, apache, 网络组件，那么运维就可以不去关心了，一切都交给kubernetes就好了。
展望

国内有公司像腾讯，网易都给客户提供私有云解决方案，目前来看有直接用openstack，也有直接用kubernetes，还有的是相互结合。同时也有公有云的容器引擎是用openstack + kubernetes 实现，像网易的蜂巢。所以说他们的关系是一个相互促进，相辅相成的，大家会越来越喜欢这两个项目，他们都在努力的为开源社区作贡献，都在各自的方向走向极致。
最后

感谢这两个项目，让我们学到超级多的架构知识，也感谢身处在的这个移动互联网时代，有这么棒的开源项目和开源社区。

原文:https://juejin.im/post/5b953d21f265da0afa3dc61b

## 参考

- [openstack vs kubernetes](https://blog.csdn.net/luanpeng825485697/article/details/86706131)
