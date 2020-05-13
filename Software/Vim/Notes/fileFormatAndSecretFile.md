---
title: 文件格式和文件加密
date: 2017-12-13
tags: [vim]
categories: Linux
---

- :set fileformat 查看当前文档的文件格式，有三种格式；unix/ <LF>; dos/ <CR><LF>; mac/ <CR>
- :set fileformat=unix 把当前编辑文件转换为unix格式

## 加密解密
- vim -x f1.txt 用加密的形式打开文件，文件保存后会以乱码的形式显示，只有输入正确的密码才可以查看到正确的内容。即便是乱码的形式，还是可以继续输入或者编辑文件。
- :set key= 对于设置了加密文件通过这个方法可以解密文件
- :X 已经在vim编辑内部，可以通过这个方法来给文件加密
- vim -x -n file.txt 以加密的方式并且不生成暂存文件，因为虽然文件是加密的，但是暂存文件是没有加密的，
- :setlocal noswapfile 如果已经在vim界面了，可以通过这个方法来禁用交换文件
