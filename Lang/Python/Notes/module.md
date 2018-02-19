---
title: 模块
date: Sun 31 Dec 2017 03:53:39 PM CST
tag: [python]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

## 基础概念
- import bar 通过导入同目录文件名来导入模块
- 包 `__init__.py`文件的目录可以用来作为一个包，目录里所有的`.py`文件都是这个包的子模块
- `help() ==> modules` 在'python'的帮助面板中输入`modules`可以查看所有可用的内建模块

## os
- 提供了与操作系统相关的功能
- os.getuid() 获取当前有效用户的id
- os.uname() 获取操作系统的信息
- os.getcwd() 获取当前工作目录
- os.chdir(path) 改变工作目录到'path'
- os.listdir(path) 获取目录`path`内的所有文件

## Requests 模块
- 提供了接口操作的功能
- 这个是第三方的模块，需要单独安装
- pip3 install Requests
    ```python
    import requests
    req = requests.get('http://www.baidu.com')
    req.status_code // 200
    ```
    
