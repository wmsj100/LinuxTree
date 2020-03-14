---
title: scp
date: 2020-03-14 22:20:50
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# scp

## 概要

- 可以远程拷贝文件到不同主机
- 通过tcp/ip协议来传输文件,传输效率要远高于U盘传输
- wifi传输和网线传输的效率差距有5倍左右,

## 使用

- 场景是我的电脑和树莓派通过通过无线连接到路由器,通过网段`192.168.0.0/24`连同
- 我又用一根网线把树莓派和电脑连接起来,设置的网段是`192.168.20.0/24`,且指定`192.168.20.1`为网关
- 现在先拷贝文件时如何选择ip
- 刚开始想着是拷贝文件时如何指定本地ip来传输文件,即我想用本地的192.168.20.1来传输文件,然后查scp没有指定本地ip的用法.
- 后来转念一想,其实就不用指定本地ip,只需要指定远端ip即可,
- 如果指定树莓派ip为`192.168.0.102`时,本地传输ip默认就是`192.168.0.103`,因为只有这个ip它是连同的,即选择了无线传输
- 如果指定树莓派ip为`192.168.20.2`,本地就选择ip`192.168.20.1`来传输,即就选择了网线传输

## 命令

- 在主机传输镜像到树莓派,有线和wifi的网速差距4倍左右
```
ubuntu@Ubuntu:~/Downloads$ scp 2020-02-13-raspbian-buster-lite.zip $pi:/tmp
2020-02-13-raspbian-buster-lite.zip                                                                                                                    6%   27MB   2.4MB/s   02:46 ETA^Cubuntu@Ubuntu:~/Downloads$ man scp
ubuntu@Ubuntu:~/Downloads$ scp 2020-02-13-raspbian-buster-lite.zip pi@192.168.20.2:/tmp
The authenticity of host '192.168.20.2 (192.168.20.2)' can't be established.
ECDSA key fingerprint is SHA256:KkKUU6Rif28S34+lTJjZi4iqweNbhXmlVjwJrAsVxjw.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '192.168.20.2' (ECDSA) to the list of known hosts.
2020-02-13-raspbian-buster-lite.zip                                                                                                                  100%  433MB   9.1MB/s   00:47
```
- 树莓派传输文件到主机,网速差距也在4倍左右
```
pi@raspPI:/tmp $ scp 2020-02-13-raspbian-buster-lite.zip $ubuntu:/tmp
2020-02-13-raspbian-buster-lite.zip                                                                                                                   11%   51MB   3.1MB/s   02:02 ETA^Cpi@raspPI:/tmp $ scp 2020-02-13-raspbian-buster-lite.zip ubuntu@192.168.20.1:/tmp
2020-02-13-raspbian-buster-lite.zip                                                                                                                   85%  372MB  11.3MB/s   00:05 ETA^
```

## 总结

- 从上面看出,如果可能,还是使用网线传输文件速度更快,而且更加安全,

## 参考

