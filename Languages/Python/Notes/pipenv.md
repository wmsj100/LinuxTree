---
title: pipenv
date: 2020-02-02 13:00:34
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# pipenv

## 概要

- `pipenv`是可以替换`pip`的一种更加高级的包管理器，是`python`的项目的依赖管理器，可以简化依赖关系管理的常见使用情况。

## 换源

- `pipenv`和`pip`类似，也需要更换源，默认是官网，速度太慢
- 进入到要安装的项目目录，执行`pipenv install requests`，会先执行创建`virtualenv`等虚拟环境准备，然后开始下载`requests`，会卡在install阶段，然后停止下载，当前目录会生成一个文件`Pipfile`
- 修改`Pipfile`文件的source，更换`url`为国内源。
```Pipfile
[[source]]
name = "pypi"
url = "https://pypi.tuna.tsinghua.edu.cn/simple/"
verify_ssl = true

[dev-packages]

[packages]
requests = "*"

[requires]
python_version = "3.7"
```

## 参考

- [pipenv介绍](https://www.jianshu.com/p/d08a4aa0008e)
- [pipenv换源](https://blog.csdn.net/jpch89/article/details/81952416)
