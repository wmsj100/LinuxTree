---
title: kvm
date: 2020-04-01 19:55:36
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# kvm

## 概要

- KVM针对运行在x86硬件上的、驻留在内核中的虚拟化基础结构。
- KVM是第一个成为原生Linux内核(2.6.20)的一部分的hypervisor，它是由Avi Kivity开发和维护的，现在归Red Hat所有。
- 这个hypervisor提供x86虚拟化，同时拥有到PowerPC和IA64的通道。
- KVM最近还添加了对对称多处理主机的支持，并且支持企业级特性，比如活动迁移(允许来宾操作系统在物理服务器之间迁移)
- KVM是作为内核模块实现的，因为Linux只要加载该模块就会成为一个hypervisor。
- KVM为支持hypervisor指令的硬件平台提供完整的虚拟化
- KVM还支持准虚拟化来宾操作系统，包括Linux和Windows。
- 这种技术由俩个组件实现。第一个是可加载的KVM模块，当在Linux内核安装该模块后，它就可以管理虚拟化硬件，并通过/proc文件系统公开其功能。
- 第二个组件用于PC平台模拟，它是由修改版QEMU提供的。QEMU作为用户空间进程执行，并且在来宾操作系统请求方面与内核协调。
- 当新的操作系统在KVM上启动时(通过一个称为KVM的实用程序),它就成为宿主操作系统的一个进程，因此就可以像其他进程一样调度它。
- 但与传统的linux进程不一样，来宾操作系统被hypervisor标识为处于"来宾"模式(独立于内核和用户模式)
- 每个来宾操作系统都是通过/dev/kvm设备映射的，它们拥有自己的虚拟地址空间，该空间映射到主机内核的物理地址空间。
- KVM使用底层硬件的虚拟化支持来提供完整的虚拟化
- IO请求通过主机内核映射到主机上(hypervisor)执行的QEMU进程。
- KVM在Linux环境中以主机的方式运行，不过只要底层硬件虚拟化支持，它就能够支持大量的来宾操作系统。

## 参考

- [kvm](https://blog.csdn.net/baidu_23959681/article/details/82732488)
