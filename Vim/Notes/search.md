---
title: 查找命令
date: 2017-12-14
tags: [vim]
categories: Linux
---

- :set ingorecase smartcase 这个是聪明的忽略大小写设置，如果不输入大写字母，会查找到所有的大小写值，如果输入一个大写字母，就开始区分大小写搜索
- /\cworld 这个可以屏蔽掉'vimrc'设置中添加的关于'ingorecase'的设置，不区分大小写。
- /\Cworld 这个是对当前这一次搜索区分大小写
- /world/e 光标位于搜索值的末尾
- /world/e+2 光标位于搜索值的
- /world/b 光标位于搜索值的首部
- /world/b+2 光标位于搜索值首部往右走俩个字符
- /world/b-2 光标位于搜索值首部往左走俩个字符
- /m/{2,4} 查找'm'重复2到4次的值
- /scope\|business 搜索scope或者business
