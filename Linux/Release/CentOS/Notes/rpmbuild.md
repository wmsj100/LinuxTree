---
title: rpmbuild
date: 2020-04-01 07:50:54
modify: 
tags: [Notes]
categories: CentOS
author: wmsj100
email: wmsj100@hotmail.com
---

# rpmbuild

## 概要

- RPM: Redhat Package Manager
- 通过自定义rpm包，统一管理，或者一键环境安装，就需要使用rpmbuild来进行编译。
- 制作RPM包最主要的就是写SPEC文件，完成来就会用rpmbuild命令根据SPEC文件制作RPM包。
- 这个文件会指引你在CentOS下安装及设置一个用来创建RPM的环境
- 切勿以root身份来创建RPM,这个工作应该永远在一个没有特殊权限的户口内执行.以root的身份来创建RPM可能会损坏系统.

## rpmbuild搭建

- `yum install pcre-devel zlib-devel openssl-devel make cmake gcc gcc-c++ bison ncurses-devel rpm-build  -y`
- `yum install rpmdevtools` 安装rpm开发包
- `rpmdev-setuptree` 会自动生成`BUILD/SOURCES/RPMS/SPECS/SRPMS/.rpmmacros`等文件和目录
- `rpmdev-newspec` 会在当前目录生成一个默认的spce模板

## rpmbuild目录介绍

- BUILD: 编译rpm包的临时目录
- RPMS: 最终生成的可安装rpm包的所在目录
- SOURCES: 所有源代码和补丁文件的存放目录
- SPECS: 存放SPEC文件的目录
- SRPMS: 软件最终的rpm源码格式存放路径

## rpmbuild命令

- `bp` 只执行%pre段(解开源码包并打补丁，即只做准备)
- `bc` 执行spec的%pre和%build段(准备并安装)
- `bi` 执行spec的%pre/%build/%install(准备，编译并安装)
- `bl` 检查spec的%file(查看文件是否齐全)
- `ba` 建立源码与二进制包(常用):即编译后做成*.rpm和*.src.rpm
- `bb` 建立二进制包(常用):即编译后做成*.rpm
- `bs` 只建立源码包:即只做成*.src.rpm
- tc/ti/tb/ts功能类似，只是所需参数由spce文件变成tar包

## 命令

- `sudo yum install rpm-build` 安装rpm-build
- `rpmbuild --showrc`
- `rpmbuild --version` 查看版本
- `rpm -q redhat-rpm-config` 大部分以CentOS作为重建目标的SRPM亦需要特点的rpmbuild创建宏及辅助脚本，他们都收录在redhat-rpm-config组件内。
- `sudo yum install redhat-rpm-config`

## 参考

- [centos rpmbuild wiki](https://wiki.centos.org/zh/HowTos/SetupRpmBuildEnvironment)
- [rpmbuild 构建](http://www.myjishu.com/?p=259)
- [rpmbuild 构建](https://blog.csdn.net/u012373815/article/details/73257754)
- [rpmbuild修改内容并重新打包](https://blog.csdn.net/hmxz2nn/article/details/98765997)
