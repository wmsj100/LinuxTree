---
title: 网络基础概念
date: 2018-03-24 15:23:06 Sat
modify: 2018-03-24 15:23:06 Sat
tag: [net]
categories: Network
author: wmsj100
mail: wmsj100@hotmail.com
---

# 网络基础概念

## 网络分类
1. 电信网络：提供电话、电报和传值服务
2. 有线电视网络：提供各种电视节目
3. 计算机网络：使用户能够在计算机之间传输文件； 发展最快并且起到核心作用

## 网络名称解析
- Internet： 互联网 由数量极大的各种计算机网络互连起来
- 互联网特性：连通性和共享
- 互联网+：互联网+各个传统行业
- 网络： 集线器、链路、计算机构成
- 互联网： 路由器、网络、链路构成
- 主机： 与互联网相连的计算机
- ISP Internet Server Provider 互联网服务提供商
- RFC request for comments 请求评论
    - RFC文档更新后，陈旧的文档并不会被删除，而是一直保留
- 互联网上的主机必须有IP才可以上网
- IXP 互联网交换点 允许俩个网络直接相连并且交换分组，
- 进程： 运行着的程序，主机之间的通信实际上就是进程间的通信
- IP协议是互联网的核心

## 网络大事记
- 1983年 互联网诞生
- 1992年 互联网管辖权从美国政府转移到互联网协会
- 1994-4-20 中国接入互联网

## 互联网从工作方式划分
1. 边缘部分： 由所有连接在互联网上的主机组成
2. 核心部分： 由大量网络和连接这些网络的路由器组成，是互联网最复杂的部分

## 计算机通信方式
1. 客户-服务器方式：
2. 对等方式P2P：

## 路由器
- 路由器： 是一种专用计算机，是实现分组交换的关键构件，其任务是转发收到的分组，
- 路由器暂时存储的是一个个短分组，而不是整个的长报文，短分组是存储在路由器的存储器（内存）中而不是存储在磁盘中，这样保证了较高的交换速率。
- 如果某些节点或链路出现故障，通过路由选择协议路由器会自动找到转发分组最合适的路径
- 路由器只有在转发分组时候才占用一段通信资源，到达后会先暂存分组，然后之前占用的通信资源就释放了。

## 电信网
- 电信网： 由很多彼此连接起来的电信交换机
- 电路交换： 建立连接（占用通信资源）、通话（一直占用通信资源）、释放连接（归还通信资源）

## 分组交互
- 分组交换采用存储转发技术，表示把一个报文划分成几个分组后再进行传送。
- 报文： 通常把要发送的整块数据称为报文
- 在发送报文前先把较长的报文划分为一个个更小的等长数据段，每个数据段为1024bit，在每个数据段头部添加必要的控制信息组首部后就构成了一个分组。
- 分组又称为包，分组的首部称为包头。
- 分组是互联网中传送数据的单元。

## 网络类型
### 按照作用范围
1. 广域网WAN Wide Area Network
2. 城域网MAN Metropolitan
3. 局域网LAN Local
4. 个人区域网PAN Personal

### 按照使用者分类：
1. 公共网 public network
2. 专用网 private network

### 接入网
- 把用户接入互联网  这种网络称为接入网
- 本地接入网或居民接入网，是比较特殊的计算机网络，
- 接入网即不属于互联网的核心部分，也不属于计算机的边缘部分
- 接入网是某个用户客户端到互联网的第一个路由器（边缘路由器）直接的一种网络

## 网络性能指标
1. 计算机网络性能指标： 速率、带宽（单位时间内某信道所能通过的最高数据率）、吞吐量、时延（数据从一端传输到另一端所需的时间，也叫延迟；分为发送时延、传播时延、处理时延、排队时延）、时延带宽积、往返时间RTT、利用率（信道利用率、网络利用率： 信道或网络的利用率过高会产生非常大的时延）
2. 计算机网络的非性能指标：费用、质量、标准化、可靠性、可扩展性和可升级性、易于管理和维护

## 计算机网络体系结构
- SNA  System network Architecture 系统网络体系结构  IBM 提出 独家垄断 
- OSI/RM Open System Interconnection Reference Model 开发系统互联基本参考模型  七层协议的体系结构  是一个理论研究成功，商业化推广失败 
- TCP/IP 没有使用OSI标准，四层协议： 应用层、运输层、网际层IP、网络接口层
- 五层协议标准： 综合参考OSI和TCP/IP：应用层、运输层、网络层、数据链路层、物理层

### 五层协议
1. 应用层： 通过应用进程间的交互来完成特定网络应用，交互的数据单元是报文
2. 运输层：为进程之间的通信提供通用的数据传输服务（TCP、UDP）
     TCP：传输控制协议 Transmission Control Protocol 面向连接、可靠传输、报文段
     UDP：用户数据协议 User Datagram Protocol  无连接、尽力而为的传输、用户数据报
3. 网络层：负责为分组交换网上的不同主机提供通信服务，选择合适的路由，是源主机运输层传下来的分组能够通过网络中的路由器找到目的主机
    互联网是由大量异构网络通过路由器相互连接起来，互联网使用的网络层协议是无连接的网际协议IP和许多种路由选择协议。
4. 数据链路层：俩台主机之间的数据传输总是一段一段的链路上传送的，需要专门的链路层协议；链路层把网络层交下来的IP数据报组装成帧，在俩个相邻节点间的链路上传送帧，每一帧包括数据和必要的控制信息（同步信息、地址信息、查错控制）
5. 物理层： 传输的数据单位是比特
6. 媒介层： 包括传输网线、光纤等，这些不属于物理层，也不在TCP/IP协议内部，属于下层协议

## 网络协议核心
1. 语法：数据与控制信息的结构或格式
2. 语义：需要发出何种控制信息，完成何种动作以及作出何种响应
3. 同步：事件实现的顺序

## 网络分层
> 基于网络的复杂性，网络必须分层，分层的优势：
1. 各层之间独立
2. 灵活性好
3. 结构上可分割开
4. 易于实现和维护
5. 能促进标准化工作

## 协议名词
- 实体： 任何可以发送或接收信息的硬件或软件进程
- 协议： 控制俩个对等实体进行通信的规则集合
- 协议是水平的，服务是垂直的，要实现本层协议需要使用下层提供的服务
- 服务原语：上层与下层交互的命令
- SAP： Service Access Point 服务访问点 同一系统中相邻俩层的实体进行交互的地方，
- SDU: Service Data Unit 服务数据单元 层与层交换的数据的单位
