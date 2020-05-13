---
title: vim-plug
date: 2018-10-02 22:25:00	
modify: 
tag: [plug]
categories: Vim
author: wmsj100
mail: wmsj100@hotmail.com
---

# vim-plug

## 概述
- `curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim` 
- 下载plug的配置文件,并且设置目录

   ```bash
	call plug#begin('~/.vim/plugged')
	Plug 'mattn/emmet-vim'
	Plug 'scrooloose/nerdtree'
	Plug 'tomasr/molokai'
	Plug 'nvie/vim-flake8'
	call plug#end()

	set number
	syntax on
	set tabstop=4
	set shiftwidth=4
	set smarttab
	set autoindent
	set smartindent
	filetype indent on

	set encoding=utf-8
	set termencoding=utf-8
	set helplang=cn
	map <F2> :NERDTreeToggle <CR>
	```
- source ~/.vimrc
- 进入`vim`界面,`PlugInstall`进行插件安装

## 参考
- []()
