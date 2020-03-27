---
title: 内存分页
date: 2020-03-27 22:04:37
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# 内存分页

## 概要

- CPU是通过寻址来访问内存的,32位的CPU寻址宽度是4G,也就是说可支持的物理内存最大是4G.
- 但在实践中碰到了这样的问题,程序需要使用4G内存,而可用物理内存小于4G,导致程序不得不降低内存占用,为了解决此类问题,现代CPU引入了MMU(Memory Management Unit内存管理单元)
- MMU的核心思想是使用虚拟地址替换物理地址,即CPU寻址时使用虚址,由MMU负责将虚址映射为物理地址.
- MMU的引入,解决了对物理内存的限制,对程序来说,就像自己在使用4G内存一样.
- 内存分页(Paging)是在使用MMU的基础上,提出的一种内存管理机制,它将虚拟地址和物理地址按固定大小(4K)分割成页(page)和页帧(page frame),并保证页与页帧的大小相同.
- 这种机制从数据结构上保证了访问内存的高效,并使OS能支持非连续的内存分配.
- 在程序内存不够用时,还可以将不常用的物理内存转移到其他存储设备上,比如磁盘,这就是大家耳熟能详的虚拟内存.
- 虚拟地址和物理地址需要通过映射才能使CPU正常工作.
- 而映射就需要存储映射表.在现代的CPU架构中,映射关系通常被存储在物理内存上一个被成为页表(page table)的地方.
- 虚拟地址空间被划分为页的单位,而相应的物理地址也被进行划分,单位是页帧,一个在内存,一个在磁盘,页和页帧的大小必须相同.
- 页的大小是4K,而相应的页帧的大小与页相等,这点必须保证,因为内存和外围存储器之间的传输总是以页为单位的.对应4G的虚拟地址和256M的物理存储器,他们分别包含了1M个页和64K个页帧.
- 页表就像一个函数,输入页号,输出页帧,实现从页号到物理地址的映射,操作系统给每一个进程维护一个页表.所以不同进程的虚拟地址可能一样,页表给出了进程中每一页所对应的页帧的位置.
- 意思是说:一个页可以存储4K个虚拟内存的地址项,页存储在内存中;一个页帧也是存储4K个物理地址项,页帧存储在磁盘中,页表中保存的是页号和页帧的对应关系,页表存储在内存中.

## TLB

- TLB(Translation lookaside buffer 页表寄存器缓存)
- 页表是存储在内存中,CPU通过总线访问内存肯定要慢于直接访问寄存器
- 为了进一步优化性能,现代CPU架构引入TLB,用来缓存一部分经常访问的页表内容,TLB存储在寄存器中.

## 大页内存

- TLB是有限的,当超出TLB的存储极限时,就会发生TLB miss,之后,OS就会命令CPU区访问内存上的页表,如果频繁出现TLB miss,程序的性能会下降的很快.
- 为了让TLB可以存储更多的页地址映射关系,我们的做法是调大内存分页大小.
- 如果一个页4M对比一个4K,前者可以让TLB多存储1000个地址映射关系,性能的提升是比较直观的.
- 分页机制可以让逻辑上连续,物理上分散

## 参考

- [内存分页](https://blog.csdn.net/u010002184/article/details/77039135)