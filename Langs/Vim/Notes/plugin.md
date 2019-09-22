---
title: vim插件
date: Sat 16 Dec 2017 11:07:48 PM CST
modify: 2019-04-20 09:32:12	
tag: [vim, vimPlugin]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

- 安装了很牛逼的vim插件，感觉瞬间就牛逼了，可以好好的学习插件的使用了，然后就是配置属于自己的插件了。
- 之前不能安装'vim'插件，是因为我的git版本有问题，所以就删除了重新安装了一个低版本git，然后问题就解决了。

http://www.cnblogs.com/wangweiwen/p/6103744.html

1,先安装vim，注意vim必须7.4以上版本，因为下面的插件要求7.4以后的版本
2,安装git
3,mkdir -p ~/.vim && touch ~/.vimrc
4,git clone https://github.com/gmarik/vundle.git ~/.vim/bundle/vundle
5,vi ~/.vimrc写入如下的内容, (见当前目录文件.vimrc);
6，vim 然后在normal模式下面，输入 “：PluginInstall”，然后回车
##  
