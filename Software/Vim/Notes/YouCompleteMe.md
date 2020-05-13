---
title: YouCompleteMe
date: 2020-03-02 09:31:48
modify: 
tags: [Notes]
categories: Vim
author: wmsj100
email: wmsj100@hotmail.com
---

# YouCompleteMe

## 概要

- vim的一个自动补全插件

## 安装

- `Plugin 'Valloric/YouCompleteMe'`
- 进入vim，执行`PluginInstall`开始安装
- `git submodule update --init --recursive`下载细部文件到插件的各个目录
- `cd ~/.vim/bundle/YouCompleteMe`
- `./install.py --clang-completer` 前提是有安装`Cmake`，`sudo apt install cmake`
- `let g:ycm_global_ycm_extra_conf='/home/pi/.vim/plugged/YouCompleteMe/third_party/ycmd/.ycm_extra_conf.py'` 编辑`~/.vimrc`文件，添加该句

## 参考

- [youcompleteme插件安装](https://blog.csdn.net/weixin_44638957/article/details/91985270)
