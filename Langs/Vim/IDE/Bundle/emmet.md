---
title: emmet
date: 2018-05-06 17:55:34 Sun
modify: 2018-05-06 17:55:34 Sun
tag: [frame]
categories: VIM
author: wmsj100
mail: wmsj100@hotmail.com
---

# emmet

## 概述
- 该插件的所有操作都是基于ctrl+y+， 组合

## 下载
- git clone https://github.com/boydos/emmet-vim.git
- cd emmet-vim
- cp plugin/emmet.vim ~/.vim/plugin/
- cp autoload/emmet.vim ~/.vim/autoload/
- cp -a autoload/emmet ~/.vim/autoload/
- 如果上面操作后不生效，就按照下面这个修改
- vi ~/.vimrc 'boydos/emmet-vim'
## 范例
- div>ul>li*3>span ctrl+y+,
- shift+v ul>li*3*
