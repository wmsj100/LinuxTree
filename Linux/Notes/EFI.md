---
title: EFI
date: 2020-03-15 11:31:16
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# EFI

## 概要

- EFI: Extensible Firmware Interface 可扩展固件接口
- 英特尔公司再2000年开始,发明了可扩展固件接口,用以规范BIOS的开发.且替代BIOS的升级方案
- 支持EFI规范的BIOS也被称作EFI BIOS
- 为了推广EFI,业界多家著名公司成立了一个统一可扩展固件接口论坛(UEFI Forum)
- 英特尔公司将EFI1.1规范贡献给业界,用以制定新的国际标准UEFI规范.
- EFI在概念上非常类似于一个低阶的操作系统,并且具有操控所有硬件资源的能力.

## 和BIOS区别

- 一个显著的区别就是EFI BIOS是用模块化,C语言风格的参数堆栈传递方式,动态链接的形式构建的系统,较BIOS而言更易于实现,容错和纠错特性更强,缩短了系统研发时间.
- 它运行于32/64位模式,达到处理器最大寻址
- 它利用加载EFI驱动的形式,识别及操作硬件,不同于BIOS利用挂载实模式中断的方式增加硬件功能.

## 参考

