---
title: pipenv
date: 2020-07-20 11:18:16
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# pipenv

## 概要

- `pipenv` 是python的一个包管理器，集成了pip, virtualenv还有自己的依赖管理的操作。
- 通过pipenv管理的依赖会出生成俩个文件`Pipfile`和`Pipfile.lock`，前者保存的软件，后者是该软件的所有依赖的软件对应的shd512公钥签名
- 使用了pipenv来管理软件就省去了自己部署virtualenv或者是执行`python -m venv env36`类似这样的操作了，而且对于依赖的包管理器更加精确，可以确保当前环境是完全可以复制和重新构建的。

## 命令

- `pipenv install` 依据当前目录的Pipfile来安装软件
- `pipenv install flask uwsgi` 安装指定软件并更新`Pipfile.lock`文件
- `pipenv uninstall` 卸载所有软件
- `pipenv shell` 进入pipenv的环境
- `pipenv run uwsgi --init uwsgi.ini` 使用pipenv的环境的命令来执行命令

## docker

- 在docker里使用pipenv需要执行如下命令
- `pipenv install --deploy --ignore-pipfile` 
	- `deploy` 如果Pipfile.lock文件过期，这样不会报错
	- `ignore-pipfile` 
- `CMD ["pipenv", "run", "--ini", "uwsgi.ini"]`


## 参考

- [docker pipenv](https://stackoverflow.com/questions/46503947/how-to-get-pipenv-running-in-docker)
