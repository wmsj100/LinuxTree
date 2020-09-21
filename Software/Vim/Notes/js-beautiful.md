---
title: js-beautiful
date: 2020-09-21 10:13:22
modify: 
tags: [Notes]
categories: Vim
author: wmsj100
email: wmsj100@hotmail.com
---

# js-beautiful

## 概要

- 这个插件是用来格式化js/css/html/json的插件
- 该插件的使用依赖于nodejs，所以需要先安装
- 通过会把调用映射为<c-f>

## 使用

- `sudo apt install nodejs`
- `git clone https://github.com/maksimr/vim-jsbeautify.git`
- `cd vim-jsbeautify`
- `git submodule update --init --recursive`
- `cp -a vim-jsbeautify ~/.vim/pluged/`
- `vim ~/.vimrc`
```.vimrc
map <c-f> :call HtmlBeautify()<cr>
autocmd FileType javascript noremap <buffer>  <c-f> :call JsBeautify()<cr>
autocmd FileType json noremap <buffer> <c-f> :call JsonBeautify()<cr>
autocmd FileType html noremap <buffer> <c-f> :call HtmlBeautify()<cr>
autocmd FileType css noremap <buffer> <c-f> :call CSSBeautify()<cr>

```
- `vim ~/.vim/.ed`
- `vim ~/.vim/.editorconfig`

```.editorconfig
;.editorconfig

root = true

[**.js]
indent_style = space
indent_size = 4

[**.json]
indent_style = space
indent_size = 4

[**.jsx]
e4x = true
indent_style = space
indent_size = 4

[**.css]
indent_style = space
indent_size = 4

[**.html]
indent_style = space
indent_size = 4
max_char = 78
brace_style = expand
```

## 参考

- [vim-jsbeautify](https://vimawesome.com/plugin/vim-jsbeautify)
