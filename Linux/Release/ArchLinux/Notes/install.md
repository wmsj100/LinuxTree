---
title: install
date: 2020-03-20 16:31:32
modify: 
tags: [Notes]
categories: ArchLinux
author: wmsj100
email: wmsj100@hotmail.com
---

# install

## 概要

- 安装无界面系统

## 步骤

### 连接wifi

- `wifi-menu -o` 选择要连接的wifi,保存配置文件
- `netctl start wlan-wmsj100` 通过netctl网络管理工具启动无线连接
	- 如果启动过程报错,查看网卡是否已经启动`ip link set wlan0 down`
- `ip route` 查看路由是否正确

### 更新系统时间

- `timedatectl set-ntp true`
- `timedatectl status`
- 这个设置时间没什么效果,后面选择时区时候还可以重新选择

### 建立硬盘分区

- `fdisk /dev/sda` 选择要安装系统的磁盘,一定要看准了
- 进行磁盘分区规划
	- `/` 30G
	- `/var` 30G
	- `swap` 4G
	- `/home` 100G 把剩下的全部
- `mkfs.ext4 /dev/sdb1`
- `mkswap /dev/sdb2`

### 挂载分区

- `mount /dev/sdb1 /mnt`
- `mkdir -p /mnt/var /mnt/home` 先挂载根目录然后再创建目录进行挂载
- `mount /dev/sdb2 /mnt/var`
- `mount /dev/sdb5 /mnt/home`

### 修改镜像源顺序

- `vi /etc/pacman.d/mirrorlist` 调整China到顶部优先顺序

### 安装基础软件

- `pacstrap /mnt base linux linux-firmware` 安装系统,这个过程必须联网,因为会下载很多东西,包括内核什么的,大概会下载700M左右的数据

### 生成挂载文件

- `genfstab -U /mnt >> /mnt/etc/fstab` 记住是追加模式,不是覆盖模式

### 安装系统

- `arch-chroot /mnt` 切换到系统
- `ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime` 设置时区
- `hwclock --systohc` 生成`/etc/adjtime`

### 本地化

- `vim /etc/locale.gen` 取消注释`en_US.UTF-8 UTF-8`
- `locale-gen` 生成locale讯息
- `vi /etc/locale.conf` 添加`LANG=en_US.UTF-8`

### 设置网络

- `vi /etc/hostname` `ArchOS`
- `vi /etc/hosts` 
	- `127.0.0.1 localhost`
	- `::1 localhost`
	- `127.0.1.1 ArchOS.localdomain ArchOS`
- `pacman -S netctl` 选择`openresolv`来安装网络工具

### 设置root密码

- `passwd`

### 安装引导程序

- `pacman -S grub` 安装grub软件
- `grub-install --target=i386-pc /dev/sdb` 安装grub引导程序,后面的硬盘必须是系统盘的主盘
- `grub-mkconfig -o /boot/grub/grub.cfg` 生成主配置文件

### 安装软件

- `pacman -S netctl`
- `pacman -S dialog`
- `pacman -S wpa_supplicant` 这样启动机器后就可以通过`wifi-menu -o`来生成配置文件
- `pacman -S dhcpcd` 必须安装这个软件,否则网卡无法启动
	- `systemctl status netctl@wlan0-wmsj100` 来查看运行日志获取到的信息.

### 重启

- `exit` 退出系统
- `umount -R /mnt` 递归下载/mnt绑定的分区

### 配置网络

- `wifi-menu -o` 选择wifi并且连接,顺利会直接连接网络,如果无法连接,也会生成一个配置文件`/etc/netctl/wlano-wmsj100`
- `netctl start wlan0-wmsj100` 如果上面无法启动,执行这个命令来启动网络,如果有报错,可以先把wlan0停掉`ip link set wlan0 down`
- `systemctl status netctl@wlan0-wmsj100` 通过这个命令来查看日志,可能会有某个服务未启动未找到,比如`wpa_susplicant/dhcpds`等,确保这俩个软件安装
- 确保要连接的wifi是可以连接的,基本上排查了上面因素,网络就可以连接了.

## 参考

- [archlinux wiki install](https://wiki.archlinux.org/index.php/Installation_guide_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))
- [archlinux grub](https://wiki.archlinux.org/index.php/GRUB_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)#%E7%94%9F%E6%88%90%E4%B8%BB%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6)
