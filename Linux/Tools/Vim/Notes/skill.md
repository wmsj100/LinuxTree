---
title: 小技巧
date: Mon 11 Dec 2017 11:10:51 PM CST
tag: [vim]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

- :s/\([^,]\), \(.*\)/\2 \1/ 交换位置，效果： "John, Doe" ==> "Doe John"
- :.,/^$/-1!sort 排序，知道碰到空行为止
- :g/^/m 0 反转文档的内容，效果等同于tac
- g ctrl g  g和ctrl 之间没有空格，这样会统计数据，包括在第几行第几列，第几个单词
- :%s/\s\+$// 删除行末的空格
