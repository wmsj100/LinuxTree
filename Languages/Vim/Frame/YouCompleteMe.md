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

## 报错

- 下载完成后执行安装过程中报错
```
ubuntu@Ubuntu:~/.vim/plugged/youcompleteme$ python3 ./install.py --clang-completer
Searching Python 3.6 libraries...
Found Python library: /usr/lib/python3.6/config-3.6m-x86_64-linux-gnu/libpython3.6.so
Found Python headers folder: /usr/include/python3.6m
-- The C compiler identification is GNU 7.5.0
-- The CXX compiler identification is unknown
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
CMake Error at CMakeLists.txt:26 (project):
  No CMAKE_CXX_COMPILER could be found.

  Tell CMake where to find the compiler by setting either the environment
  variable "CXX" or the CMake cache entry CMAKE_CXX_COMPILER to the full path
  to the compiler, or to the compiler name if it is in the PATH.


-- Configuring incomplete, errors occurred!
See also "/tmp/ycm_build_aeyiw3_h/CMakeFiles/CMakeOutput.log".
See also "/tmp/ycm_build_aeyiw3_h/CMakeFiles/CMakeError.log".
ERROR: the build failed.

NOTE: it is *highly* unlikely that this is a bug but rather
that this is a problem with the configuration of your system
or a missing dependency. Please carefully read CONTRIBUTING.md
and if you're sure that it is a bug, please raise an issue on the
issue tracker, including the entire output of this script
and the invocation line used to run it.
```
- 查找资料提示缺少lib库
- `sudo apt install gcc`
- `./install.py` 没有添加后面的`--clang-completer`,因为对与C语言暂时没有补全的需求
- 编译成功
- `python3 install.py --go-completer` 添加go语言的补全

## 参考

- [YouCompleteMe解析](https://blog.csdn.net/weixin_44638957/article/details/91985270)
- [vim配置](https://www.jianshu.com/p/8426cef1f4f5)
- [YouCompleteMe编译报错](https://askubuntu.com/questions/152653/cmake-fails-with-cmake-error-your-cxx-compiler-cmake-cxx-compiler-notfound)
- [issue error](https://github.com/ycm-core/YouCompleteMe/issues/2945)
