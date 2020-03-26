---
title: NAT
date: 2020-03-19 08:23:21
modify: 
tags: [Notes]
categories: NetWork
author: wmsj100
email: wmsj100@hotmail.com
---

# NAT

## 概要

- NAT: Network Address Translation 网络地址转换
- NAT对外展示的所有的服务都是一个Public IP,隐藏了内部主机的ip信息,可以起到一定的保护作用.

## NAT流程

- 先经过NAT table的PREROUTING链
- 经由路由判断这个数据包是否要进入本机,若不进入本机,则下一步
- 再经由Filter table的FORWARD链
- 通过NAT table的POSTROUTINT链,最后传送出去.
---
- Nat的俩条重要的链
	- PREROUTING: 修改目标IP DNAT
	- POSTROUTING: 修改来源IP SNAT
- SNAT: 修改数据包报头的来源项目,通常用于内网主机访问服务器
	- 客户端发出数据包报头中,来源是'192.168.1.100',访问目标'tw.yahoo.com',然后把请求发送到NAT主机
	- NAT受到这个请求后,会主动分析数据包报头,因为报头不是本机,所以经过路由分析,将此数据包转到可以连接到Intenet的public IP处
	- 由于private IP和public IP不能互通,所以Linux主机通过iptables的NAT table内的POSTROUTING修改来源ip为Linux的public IP,并且将俩个不同来源(192.168.100.1及public IP)的数据包对应写入暂存内存当中,然后将此数据包发送出去
	- Internet IP接受并将响应数据发送给public IP
	- 当Linux publicIP主机接受到数据包时候,会分析数据包的序号,并比对刚刚记录到内存当中的数据,由于发现该数据为内网主机之前发送出去的,因此在NAT PREROUTING链中,会将目标IP修改为内网IP(192.168.100.1)
- DNAT: 修改数据包报头的目标项目,通常用于提供服务的主机位于内网,向外提供类似www服务
	- 外部主机想要访问目的端的www服务,
	- 请求到达NAT主机,分析出目的端的port 80数据包,修改目的IP由public iP 修改为private,且将该数据包相关信息记录下来,等待内部主机响应.
	- private主机响应数据发送到NAT主机,
	- NAT主机分析内存中有这样的对应关系,修改目标IP为外网IP,然后就把数据传送出去.

## 常用命令

- `sudo iptables -t nat -A POSTROUTING -s 192.168.20.0/24 -o wlan0 -j MASQUERATDE` 这样就会把来自内网eth0的流量请求通过wlan0接口转发出去,实现SNAT功能
- `sudo iptables -t nat -A PREROUTING -i wlx081079db1327 -p tcp --dport 80 -j DNAT --to-destionation 192.168.20.2:80` 这样就实现了DMZ功能,即向外网开放局域网的服务,外网通过访问public IP 192.168.0.103即可访问到局域网中192.168.20.2:80提供的网络服务
- `sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-ports 8001` 对本机的端口进行转换

## 问题定位

### 网卡设置了nat流量转发,但是无法通过树莓派来实现转发效果

- 最可能就是网卡没有开启流量转发的配置开关
- `echo 1 > /proc/sys/net/ipv4/ip_forward`
- `echo 1 > /proc/sys/net/ipv4/conf/wlan0/forwarding`

### 开启nat流量转发功能后无法实现ping域名功能

- 最可能就是dns的解析配置有问题,
- `vi /etc/resolv.conf` 修改到正确的dns配置`nameserver 192.168.43.1`或者是路由器的配置

## 参考

