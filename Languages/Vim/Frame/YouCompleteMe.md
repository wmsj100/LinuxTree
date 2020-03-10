---
title: YouCompleteMe
date: 2020-02-06 17:01:22
modify: 
tags: [Frame]
categories: Vim
author: wmsj100
email: wmsj100@hotmail.com
---

# YouCompleteMe

## 概要

- 这是一个vim的自动补全插件

## 安装

- `Plugin 'Valloric/YouCompleteMe'` 下载安装插件
- `cd /home/ubuntu/.vim/plugged/YouCompleteMe`
- `./install.py --clang-completer` 执行手动编译
	- 如果编译过程中提示缺失`cmake`，就安装缺少的插件`sudo apt install cmake`
- `let g:ycm_global_ycm_extra_conf='/home/ubuntu/.vim/plugged/YouCompleteMe/third_party/ycmd/.ycm_extra_conf.py'`  在`~/.vimrc`文件中添加该行命令

## 参考

- [YouCompleteMe解析](https://blog.csdn.net/weixin_44638957/article/details/91985270)
- [vim配置](https://www.jianshu.com/p/8426cef1f4f5)
