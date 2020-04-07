---
title: gcc
date: 2020-04-01 09:44:12
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# gcc

## 概要

- gcc是c的编译器
- centos7自带的gcc版本太低，需要手动升级

## 升级流程

- 当前系统自带gcc版本是4.8.5,目标gcc版本是`5.4.0`
- `wget https://mirrors.tuna.tsinghua.edu.cn/gnu/gcc/gcc-5.4.0/gcc-5.4.0.tar.gz`
- `tar -xvf gcc-5.4.0.tar.gz` 解压时候不需要指定压缩格式，tar会自己进行判断
- `yum install -y gcc  gcc-c++  glibc-static libstdc++-static  kernel-devel` 先安装这些依赖，避免安装出错
- `./contrib/download_prerequisites` 安装依赖，如果依赖包下载失败，可以打开这个文件查看要安装的依赖版本号，单独安装
	- `wget https://gcc.gnu.org/pub/gcc/infrastructure/gmp-6.1.0.tar.bz2`
	- `wget https://gcc.gnu.org/pub/gcc/infrastructure/isl-0.16.1.tar.bz2`
	- `wget https://gcc.gnu.org/pub/gcc/infrastructure/mpc-1.0.3.tar.gz`
	- `wget https://gcc.gnu.org/pub/gcc/infrastructure/mpfr-3.1.4.tar.bz2`
	- 这个下载操作是在gcc的解压目录执行下载，然后重新执行这个download_prerequisites
- `./configure --prefix=/usr/local/gcc  --enable-bootstrap  --enable-checking=release --enable-languages=c,c++ --disable-multilib` 进入解压包执行这个命令，进行依赖包安装，该脚本会自动下载、配置、安装依赖库
	- `--prefix=/usr/local/gcc` 指定安装路径
	- `--enable-bootstrap` 用第一次编译生成的程序进行第二次编译，然后用第二次生成的程序进行第三次编译，并且检查比较第二次和第三次结果的正确性，也就是进行冗余的编译检查工作。非交叉编译环境下，默认已经将该值设置为enable，可以不用显示指定；交叉编译环境下，需要显示将值设为disable
	- `--enable-checking=release` 以软件发布版的标准来对编译时生成的代码进行一致性检查；设置该选项为enalbe并不会改变编译器生成的二进制结果，但是会导致编译的时间增加；该选项仅支持gcc编译器；
	- `--enable-languages=c,c++` 支持的高级语言类型和运行时库，可以设置的所有语言包括“ada,c,c++,Fortan,java,objc,obj-c++,GO”.这里只开启了c和c++，就需要安装越多的相应静态库与动态库。
	- `--disable-multilib` 如果操作系统是32位，默认就已经设置为disable，这意味着gcc仅能生成32位的可执行程序；如果系统是64位，默认就已经设置为enable,;
- `./configure --prefix=/usr/local/gcc --disable-checking  --enable-languages=c,c++  --disable-multilib` 上面的检查过程非常漫长，可以禁用检查来提升速度
- `mkdir /usr/local/gcc-5.4.0` 创建要存放编译后的文件的位置
- `make -j4` 参数j可利用多核cpu加快编译速度
	- `cat /proc/cpuinfo | grep "processor" | wc -l`确定核数
- `make install`
- 安装完成后的替换
	- `ln -sf /usr/local/gcc/bin/gcc /usr/bin/gcc`
	- `ln -sf /usr/local/gcc/bin/g++ /usr/bin/g++`
	- `rm -rf /usr/lib64/libstdc++.so.6`
	- `cp /usr/local/gcc/lib64/libstdc++.so.6.0.24 /usr/lib64/`
	- `ln -s /usr/lib64/libstdc++.so.6.0.24 /usr/lib64/libstdc++.so.6`

## 遇到问题

- 首先在安装之前我已经把低版本的gcc卸载了，然后安装高版本，但是在config时候会涉及到C编译的问题，但是当前系统无法找到可以编译C的编译器，所以只能先把低版本的gcc重新安装回来，然后在进行编译

## configure error

- `configure: error: Building GCC requires GMP 4.2+, MPFR 2.4.0+ and MPC 0.8.0+.` 执行config时候报错
	- `wget https://mirrors.tuna.tsinghua.edu.cn/gnu/mpfr/mpfr-4.0.2.tar.gz`
	- `wget https://mirrors.tuna.tsinghua.edu.cn/gnu/gmp/gmp-6.2.0.tar.xz`
	- `wget https://mirrors.tuna.tsinghua.edu.cn/gnu/mpc/mpc-1.1.0.tar.gz`
- 分别解压并执行`configure`
	- 配置gpm时候报错提示没有“m4”，`yum install m4`重新开始配置
	- 配置mpc时候报错`configure: error: libmpfr not found or uses a different ABI (including static vs shared).` 提示mpfr没有找到，所以需要先安装mpfr，就是说mpc依赖与mpfr

## 报错缺少动态库

- 编译gcc时候还是报错缺少动态库，在根目录查找是有这个动态库的，
- 查询资料有俩个方法可以解决，一个是在编译时候指定当前动态库，当时测试失败了，升级gcc-5.4.0
- 导出环境变量`export DL_LIBRARY_PATH_=/usr/local/lib`，然后再执行编译就好了。

## 参考

- [gcc 源码安装](https://www.cnblogs.com/as007012/articles/10045011.html)
- [gcc 源码安装参考](https://blog.csdn.net/lucboll/article/details/93464729)
- [gcc 源码安装](https://www.huaweicloud.com/kunpeng/software/gcc.html)
