---
title: pip
date: 2018-03-18 22:38:10 Sun
modify: 2020-01-09 22:18:20
tag: [pip,python,tool]
categories: Python
author: wmsj100
mail: wmsj100@hotmail.com
---

# pip python软件管理工具

## 软件安装
- https://pypi.python.org/packages/e5/8f/3fc66461992dc9e9fcf5e005687d5f676729172dda640df2fd8b597a6da7/pip-9.0.2.tar.gz#md5=2fddd680422326b9d1fbf56112cf341d 下载pip软件包
- tar -zxvf pip.tar.gz
- sudo python setup.py install 安装pip
- pip -V 查看pip版本号

## 配置pip源

### linux

- mkdir ~/.pip
- vi ~/.pip/pip.conf
```pip.conf
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```
- 重新开一个会话窗口，就可以执行pip命令了
- `sudo pip3 install virtualenv`
- 如果要执行上面的sudo命令来执行pip，需要在/root/下也创建相应的pip的配置文件
- `pip3 install --upgrade pip` 升级pip

### windows

- mkdir ~/pip
- vi ~/pip/pip.ini
```pip.ini
[global]

timeout = 6000

index-url = https://pypi.tuna.tsinghua.edu.cn/simple

trusted-host = pypi.tuna.tsinghua.edu.cn
```
- 进入cmd，执行`pip install --user pipenv` 安装
