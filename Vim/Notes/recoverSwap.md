---
title: 恢复文件 
date: Sat 11 Dec 2017 18:48:55 PM CST
tag: [vim]
categories: Tools
author: wmsj100
mail: wmsj100@hotmail.com
---

- vim -r userlist.js vim会读取交换文件
- vim在停止4秒或者输入大约2百字符以后才会更新交换文件。
  - :set updatetime // 4000 查看更新时间
  - :set updatecount // 200 查看更新计数
- vim -r 查看能找到的当前目录内容的交换文件
- o 用只读方式打开文件，只是想看看文件的内容，不打算恢复它的时候用这个选项，
- e 直接编辑，这个操作就是放弃暂存文件
- r 从交互文件中恢复文件，
- q 退出不再编辑
