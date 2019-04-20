---
title: read获取用户键盘输入
date: Tue 20 Feb 2018 12:07:21 PM CST
tag: [linux,shell]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

- read 读取来自键盘的输入并存储到变量中。
    - read -p 后面可以接提示符
    - read -t 后面接等待的秒数
    - read -p "Please input your name: " -t 30 named 有提示信息，提示用户在30s内输入用户名，并且存储到变量named 中。
- read atest 把用户键盘输入的值存储到变量`atest`中，通过`echo $atest`可以输出用户输入的信息。

