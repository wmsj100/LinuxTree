---
title: RaspberryPi-Lite
date: 2020-03-11 09:45:24
modify: 
tags: [Notes]
categories: RaspberryPi
author: wmsj100
email: wmsj100@hotmail.com
---

# RaspberryPi-Lite

## 概要

- 之前一直都是安装的完整版本,第一次安装Lite版本
- 区别是Lite是一个纯净版本,没有视窗和其他多余软件,但是系统压缩比400M左右,解压出来有接近2G,这个压缩率是不是太高了.
```
-rw-r--r--  1 ubuntu ubuntu 1.8G Feb 14 00:10  2020-02-13-raspbian-buster-lite.img
-rw-rw-r--  1 ubuntu ubuntu 434M Mar 11 08:00  2020-02-13-raspbian-buster-lite.zip
```
- 看了下安装好的系统容量没有镜像大,因为我没有安装视图窗口,而且还有我在home目录存放的270M的数据文件
```
pi@raspPI:~ $ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/root        29G  1.8G   27G   7% /
devtmpfs        459M     0  459M   0% /dev
tmpfs           464M     0  464M   0% /dev/shm
tmpfs           464M  6.2M  457M   2% /run
tmpfs           5.0M  4.0K  5.0M   1% /run/lock
tmpfs           464M     0  464M   0% /sys/fs/cgroup
/dev/mmcblk0p1  253M   53M  200M  21% /boot
tmpfs            93M     0   93M   0% /run/user/1000

```

## 配置

- 没有试图界面,而且是通过wifi连接,有很多类似Arch的网络连接工具,wpa_suport工具,但是没有netctl/wifi-工具,是另一个networkctl
- 树莓派也是类似Arch的`Arch-setup`,
- `raspi-config`进入配置界面,可以首先要配置location,选择`en_US_UTF-8`,键盘也要选择,那个就选择US,其他默认
- 网络,想选择国家,wifi_name,wifi_pwd
- 配置控制台是否安装GUI,是否自动进入那个界面,控制台也是可以自动登陆的.
- 其他配置可以随便看看

## 总结

- 如果要用树莓派肯定要安装这个版本,因为GUI基本都不会使用,不可能用树莓派连接一个显示屏,太占用资源了.主要是根本不会用,干嘛要开机运行.
- 这个性能也要明显好,剩余资源很多,
- 但总归来说arm在服务器领域还是弱势,很多发行版或者软件包不会有arm的,尤其是docker的arm镜像更加少了,而且不同平台联合使用的时候通过docker控制总是会出现问题,虽说是平台无关的.
- 总归使用体验是非常好的
- 我安装这个的原因是自己想格式化u盘时候不小心进错了控制台,把树莓派给格式化了,所以没有办法了,只能重新安装了,装了alpine/arch,使用下来还是RaspberryPi稳定好用,毕竟是官方适配的镜像.

## 参考

