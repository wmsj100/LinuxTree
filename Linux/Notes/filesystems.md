---
title: filesystems
date: 2020-03-13 18:20:53
modify: 2020-04-02 17:19:55 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# filesystems

## 概要

- 操作系统对系统的软件资源(不论是应用软件和系统软件)的管理都是以文件方式进行，承担这部分功能的操作系统称为文件系统。
- 文件系统是操作系统用于明确存储设备(磁盘)或分区上的文件的方法和数据结构；即在存储设备上组织文件的方法。
- 操作系统中负责管理和存储文件信息的软件机构称为文件管理系统，简称文件系统。
- 文件系统由三部分组成:文件系统的接口，对对象操作和管理的软件集合，对象及属性。
- 从系统角度来看，文件系统是对文件存储设备的空间进行组织和分配，负责文件存储并对存入的文件进行保护和检索的系统。
- 具体说它负责为用户建立文件，存入，读出，修改，转储文件，控制文件的存取，当用户不使用时撤销文件。
- 文件系统是命名文件及放置文件的逻辑存储和恢复的系统。
- 其实说起来就是文件系统为来提高磁盘的使用效率，帮助用户来管理文件存储，提高存储效率，并且能提供保护和恢复，所以会在磁盘某一个分区划分不同的文集系统，不同文件系统由各自擅长领域.

## 使用

- `cat /proc/filesystems`
- 如何查看当前系统分区的文件系统类型
- `df -T` 会输出当前所有分区的详情
- `sudo parted -l` 列出当前分区系统详情, 只列出手动分区的信息
- `sudo blkid` 打印当前已格式化分区的UUID和文件系统
- `lsblk -f` 查看文件系统

## 范例

- `lsblk -f`
```
ubuntu@Ubuntu:~/Documents/Github/LinuxTree/Linux/Notes$ lsblk -f
NAME        FSTYPE   LABEL UUID                                 MOUNTPOINT
loop0       squashfs                                            /snap/gnome-calculator/544
loop1       squashfs                                            /snap/gnome-system-monitor/127
loop2       squashfs                                            /snap/gnome-characters/399
loop3       squashfs                                            /snap/gtk-common-themes/1440
loop4       squashfs                                            /snap/gnome-3-28-1804/116
loop5       squashfs                                            /snap/gnome-logs/81
loop6       squashfs                                            /snap/core18/1668
loop7       squashfs                                            /snap/core/8268
nvme0n1
├─nvme0n1p1 vfat           6569-B76F                            /boot/efi
├─nvme0n1p2 xfs            553e1888-2116-4d25-b7b5-4c0124bdea3a /
├─nvme0n1p3 xfs            7b147c5c-9b0b-424c-89fe-5a1032ebbb15 /var
├─nvme0n1p4 ext4           174cb133-62dc-4629-a556-e38a8a00934d /boot
└─nvme0n1p5 xfs            c2dea934-b8dc-42f0-8b00-eaf90178c5d4 /home
```

- `sudo blkid`
```
/dev/nvme0n1: PTUUID="c7edb3d2-0267-4603-9492-2ffe5c3851d8" PTTYPE="gpt"
/dev/nvme0n1p1: UUID="6569-B76F" TYPE="vfat" PARTUUID="ee5e4981-2602-47d6-b2d0-4c912d99902b"
/dev/nvme0n1p2: UUID="553e1888-2116-4d25-b7b5-4c0124bdea3a" TYPE="xfs" PARTUUID="75a81033-5958-47ae-93ae-fd37f52fedf4"
/dev/nvme0n1p3: UUID="7b147c5c-9b0b-424c-89fe-5a1032ebbb15" TYPE="xfs" PARTUUID="459a3698-64a7-4131-849a-09a9b8516f2d"
/dev/nvme0n1p4: UUID="174cb133-62dc-4629-a556-e38a8a00934d" TYPE="ext4" PARTUUID="36bf05a9-862f-490a-82a6-361b2e927dc9"
/dev/nvme0n1p5: UUID="c2dea934-b8dc-42f0-8b00-eaf90178c5d4" TYPE="xfs" PARTUUID="541f28d6-30cf-4f4e-8a8d-12b512cdee4d"
```

- `sudo parted -l`
```
Number  Start   End     Size    File system  Name  Flags
 1      1049kB  99.6MB  98.6MB  fat32              boot, esp
 2      99.6MB  20.6GB  20.5GB  xfs
 3      20.6GB  40.8GB  20.2GB  xfs
 4      40.8GB  41.8GB  1024MB  ext4
 5      41.8GB  128GB   86.3GB  xfs
```

- `df -T`
```
ubuntu@Ubuntu:~/Documents/Github/LinuxTree/Linux/Notes$ df -T
Filesystem     Type     1K-blocks    Used Available Use% Mounted on
udev           devtmpfs   1901848       0   1901848   0% /dev
tmpfs          tmpfs       385204    1768    383436   1% /run
/dev/nvme0n1p2 xfs       19989504 7093092  12896412  36% /
tmpfs          tmpfs      1926008   97688   1828320   6% /dev/shm
tmpfs          tmpfs         5120       4      5116   1% /run/lock
tmpfs          tmpfs      1926008       0   1926008   0% /sys/fs/cgroup
/dev/nvme0n1p5 xfs       84189016 6575484  77613532   8% /home
/dev/nvme0n1p4 ext4        968312  118388    783520  14% /boot
/dev/nvme0n1p1 vfat         94759    6201     88558   7% /boot/efi
/dev/nvme0n1p3 xfs       19696640 2980408  16716232  16% /var
/dev/loop1     squashfs      3840    3840         0 100% /snap/gnome-system-monitor/127
/dev/loop2     squashfs     15104   15104         0 100% /snap/gnome-characters/399
/dev/loop3     squashfs     46080   46080         0 100% /snap/gtk-common-themes/1440
/dev/loop0     squashfs      4352    4352         0 100% /snap/gnome-calculator/544
/dev/loop4     squashfs    164096  164096         0 100% /snap/gnome-3-28-1804/116
/dev/loop6     squashfs     56064   56064         0 100% /snap/core18/1668
/dev/loop5     squashfs      1024    1024         0 100% /snap/gnome-logs/81
/dev/loop7     squashfs     91264   91264         0 100% /snap/core/8268
tmpfs          tmpfs       385200      36    385164   1% /run/user/1000
```

- `cat /proc/filesystems`
```
nodev	sysfs
nodev	tmpfs
nodev	bdev
nodev	proc
nodev	cgroup
nodev	cgroup2
nodev	cpuset
nodev	devtmpfs
nodev	configfs
nodev	debugfs
nodev	tracefs
nodev	securityfs
nodev	sockfs
nodev	bpf
nodev	pipefs
nodev	ramfs
nodev	hugetlbfs
nodev	devpts
	ext3
	ext2
	ext4
	squashfs
	vfat
nodev	ecryptfs
	fuseblk
nodev	fuse
nodev	fusectl
nodev	efivarfs
nodev	mqueue
nodev	pstore
	xfs
nodev	autofs
nodev	binfmt_misc
nodev	overlay
nodev	aufs
```

## 参考

- [linux 查看文件系统](https://www.cnblogs.com/kerrycode/p/9445608.html)
