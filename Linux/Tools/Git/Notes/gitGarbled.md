---
title: Git for windows 中文乱码解决方案
date: 2016-05-15
tags: [技巧]
categories: Frame
---
https://gist.github.com/nightire/5069597

> Git 是在linux下开发的，而 Linux 的编码方式是基于 UTF-8 的，所以移植到 Windows 之后难免会存在编码冲突，导致乱码。Git 在 Windows 下有多种乱码情况，请按具体情况操作～

$ git config --global core.quotepath false          # 显示 status 编码
$ git config --global gui.encoding utf-8            # 图形界面编码
$ git config --global i18n.commit.encoding utf-8    # 提交信息编码
$ git config --global i18n.logoutputencoding utf-8  # 输出 log 编码
$ export LESSCHARSET=utf-8
# 最后一条命令是因为 git log 默认使用 less 分页，所以需要 bash 对 less 命令进行 utf-8 编码

假设 Git 安装目录为 `C:\Git`

## 1.使用 git add 命令添加文件名含中文字符的文件时

##### 1.1 乱码类似：

```
    \316\304\261\276\316\304\265\265.txt

```

##### 1.2 解决方案：

编辑 `C:\Git\etc\inputrc` 文件中对应的行，查找以下2行，并修改其值，

编辑 `C:\Git\etc\inputrc` 文件中对应的行，查找以下2行，并修改其值，
原先：

```
    set output-meta off
    set convert-meta on
```

改为：

```
    set output-meta on
    set convert-meta off

```

## 2.使用git log查看含有中文的log信息时

##### 2.1 乱码类似：

```
    <E4><BF><AE><E6><94><B9><E6><96><87><E6><9C><AC><E6><96><87><E6><A1><A3>

```

##### 2.2 解决方案：

在Bash提示符下输入：

```
    git config --global i18n.commitencoding utf-8
    git config --global i18n.logoutputencoding gbk

```

注：设置 commit 提交时使用 utf-8 编码，可避免 Linux 服务器上乱码；同时设置在执行 `git log` 时将 utf-8 编码转换成 gbk 编码，以解决乱码问题。

注：设置 commit 提交时使用 utf-8 编码，可避免 Linux 服务器上乱码；同时设置在执行 `git log` 时将 utf-8 编码转换成 gbk 编码，以解决乱码问题。
编辑 `C:\Git\etc\profile` 文件，添加如下一行：

```
    export LESSCHARSET=utf-8

```

注：以使git log可以正常显示中文（需要配合：`i18n.logoutputencoding gbk`）

## 3.使用ls命令查看含有中文的文件名乱码时

##### 3.1 乱码类似：

```
    ????.txt
    ???????.md

```

##### 3.2 解决方案：

使用  **ls --show-control-chars**  命令来强制使用控制台字符编码显示文件名，即可查看中文文件名。

使用  **ls --show-control-chars**  命令来强制使用控制台字符编码显示文件名，即可查看中文文件名。
为了方便使用，可以编辑 C:\Git\etc\git-completion.bash 文件，添加如下一行：

```
    alias ls="ls --show-control-chars"

```

## 4.在Git Gui中查看UTF-8编码的文本文件时

##### 4.1 乱码类似：

```
    锘夸腑鏂囨枃妗￡

```

##### 4.2 解决方案：

在Bash提示符下输入：

```
    git config --global gui.encoding utf-8

```

注：通过上述设置，UTF-8 编码的文本文件可以正常查看，但是 GBK 编码的文件将会乱码，所以还是没有从根本上解决问题。

可行的方法之一为：将所有文本文件的编码统一为 UTF-8 或 GBK，然后设置相应的`gui.encoding` 参数为 `utf-8` 或 `gbk`。


解决 Git 在 windows 下中文乱码的问题

原因

中文乱码的根源在于 windows 基于一些历史原因无法全面支持 utf-8 编码格式，并且也无法通过有效手段令其全面支持。

解决方案

安装

设置（以下需要修改的文件，均位于 git 安装目录下的 etc/ 目录中）

2.1. 让 Git 支持 utf-8 编码

在命令行下输入以下命令：

$ git config --global core.quotepath false          # 显示 status 编码
$ git config --global gui.encoding utf-8            # 图形界面编码
$ git config --global i18n.commit.encoding utf-8    # 提交信息编码
$ git config --global i18n.logoutputencoding utf-8  # 输出 log 编码
$ export LESSCHARSET=utf-8
# 最后一条命令是因为 git log 默认使用 less 分页，所以需要 bash 对 less 命令进行 utf-8 编码
2.2. 让 ls 命令可以显示中文名称

修改 git-completion.bash 文件：

# 在文件末尾处添加一行
alias ls="ls --show-control-chars --color"
经过以上折腾之后，基本可以解决中文显示的问题。唯一的麻烦在于输入中文字符时会显示乱码，目前还没有完美的解决方案。

以下描述一个可用的临时方案：

前提条件：git commit 时，不用 -m 参数，也就是不在命令行下直接输入提交信息，而是敲回车，让 vim 来接管

进入 vim 后，按 i 键进入编辑模式，然后输入提交信息。（可多行）

输入完成后按 esc 退出编辑模式，然后输入 :wq，也就是写入+退出，即可。

如果进入 vim 后发现不能输入中文，那么先按 esc 退出编辑模式，然后输入：:set termencoding=GBK，即可。（也可能是 GB2312，都试一下）

还好我们有 GUI

实在搞不定命令行的童鞋，请直接使用各种 GUI 工具吧！

使用 eclipse IDE的，可以安装 EGit 插件

不使用 IDE 的，可以搜索一个叫做 SmartGit 的 GUI 客户端

That's All!