---
title: readonly
date: Tue 20 Feb 2018 04:47:21 PM CST
tag: [linux]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

# readonly 只读变量
- readonly b=1; 这样就创建了一个只读变量b，
- 它的作用和declare -r 效果一样
- 只读变量一旦创建就无法修改和删除，真的是删除都无法做到
- unset b; 会报错
- 只有退出这个shell重新进入一个shell才可以。
