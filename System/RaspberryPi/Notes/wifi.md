---
title: 树莓派配置WiFi
date: 2019-04-19 22:52:48	
modify: 
tag: [basic]
categories: Raspberry 
author: wmsj100
mail: wmsj100@hotmail.com
---

# 树莓派配置wifi

## 概述
- 将刷好系统的SD卡插入到windoS系统
- 在boot分区添加文件`wpa_supplicant.conf`
- 文件内容如下
```
country=CN
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
ssid="WiFi-A"
psk="12345678"
key_mgmt=WPA-PSK
priority=1
}

network={
ssid="WiFi-B"
psk="12345678"
key_mgmt=WPA-PSK
priority=2
scan_ssid=1
}
```
- ssid: wifi名称
- psk: WiFi密码
## 参考
- [树莓派设置wifi](http://shumeipai.nxez.com/2017/09/13/raspberry-pi-network-configuration-before-boot.html)
