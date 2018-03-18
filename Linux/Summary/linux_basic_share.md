---
name: linux技术分享
date: 2018-02-27
tag: [linux]
categories: Linux
user: wmsj100
email: wmsj100@hotmail.com
---

# 技术分享：

> 我们做的事情，后来人也会做，而且可以做的更好; 
> 他们做的事情，那些成就和辉煌，只有他们能配的上!

## 开源介绍
> 如果真正喜欢一个东西，就会去追寻它经历的故事

- 我（以土鳖的口吻追忆当年）15年开始接触Git，当我成功的用Git提交代码到github远程库的时候真的是利器在手，天下我有的感觉；然后就去谷歌（那时候还有钱买VPN）了解它的故事，才知道是林纳斯·托瓦兹（Linus Torvalds）写的，然后果断就成偶像了；
- 然后就去八卦他的故事，才知道linux内核也是他写的，还是瑞典人；挨着芬兰，就是诺基亚的老家；
- 后来又接触到MySQL，才就知道MySQL也是瑞典人写的，然后就去了解这个人才辈出的国家的历史，发现它是一个很小的中立国，二战时候还帮希特勒运物资。。。XD

> 学新事物的同时去了解它背后的故事，因为故事也可以成为坚持的理由；

- AT&T公司的贝尔实验室 （撕毁了和华为的手机销售合同）

- 丹尼斯·里奇 （实验室成员）  C语言的创造者、UNIX之父  图灵奖得主    

- 1983 GNU（GNU's Not Unix!的递归缩写）理察·马修·斯托曼  （大胡子，就是那个把笔记本挂脖子上等车时候写代码的人）写了 c语言编译器 GCC（免费）、Emacs（开发语言编辑器有三种： Vim、Emacs、其它）、写了GNU通用公共许可协议（GPL，现在主流的开源协议）

- 布莱恩·福克斯（是大胡子的组员，写了最牛逼的Bash）， 几乎所有类unix的默认shell； Shell是一个命令解释器，是系统的用户界面，提供了用户与内核（Unix）进行交互操作的一种接口。它接收用户输入的命令并把它送入内核去执行，Shell有自己的编程语言（shell脚本），所有的服务器操作都是在shell上操作，没有视窗（xwindows）

- AT&T公司收回Unix版权争夺，拒绝授权学术机构 

- 一个程序员为了保住大学教师职位（Unix源码不让教，他在大学就是教这个的），写了一个乞丐版类Unix系统内核，（完全自己写，坚持初心，拒绝商业诱惑（但是会销售光盘赚小钱），只为了教学，拒绝优化和升级）

- 1991 林纳斯·托瓦兹（Linus Torvalds）linux之父 （他最为人熟知的就是对英伟达竖中指）（买了老师的光盘，参考了内核原理，在思想的引导（没有复制代码）（版权意识）最高级重构）linux内核  接受提意见，积极和粉丝沟通，主动积极做优化升级、（学老师卖光盘）

## linux
- linux 分享linux系统用户、常见命令（cd/ pwd/ touch/ echo/ mkdir/ ll/ ）文件权限（用户和用户组 ）常见命令（chmod/ chown/ chgrp ），
最后针对微服务常用脚本（服务重启、关闭）无法触发，提示命令找不到的解决办法，常见命令或脚本的帮助信息（--help man）的使用