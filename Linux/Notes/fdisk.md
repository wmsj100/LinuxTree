---
title: fdisk
date: Mon 19 Feb 2018 09:29:02 AM CST
tag: [linux]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

 # 文件系统操作与磁盘管理

## 查看磁盘和目录的容量
- df 查看磁盘的容量
- du 查看目录的容量
	- h 以KB/MB/GB 的容量显示占用的大小
	- d 1 查看目录的深度，1表示只查看目录下的一层，2表示目录的深度是2
	- s 只列出总大小

## 创建虚拟磁盘
- dd 该命令用于转换和复制文件，可以读取自或写入到文件，可以用在备份系统的引导扇区/获取一定数量的随机数据/或者写入空数据的任务；dd也可以在复制时处理数据，例如字节转换或者编码转换。
	- dd of=test bs=10 count=1
		- if input file 读取的数据文件
		- of output file 输入数据文件
		- bs block size，默认单位为byte，可以指定单位K/M/G
		- count 写入的bs个数
	- dd if=/dev/stdin of=test bs=10 count=1 conv=ucase
		- conv 表示把输入全部转换为大写然后写入输出
	- dd if=/dev/zero of=virtual.img bs=1M count=256 用0数据创建一个大小为256M的文件

- mkfs.ext4 virtual.img 把创建的文件格式化为ext4文件系统

### moutn挂载磁盘到目录树
- 用户在linux上打开一个文件以前，包含该文件的文件系统必须先挂载。实验mount命令进行挂载，该命令通常使用在USB或其他可移除设备。根目录需要保持挂载状态。
- linux文件系统可以对应一个文件而不一定要时一个硬件设备，所以可以挂载一个包含文件系统的文件到目录树。
- mount指令时告诉操作系统，对应的文件系统已经准备好，可以使用了，而该文件系统会对应到一个指定的点（称为挂载点）。挂载好的文件/目录/设备即可以供用户使。
- loop 在类UNIX系统中，/dev/loop 是一种伪设备，这种设备使得文件如同块设备一样被访问。这种设备经常被用于光盘或者磁盘镜像。
- mount -o loog -t ext4 virtual.img /mnt 把virtual.img 挂载到/mnt
- umount /mnt 卸载已挂载的磁盘

## fdisk 为磁盘分区
- 刚刚创建了一个文件系统文件，并且已经通过mkfs命令格式化好了，也通过命令mount挂载过，现在通过命令“fdisk”命令来对文件系统进行分区。
- fdisk virtual.img
	- p 查看当前文件系统的分区情况，因为时新创建的系统，所以分区为空。
	- 当前的磁盘规划是打算创建一个30M 的主分区剩余部分为扩展分区包含2个分别大约45M的逻辑分区
	- n 创建新分区，
		- p创建主分区
		- enter直接按下
		- +30M 这个主分区设置为30M
	- n 
		- e 创建逻辑分区
		- 直接俩个enter把剩余的所有空间全部纳入扩展分区，逻辑分区在扩展分区内部继续划分
	- n
		- l
		- enter
		- +45M 这个扩展分区大小为45M
	- w 把所有的操作写入并且保存
- partprobe 通过这个命令会让刚刚操作的立即生效
