---
title: ufw_or_iptables
date: 2020-03-17 14:13:22
modify: 
tags: [Notes]
categories: Ubuntu
author: wmsj100
email: wmsj100@hotmail.com
---

# ufw_or_iptables

## 概要

- ubuntu默认的防火墙是ufw,然后在ufw和iptables之间如何选择呢
- 专业人士的回答是建议使用ufw

## 答复

```
Iptables used to be how network was managed but as you might have observed it is messy to write and even more complicated to learn. UFW is an alternative to iptables and firewallD front-end network traffic controller applications.

For a newbie you will find ufw more easy to manage and use, and is Ubuntu's alternative to firewallD used by RHEL and it's derivatives. Iptables still lies underneath ufw but now you write these [iptable] rules using ufw. Also of note is the fact that firewallD lacks rate limiting feature found in ufw.

    The Uncomplicated Firewall (ufw) is a front-end for iptables and is particularly well-suited for host-based firewalls. ufw provides a framework for managing netfilter, as well as a command-line interface for manipulating the firewall. ufw aims to provide an easy to use interface for people unfamiliar with firewall concepts, while at the same time simplifies complicated iptables commands to help an administrator who knows what he or she is doing. ufw is an upstream for other distributions and graphical front-ends.

Put simply ufw is meant to remove all the complications that we see in iptable use and maintenance. Stick with ufw it still what it's designed for. In Ubuntu the configurations of ufw can be found in /etc/ufw and default configurations in /etc/default/ufw file. Looking in the /etc/ufw directory you will see the following files and folders:

after6.rules  after.init  after.rules  applications.d/
before6.rules  before.init  before.rules  sysctl.conf
ufw.conf  user6.rules  user.rules

You can add iptablelike rules in there too:

# allow all on eth0
-A ufw-before-input -i eth0 -j ACCEPT
-A ufw-before-output -o eth0 -j ACCEPT

A quick sudo cat /etc/ufw/user.rules will show you iptablelike rule sets stored from command line entries.
```

- 翻译如下:
```
iptables曾经是网络的管理方式，但是正如您可能已经观察到的那样，编写代码很麻烦，学习起来更加复杂。 UFW是iptables和FirewallD前端网络流量控制器应用程序的替代方案。

对于新手，您会发现ufw更易于管理和使用，它是Ubuntu替代RHEL及其衍生产品使用的firewallD的替代品。 iptables仍然位于ufw之下，但是现在您使用ufw编写这些[iptable]规则。另外值得注意的是，firewallD缺乏ufw中的速率限制功能。

    简易防火墙（ufw）是iptables的前端，特别适合基于主机的防火墙。 ufw提供了用于管理netfilter的框架，以及用于操纵防火墙的命令行界面。 ufw旨在为不熟悉防火墙概念的用户提供易于使用的界面，同时简化复杂的iptables命令，以帮助知道自己正在做什么的管理员。 ufw是其他发行版和图形前端的上游。

简单地说ufw是为了消除在iptable使用和维护中看到的所有复杂性。坚持使用ufw仍然是它的设计目的。在Ubuntu中，可以在/ etc / ufw中找到ufw的配置，在/ etc / default / ufw文件中可以找到默认配置。在/ etc / ufw目录中，您将看到以下文件和文件夹：

after6.rules after.init after.rules应用程序。d /
before6.rules before.init before.rules sysctl.conf
ufw.conf user6.rules user.rules

您也可以在其中添加iptablelike规则：

＃允许所有在eth0上
-A ufw-before-input -i eth0 -j ACCEPT
-A ufw-输出前-o eth0 -j接受

快速的sudo cat /etc/ufw/user.rules将显示从命令行条目存储的iptablelike规则集。
```

## 参考

- [ubuntu ufw or iptables](https://askubuntu.com/questions/952705/ufw-or-iptables-on-ubuntu-for-openvpn)
