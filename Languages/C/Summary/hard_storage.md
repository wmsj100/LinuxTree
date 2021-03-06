---
title: 关于硬盘存储的理解
date: 2019-12-04 10:05:11 Wednesday
modify:
tag: [article]
categories: C
author: wmsj100
mail: wmsj100@hotmail.com
---

# 关于硬盘存储的理解

- 之前对于硬盘存储的理解没有概念,好像就应该是500G的容量,就像一个空的盒子,可以放入500G容量的内容,
- 但实际上很少有东西的尺寸可以把500G容量完全使用完,东西彼此之间肯定会有间隙,这些间隙就属于空间浪费,
- 磁盘整理就是派遣一个小管家重新规划东西之间的摆放顺序,把空间利用率提到最高,这也只是针对当前已经存在的东西.
- 所以对于一个空的磁盘进行磁盘整理是完全没有意义的.
- 磁盘的里面全部都是密密麻麻的晶体管,是集成电路,是通过某种手段使电子可以接受管束,可能老的磁盘还在使用晶体管,但现在的存储都使用集成电路了,电子的位置是属于物理状态,通过高位或低位来实现数据的记录(0/1),然后所有的数据存储其实就是物理世界的电子状态的保存,已经使用的容量,就是那些位置的电子已经进行了位置变动,开始存储信息了.
- 虽然我此刻操作的是逻辑的虚拟的软件和文字,但这个操作时时刻刻影响有着真实的物理世界的集成电路的电子来响应我的操作.
- 所有的操作是要依赖能源消耗的,因为电子运动需要能量提供动力.
- 之前的传统机械硬盘是通过光刻机来操作盘片上光子的位置来实现信息记录的,但现在已经到了固态硬盘了,就是完全使用集成电路的电子来实现信息的记录,固态硬盘的抗干扰的能力应该没有机械硬盘的厉害吧,但几乎没有噪音,体积小,能量消耗应该更低.
- 固态硬盘的传输速度也要比机械硬盘的快速,因为固态硬盘的原理应该是使用制造内存条的技术来制造固态硬盘了,成本要更高,传输速度要更快,基本开机速度就是秒级别.
- 硬盘记录了信息是需要软件来识别,编码格式来转换.
