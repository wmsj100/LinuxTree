---
title: ibus-libpinyin
date: 2020-03-22 18:07:34
modify: 
tags: [Notes]
categories: ArchLinux
author: wmsj100
email: wmsj100@hotmail.com
---

# ibus-libpinyin

## 概要

- 安装中文输入法,ibus-libpinyin,安装这个是因为在ubuntu的gnome中使用的就是这个输入法,而且也一直在调教这个输入法,有了自己的词库,所以就保持用这个输入法了.

## 安装

- `sudo pacman -S ibus` 
- `sudo pacman -S ibus-libpinyin`
- `ibus-setup` 在tty1界面执行这个操作,
	- 如果提示ibus没有运行,且有下面类似提示
```
IBus has been started! If you cannot use IBus, please add below lines in $HOME/.bashrc, and relogin your desktop.
（译：IBus已启动！如果您还不能用Ibus,请您先将以下的三行代码加到$HOME/.bashrc，再重新登录。)
  export GTK_IM_MODULE=ibus
  export XMODIFIERS=@im=ibus
  export QT_IM_MODULE=ibus
```
	- 复制上面'export'内容到`$HOME/.xprofile`
	- `vi ~/.xprofile`添加`ibus-daemon -x -d`
- 重启电脑,或者再次执行`ibus-setup`添加输入法,并且进行一些设置
- 重启电脑,可以愉快的中文输入了.

## 参考

- [archlinux ibus中文输入法](https://wiki.archlinux.org/index.php/IBus_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))
