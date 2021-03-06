---
title: 你真的需要Kubernetes吗
date: 2020-03-08 13:40:54
modify: 
tags: [Articles]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# 你真的需要Kubernetes吗

## 概要

【译者的话】Kubernetes已不仅仅是一个容器编排系统，渐渐地形成了一个庞大的生态系统，特别是随着云服务的崛起。个人认为，Kubernetes或者微服务不适合于小团队，本文也是从小团队的角度出发，解释小团队为什么不适合使用Kubernetes。或许对于小团队来说，单体应用是更合适的选择。

如果你正在使用Docker，很自然地，下一步就是使用Kubernetes，即Kubernetes来编排容器：你的生产环境应该就是这样的吧?

嗯，也许吧。为同一应用程序做设计方案，往往团队规模的大小会导致设计方案的不同，比如具有500名软件工程师的团队与具有50名软件工程师或者只有5名软件工程师的团队相比，三者的设计方案不尽相同。

Kubernetes可能并不适合小团队：它只会给你带来更多的痛苦，却没有什么好处。

让我们来看看这是为什么。
每个人都喜欢模块化组件
Kubernetes有大量的模块化组件、概念、子系统、流程、多节点、代码，这些都意味着大量的问题。
多节点
Kubernetes是一个分布式系统：由一个主节点控制着其他工作节点。具体的工作负载被分配到不同的工作节点上，再由工作节点上的容器运行工作负载。

所以你已经开始思考使用两台物理机或者虚拟机来搭建Kubernetes集群。但是你现在只有一台机器，你可能需要更多的机器，这也是一个问题。
代码量大
截至2020年3月初，Kubernetes的代码库中有超过58万行Go语言代码。这是实际的代码，并不包括注释或空白行，也不包括扩展包。对于Kubernetes的代码库，2019年的一份安全审查报告（文末附报告下载方式）中说到：

    “……Kubernetes的代码库还有很大的改进空间。代码库庞大且复杂，代码的大部分只包含很少的文档说明，但有大量的依赖关系，包括Kubernetes对外部系统的依赖。在代码库中有很多逻辑应该被重写，从而降低复杂性，简少补丁，并减少文档的负担。”

公平地说，这与许多大型项目并没有什么不同，在大型项目中，你需要维护所有这些复杂的业务逻辑以防程序出现错误。
体系结构复杂性、操作复杂性、配置复杂性和概念复杂性
Kubernetes是一个复杂的系统，包含许多不同的服务、子系统和各种组件。

在开始之前，你需要了解这张高度简化的Kubernetes体系结构图（出处：Kubernetes文档）：
components-of-kubernetes.png

你需要了解很多Kubernetes的概念，以下是节选自Kubernetes文档中的一部分：

    在Kubernetes中，EndpointSlice包含一组网络端点的引用。EndpointSlice控制器自动为Kubernetes的Service创建EndpointSlice。这些 EndpointSlice根据Service selector将Service和Pod关联起来。
    默认情况下，EndpointSlice由EndpointSlice控制器管理，每个 EndpointSlice拥有不超过100个的网络端点。EndpointSlice按照1：1的比例将Endpoints和Services关联起来，而且他们应该具有相同的性能。

我好像看懂了上面的概念，但是请注意，你还有许多概念需要了解，比如EndpointSlice、Service、selector、Pod、Endpoint。

很多时候你根本不需要了解这些概念，因为你不需要这些概念所提供的功能，因此很多时候你根本不需要Kubernetes。

我们再随机从Kubernetes文档中挑选一段话看一下：

    默认情况下，发送到ClusterIP或NodePort的流量可能被路由到该服务的任何后端地址。从Kubernetes 1.7开始，使用NodePort的方式，Pod就可以接收外部流量了，但ClusterIP并不支持接收外部流量。但是更复杂的拓扑结构，比如按照分区来路由，目前还不支持。但是可以通过服务拓扑特性来解决这个问题，它允许服务创建者根据源节点和目标节点的节点标签定义路由流量的策略。

以下是刚刚那份安全审查报告中的内容：

    Kubernetes是一个庞大的系统，操作非常复杂。评估团队发现Kubernetes的配置和部署非常复杂，某些组件具有令人困惑的默认设置、缺少操作控制和隐式定义的安全控制。

开发复杂性
Kubernetes的使用可能会影响到正常的业务开发：你需要了解所有的Kubernetes概念（Pod、Deployment、Service等等）来运行你的业务代码。所以，你需要一个完整的Kubernetes系统。

由于Kubernetes的应用程序很难在本地运行，开发也就更加困难，因此出现了各种各样的解决方案，将本地环境的进程映射到Kubernetes集群中，再将Kubernetes集群中的进程映射回本地环境……（我在几年前为此编写了一个工具），还有许多不完善的解决方案可供选择。但最简单和最好的解决方案是不使用Kubernetes。
微服务（不是个好主意）
第二个问题是，你可以创建许多服务构成一个微服务系统，但你真的需要这么多服务吗？如何合理的拆分服务？

分布式应用程序确实很难正确的编写。服务越多，出错的可能就越大。

分布式应用程序很难调试。你需要全新的方式去记录日志，这或许跟在单体应用中的方式不太一样。

微服务是一种可组织的扩展技术：当有500名开发人员为同一个线上网站工作时，如果微服务可以使各个开发团队独立工作，那么支付大规模分布式系统所带来的附加成本是有意义的。所以你的组织架构可能是这样的，每5人成为一个微服务团队，负责一部分业务功能，其余的功能由不同的团队负责。

如果你的团队一共只有5人，但有20个微服务，并且你对分布式系统没有的迫切需求，那么你就不应该使用微服务。你们不会像大公司那样，每个服务配备5人，而是每个服务0.25人。
真的没用吗？
扩展
如果你需要对应用程序进行扩展，Kubernetes可能会很有用。但让我们先考虑一些替代方案：

    如果使用云服务，你可以得到最多416 vCPUs和8TiB RAM的虚拟机，这种垂直扩展的方式，我只想用脏话来表达。是的，它会很贵，但是也很简单。
    你可以使用像Heroku这样的服务来扩展许多简单的Web应用程序。


以上的前提条件是增加服务器确实对你有好处，但大多数情况下：

    大多数应用程序不需要扩展，一些合理的优化就足够了。
    许多Web应用程序的瓶颈通常是数据库，而不是Web服务器。


可靠性
更多的模块化组件意味着更多的出错机会。

使用Kubernetes可以很简单的实现可靠性（健康检查、滚动部署），甚至在很多情况下已经内置了这些特性。例如，Nginx可以对工作进程执行健康检查，还可以使用docker-autoheal或类似的机制自动重启出错的进程。

如果你更关心的是宕机时间，那么你的第一个想法不应该是“如何将部署时间从1秒减少到1ms”，而应该是“如何确保数据库表结构的更改不会阻止部署的回滚”。

如果你想要一个可靠的网络部署方案，没有单点故障的问题，有很多方法可以做到这一点，不需要引入Kubernetes。
最佳实践?
没有所谓的通用最佳实践。只有针对特定情况的最佳实践。仅仅因为Kubernetes很流行，并不意味着它就是你的正确选择。

在某些情况下，Kubernetes是一个非常好的主意。在另一些情况下，Kubernetes可能毫无益处。

除非你已经准备好应对这些巨大的复杂性，否则有各种各样的工具也可以做得很好：例如Docker Compose，还有像Heroku这样类似的系统，Snakemake也是很好的任务流程工具。

## 参考

- [原文](http://dockone.io/article/9846)
