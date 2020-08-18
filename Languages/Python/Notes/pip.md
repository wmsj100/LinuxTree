---
title: pip
date: 2018-03-18 22:38:10 Sun
modify: 2020-08-18 10:39:47 
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

---
- `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py` 
- `python get-pip.py`

## 指定版本

- `pip install asgiref==3.2.7` 俩个等于号

## pip源码编译

- `pip install git+https://github.com/pymssql/pymssql.git`
- `pip install /tmp/a.tar`
- `pip install ./pymssql`
- 上面三种方式都可以通过源码编译的方式来安装包

## pip离线下载

- `pip3 download -r requirements.txt` 这样会在当前目录下载whl或tar包
- `pip install xxx.whl`
- `pip install xxx.tar.gz`

## pip 查看包信息

- `pip list` 获取包名称
- `pip show scipy` 可以获取包信息
```pip
Name: scipy
Version: 1.4.1
Summary: SciPy: Scientific Library for Python
Home-page: https://www.scipy.org
Author: None
Author-email: None
License: BSD
Location: /root/.local/share/virtualenvs/root-BuDEOXnJ/lib64/python3.6/site-packages
Requires: numpy
Required-by: scikit-learn, seaborn, pyltr
(root) [root@pythonTest ~]# cd /root/.local/share/virtualenvs/root-BuDEOXnJ/lib64/python3.6/site-packages/
``` 

## pip 导出列表

- `pip freeze > requirements.txt`
- `pip install -r requirements.txt`

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
