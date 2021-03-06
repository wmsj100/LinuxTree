---
title: 虚拟机
date: 2020-04-01 17:54:03
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# 虚拟机

## 概要

- 虚拟化，是指通过虚拟化技术将一台计算机虚拟为多台逻辑计算机。
- 在一台计算机上同时运行多个逻辑计算机，每个逻辑计算机可运行不同的操作系统，并且应用程序都可以在相互独立的空间内运行而互不影响，从而显著提高计算机的工作效率。
- 虚拟化是表示计算机资源的逻辑组(或子集)的过程，这样就可以用从原始配置中获益的方式访问它们。这种资源的新虚拟视图并不受实现、地址位置或底层资源的物理配置的限制。
- 虚拟化技术可针对具体应用目的创建特定目的的虚拟环境，安全、效率高、快照、克隆、备份、迁移等方面。
- 系统虚拟化是将一台物理机虚拟成一台或多台虚拟计算机系统，每个都有子集的虚拟硬件，其上的操作系统认为自己运行在一台独立的主机上，计算机软件在一个虚拟的平台上而不是真实的硬件平台上运行。
- 虚拟化技术可以扩大硬件的容量，简化软件的重新配置过程。
- 其中cpu的虚拟化可以单cpu模拟多cpu并行运行，允许一个平台同时运行多个操作系统，并且应用程序可以在相互独立的空间内运行而互不影响。
- 虚拟化技术在降低硬件成本的同时，还可以显著提高系统的工作效率和安全性。
- 虚拟化系统的实现通常是在操作系统和硬件之间加入一个虚拟机监控程序，称为Hypervisor。
- 由Hypervisor主要负责各个操作系统之间的硬件资源协调。
- 虚拟机监控程序是一种特殊操作系统，直接在裸机上运行(针对完全虚拟化技术).
- 虚拟机监控程序创建一个底层硬件平台抽象，一个或多个虚拟机(vm)共享这个底层硬件平台。
- 在这种环境中，vm只是操作系统及其应用程序的容器，一个VM与虚拟机监控程序上运行的其他VM隔离，这支持多个操作系统或多个配置不同的相似操作系统。

## 虚拟机特征

- 虚拟计算机系统三层含义： 同质、高效、资源受控
	- 同质： 本质上虚拟机和物理机是相同的，表现上有所差异，如一个物理核虚拟多个核
	- 高效： 虚拟机效能接近物理机
	- 资源受控：虚拟机对系统资源有完全的控制能力，包括分配、管理、回收。

## 虚拟机的虚拟化类型

- 硬件抽象层的虚拟化： 客户机和宿主机硬件相似，指令集相似
- 操作系统层虚拟化： 内核可以提供多个互相 隔离的用户态，其拥有独立的文件系统、网络、系统设置和库函数。
- 库函数层虚拟化： 是不同的操作系统可以拥有共同的库函数接口，应用程序不需要修改。
- 编程语言层虚拟化： 编的程序运行在一个虚拟机上，与具体硬件无法，如java。

## 虚拟机的优点

- 良好的封装: 虚拟机的运行环境保持便捷，便于随时抓取状态、备份、克隆、挂起和恢复。
- 多实例: 最大限度减少物理资源，提到利用率，便于管理。
- 隔离: 每个应用程序可以在独立的操作系统中运行，互不干涉，奔溃页不会影响其他任务。
- 硬件无关性: 只要拥有相同的硬件抽象层，虚拟机就可以无缝迁移，因此维护和升级简单。
- 安全: 便于控制访问权利，病毒入侵检测等。

## 虚拟化分类

- 按照虚拟化程度分为完全虚拟化和类虚拟化。
- 完全虚拟化: 客户及操作系统不需要任何修改即可运行，分软件辅助完全虚拟化和硬件辅助完全虚拟化，完全虚拟化能够模拟所有CPU指令。
- 类虚拟化: 操作系统需要作出适应性修改，回避那些那些难以模拟的指令。
- 按照宿主机是否存在独立操作系统分为hypervisor模型和宿主模型，
	- 前者需支持所有的物理资源管理(系统启动、内存管理、设备驱动)，效率高，复杂；
	- 后者只需要调用宿主操作系统API实现虚拟化，宿主操作系统可以windows、linux，效率低，简单。
- 第三类是俩者的混合，VMM位于硬件层上，但让出部分IO设备管理权给一个运行在特权虚拟机上的特权操作系统，VMM负责处理器和内存虚拟化。

## 虚拟化技术框架

- 虚拟环境组成: 硬件、VMM、虚拟机，物理机中操作系统直接管理硬件(通过硬件抽象层HAL)，虚拟环境中VMM管理硬件(会构建一个或多个逻辑HAL),操作系统运行在VMM逻辑HAL之上，运行在非CPU最高特权。
- 对物理资源的三个主要任务: 处理器虚拟化、内存虚拟化和IO虚拟化。
- 若硬件直接支持虚拟化技术则CPU辅助完成虚拟化过程，在CPU、芯片组以及IO设备加入专门针对虚拟化的支持，从而高容易、高效的实现虚拟化。

## 为什么选择虚拟化

- 更高的资源利用率: 虚拟可支持实现物理资源和资源池的动态共享，提高资源利用率，特别是针对那些平均需求远低于需要为其提供专用资源的不同负载
- 减低管理成本: 虚拟可以通过以下途径来提高工作人员的效率:减少必须管理的物理资源数量；隐藏物理资源的部分复杂性；通过实现自动化，获得更好的信息和实现中央管理来简化公共管理任务，实现负载管理自动化。
- 提高系统灵活性: 通过虚拟可以实现动态的资源部署和重配置，满足不断变化的业务需求。
- 提高安全性: 虚拟可以实现较简单的共享机制无法实现的隔离和划分，这些特性可实现对数据和服务进行可控和安全的访问。
- 更高的可用性: 虚拟可在不影响用户的情况下对物理资源进行删除、升级和改变
- 更高的扩展性: 根据不同产品，资源分区和汇聚可支持实现比个体物理资源小的多或大得多的虚拟资源，这意味着在不改变物理资源配置的情况下可以进行规模调整。
- 互操性和投资保护: 虚拟资源可提供底层物理资源无法提供的与各种接口和协议的兼容性
- 改进资源供应: 与个体物理资源单位相比，虚拟能够以更小的单位进行资源分配

## 参考

- [虚拟化的好处](https://blog.csdn.net/yibuchen/article/details/80426680)
