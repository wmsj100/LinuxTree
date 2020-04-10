---
title: install
date: 2020-04-07 20:06:48
modify: 
tags: [Notes]
categories: MongoDB
author: wmsj100
email: wmsj100@hotmail.com
---

# install

## 概要

- 使用源码包的方式来编译安装

## 安装

- `yum install -y unzip python-devel libcurl-devel openssl openssl-devel python-setuptools.noarch libxml2-devel   libffi-devel     libxml2 glibc-static libstdc++-static  lzip2   python2-cryptography`
- `pip install typing`
- 当前环境没有pip
	- `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py` 
	- `python get-pip.py`
	- `pip install --upgrade pip` 升级pip
- `wget http://www.rpmfind.net/linux/fedora/linux/releases/30/Everything/aarch64/os/Packages/i/isl-0.16.1-8.fc30.aarch64.rpm` 安装isl
- `rpm  -ivh  isl-0.16.1-8.fc30.aarch64.rpm`

## 升级gcc

- 当前编译环境需要高版本gcc，当前升级到gcc-7.3.0
- `wget https://mirrors.tuna.tsinghua.edu.cn/gnu/gcc/gcc-7.3.0/gcc-7.3.0.tar.gz`
- `tar -xvf gcc-7.3.0.tar.gz`
- `cd gcc-7.3.0`
- `./contrib/download_prerequisites` 下载依赖的gmp/mpfr/mpc
- `./configure --prefix=/usr/local/gcc-7.3.0  --enable-bootstrap  --enable-checking=release --enable-languages=c,c++ --disable-multilib` 进入解压包执行这个命令，进行依赖包安装，该脚本会自动下载、配置、安装依赖库
- `make -j4` 当前虚拟机使用4核，所用用4个cpu来同时编译，提高编译速度
- `make install` 安装
	- 刚开始因为目标位置写错，需要重新执行configure，再执行之前需要把之前生成的MakeFile和编译的二进制删除，否则可能会报错
	- `make clean-dir`
- 替换gcc和动态库
	- `ln -sf /usr/local/gcc-7.3.0/bin/gcc /usr/bin/gcc`
	- `ln -sf /usr/local/gcc-7.3.0/bin/g++ /usr/bin/g++`
	- `rm -rf /usr/lib64/libstdc++.so.6`
	- `cp /usr/local/gcc-7.3.0/lib64/libstdc++.so.6.0.24 /usr/lib64/`
	- `ln -s /usr/lib64/libstdc++.so.6.0.24 /usr/lib64/libstdc++.so.6`
- `gcc --version`可以看到已经升级到目标版本

## 安装mongodb

- `wget -T 10 -O mongo-r4.0.3.zip http://github.com/mongodb/mongo/archive/r4.0.3.zip`
- `unzip mongo-r4.0.3.zip`
- `cd mongo-r4.0.3`
- `sed -i '2c cryptography >= 2.0.0' buildscripts/requirements.txt`
- `pip install -r buildscripts/requirements.txt`
	- 执行这个安装时有报错,查询资料时setuptools版本太低
	- `pip install --upgrade setuptools` 升级再重新执行ok
- `python buildscripts/scons.py mongod MONGO_VERSION=4.0.3 CCFLAGS="-march=armv8-a+crc" --disable-warnings-as-errors` 
	- 开始编译，这个过程很久，用来2个半小时
- `python buildscripts/scons.py --prefix=/opt/mongo install MONGO_VERSION=4.0.3 CCFLAGS="-march=armv8-a+crc" --disable-warnings-as-errors`
	- 开始安装，会再/opt目录下创建mongo目录，里面只有一个bin目录，是几个可执行文件

## 验证

- `mkdir -p /data/db`
- `cd /opt/mongo/bin`
- `./mongod` 启动mongod服务
- `./mongo` 重新开启终端，进入mongo的shell界面
- `use mongodatabase`
- `show dbs` 可以看到当前的打印表示安装成功

## 参考

