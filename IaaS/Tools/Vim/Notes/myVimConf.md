---
title: 我的vim配置
date: Sat 03 Mar 2018 03:22:13 PM CST
tag: [vim]
categories: Vim
author: wmsj100
mail: wmsj100@hotmail.com
---

## 我的vim简单配置
```shell
set nu
set tabstop=4
set shiftwidth=4
set softtabstop=4
set ruler
set history=50
set autoindent
set clipboard+=unnamed

autocmd BufNewFile *.md, exec  ":call SetTitle()"
let $author_name="wmsj100"
let $author_email="wmsj100@hotmail.com"
func SetTitle()
	call setline(1,"---")
	call append(line("."), "title: ".expand("%"))
	call append(line(".")+1, "date: ".strftime("%c"))
	call append(line(".")+2, "tag: []")
	call append(line(".")+3, "categories: Linux")
	call append(line(".")+4, "author: ".$author_name)
	call append(line(".")+5, "mail: ".$author_email)
	call append(line(".")+6, "---")
	call append(line(".")+7, "")
endfunc
```
