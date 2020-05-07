---
title: Yarn
date: 2020-05-07 14:59:12
modify: 
tags: [Notes]
categories: Hadoop
author: wmsj100
email: wmsj100@hotmail.com
---

# Yarn

## 概要

- Yarn是Hadoop2.0对MapReduce框架做了彻底的重构的产物。
- 它将资源管理和应用监控分开处理
- Yarn的另一个目标就是拓展Hadoop，使得它不仅仅可以支持MapReduce计算，比如还可以很方便的管理诸如Spark、Hive、Hbase等应用。
- Yarn的出现使得Hadoop成为大数据的最稳定的磐石，尤其是HDFS和Yarn更是成为来核心，而MapReduce出现来替代者Spark。
- 有了Yarn，各种应用就可以互不干扰的运行在同一个Hadoop系统中，共享整个集群资源。
- 为什么会有在Container中运行应用的说法，是因为面对大数据，移动数据代价太高，所以就移动应用，然后使用资源来计算。

## Yarn组件

- Container: Yarn对计算机计算资源的抽象，它其实就是一组CPU和内存资源，所有的应用都会运行在Container中。
- ApplicationMaster: 对运行在Yarn中某个应用的抽象，它其实就是某个类型应用的实例，ApplicationMaster是应用级别的，它的主要功能就是向ResourceManager申请计算资源并且和NodeManager交互来执行和监控具体的task
- Scheduler: ResourceManager专门进行资源管理的一个组件，负责分配NodeManager上的Container资源，NodeManager也会不断发送自己Container使用情况给ResourceManager。
- ResourceManager和NodeManager俩个进程主要负责系统管理方面的任务。
- 每种类型的应用都会有一个ApplicationMaster实例，ApplicationMaster通过与ResourceManager沟通获得Container资源来运行具体的job，并跟踪这个job的运行状态、监控运行进度。

## Container

- Container是Yarn框架的计算单元，是具体执行task(map task，reduce task)的基本单位。
- Container和集群节点的关系是: 一个节点会运行多个Container，但一个Container不会跨节点。
- 一个Container就是一组分配的系统资源，现阶段只包含俩种系统资源CPU、内存。
- Container中包含计算资源的位置信息: 计算资源位于哪个机架的哪台机器上。
- 任何一个job或者application必须运行在一个或多个Container中，在Yarn框架中，ResourceManager只负责告诉ApplicationMaster哪些Container可以用，ApplicationMaster还需要去找NodeManager请求分配具体的Container。

## NodeManager

- NodeManager进程运行在集群中的节点上，每个节点都会有自己的NodeManager。
- NodeManager是一个slaver服务: 它负责接收ResourceManager的资源分配请求，分配具体的Container给应用。
- 同时它还负责监控并报告Container使用信息给ResourceManager。
- 通过和ResourceManager配合，NodeManager负责整个Hadoop集群中的资源分配工作。
- ResourceManager是一个全局进程，而NodeManager是每个节点上的进程，管理这个节点上的资源分配和监控运行节点的健康状态。
- NodeManager的具体任务列表：
	- 接收ResourceManager的请求，分配Container给应用的某个任务
	- 和ResourceManager交换信息以确保整个集群平稳运行。ResourceManager就是通过收集每个NodeManager的报告信息来追踪整个集群健康状态的，而NodeManager负责监控自身的健康状态。
	- 管理每个Container的生命周期
	- 管理每个节点上的日志
	- 执行Yarn上面应用的一些额外的服务，比如MapReduce的shuffle过程
- 当一个节点启动时，它会向ResourceManager进行注册并告知ResourceManager自己有多少资源可用。
- 在运行期，通过NodeManager和ResourceManager协同工作，这些信息会不断被更新并保障整个集群发挥出最佳状态。
- NodeManager只负责管理自身的Container，它并不知道运行在它上面应用的信息。负责管理应用信息的组件是ApplicationManager

## ResourceManager

- 主要有俩个组件: Scheduler和ApplicationManager
- Scheduler: 一个资源调度器，它主要负责协调集群中各个应用的资源分配，保障整个集群的运行效率。
- Scheduler的角色是一个纯调度器，它只负责调度Containers，不会关心应用程序监控及其运行状态等信息。同样，它也不能重启因应用失败或硬件错误而运行失败的任务。
- Scheduler是一个可插拔的插件，它可以调度集群中的各种队列、应用等。
- ApplicationManager负责接收job的提交请求，为应用分配第一个Container来运行ApplicationMaster，还有就是负责监控ApplicationMaster，在遇到失败时重启ApplicationMaster运行的Container。

## ApplicationMaster

- ApplicationMaster的主要作用是向ResourceManager申请资源并和NodeManager协同工作来运行应用的各个任务然后跟踪它们状态及监控各个任务的执行，遇到失败的任务还负责重启它。
- 如果ApplicationMaster失败，ResourceManager还可以重启它，这大大提高来集群的拓展性。
- Yarn运行每个应用开发自己对应的ApplicationMaster，一个ApplicationMaster其实就是一个类库。
- 一个ApplicationMaster类库可以对应多个实例，每种应用都会对应这一个ApplicationMaster。每个类型的应用都可以启动多个ApplicationMaster实例。

## Yarn对比老的MapReduce优势

- 这个设计大大减少来ResourceManager的资源消耗，并且让检测每一个job子任务状态的程序分布式化来，更安全、更优美。
- 在新的Yarn中，ApplicationMaster是一个可变更的部分，用户可以对不同的编程模型写自己的AppMst，让更多类型的编程模型能够跑在Hadoop集群中，
- 对于资源的表示以内存为单位，比之前以剩余slot数目更合理。
- 老框架中JobTracker一个很大的负担就是监控job下的tasks的运行状况，现在，这部分扔给ApplicationMaster做来，而ResourceManager中有一个模块叫做ApplicationManager,它是检测ApplicationMaster的运行状况，如果出问题，会将其在其他机器上重启。
- Container是Yarn为来将来做资源隔离而提出的一个框架。

## 参考

