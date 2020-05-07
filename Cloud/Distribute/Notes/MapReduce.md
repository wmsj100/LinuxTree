---
title: MapReduce
date: 2020-05-07 09:48:48
modify: 
tags: [Notes]
categories: Distribute
author: wmsj100
email: wmsj100@hotmail.com
---

# MapReduce

## 概要

- Map本意可以理解为地图，映射，从现实世界获得或产生映射。
- Reduce本意是减少，归并前面Map产生的映射。

## MapReduce的编程模型

- 按照Google的MapReduce的论文所说，编程模型的原理是：
- 利用一个输入key/value对集合来产生一个输出的key/value对集合。
- MapReduce库的用户用俩个函数表达这个计算: Map和Reduce。
- 用户自定义的Map函数接受一个输入的key/value对值，然后产生一个中间key/value对值的集合。
- MapReduce库把所有具有相同中间key值的中间value值集合在一起后传递给Reduce函数。
- 用户自定义的Reduce函数接受一个中间key的值和相关的一个value值的集合。
- Reduce函数合并这些value值，形成一个较小的value值的集合。

## MapReduce实现

- 通过将Map调用的输入数据自动分割给M个数据片段的集合，Map调用被分布到多台机器上执行。
- 输入的数据片段能够在不同的机器上并行处理。
- 使用分区函数将Map调用产生的中间key值分成R个不同的分区
- Reduce调用也被分布到多台机器上执行

- MapReduce实现的大概过程如下：
	- 用户程序首先调用MapReduce库将输入文件分成M个数据片段，每个数据片段的大小一般从16MB到64MB。然后用户程序在集群中创建大量的程序副本。
	- 这些程序副本中有一个特殊的程序master。副本中其他的程序都是worker程序，由master分配任务。
		- 有M个Map任务和R个Reduce任务将被分配
		- master将一个Map任务或Reduce任务分配给一个空闲的worker。
	- 被分配了map任务的workder程序读取相关的输入数据片段，从输入的数据片段中解析出key/value对，然后把key/value对传递给用户自定义的Map函数，有Map函数生成并输出的中间key/value对，并缓存在内存中。
	- 缓存中的key/value对通过分区函数分成R个区域，之后周期性的写入到本地磁盘上，会产生R个临时文件。
		- 缓存的key/value对在本地磁盘的存储位置将回传给master，由master将这些存储位置再传送给Reduce worker.
	- 当Reduce workder程序接收到master程序发来的数据存储位置信息后，使用RPC从Map worker所在主机的磁盘上读取这些缓存数据。
		- 当Reduce worker读取了所有的中间数据(这个时候所有的Map任务都执行完了)后，通过对key进行排序后使得具有相同key值的数据聚合在一起。
		- 由于许多不同的key值会映射到相同的Reduce任务上，因此必须进行排序，
		- 如果中间数据太大无法在内存中完成排序，那么就要在外部进行排序。
	- Reduce worker程序遍历排序后的中间数据，对于每一个唯一的中间key值，Reduce workder程序将这个key值和它相关的中间value值的集合(这个集合是有Reduce worker产生的，它存放的是同一个key对应的value值)传递给用户自定义的Reduce函数。
		- Reduce函数的输出被追加到所属分区的输出文件。

## 参考

- [mapreduce介绍](https://blog.csdn.net/suifeng3051/article/details/41651851)
