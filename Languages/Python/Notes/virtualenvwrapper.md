---
title: virtualenvwrapper
date: 2020-03-08 08:35:09
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# virtualenvwrapper

## 概要

- 之前关于python的虚拟化环境都是通过virtualenv来管理的,它的一个弊端是每次使用一个环境时候得先source目录的active
- 那就得先知道那些目录在哪里,通常做法是专们固定一个目录来存放那些库
- virtualenvwrapper自己接管了这些操作,通过会在~/.virtualenv目录存放这些文件

## 使用

- `sudo ln -s /usr/bin/python3 /usr/local/bin/python`
- 在`~/.bashrc`文件添加下面内容,只有在非root时候执行,其实这个判断无用,因为这个文件也是在当前用户的~/.bashrc,root用户就不会加载
```~/.bashrc
# python virtualenvwrapper config
export VIRTUALENV_USE_DISTRIBUTE=1
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export WORKON_HOME=$HOME/.virtualenvs
source /home/ubuntu/.local/bin/virtualenvwrapper.sh
export PIP_VIRTUALENV_BASE=$WORKON_HOME
export PIP_RESPECT_VIRTUALENV=true
```
- `source ~/.bashrc` 如果没有报异常就会自动创建下面文件
```
ubuntu@wmsj100:~/.local/bin$ source virtualenvwrapper.sh
virtualenvwrapper.user_scripts creating /home/ubuntu/.virtualenvs/premkproject
virtualenvwrapper.user_scripts creating /home/ubuntu/.virtualenvs/postmkproject
virtualenvwrapper.user_scripts creating /home/ubuntu/.virtualenvs/initialize
virtualenvwrapper.user_scripts creating /home/ubuntu/.virtualenvs/premkvirtualenv
virtualenvwrapper.user_scripts creating /home/ubuntu/.virtualenvs/postmkvirtualenv
virtualenvwrapper.user_scripts creating /home/ubuntu/.virtualenvs/prermvirtualenv
virtualenvwrapper.user_scripts creating /home/ubuntu/.virtualenvs/postrmvirtualenv
virtualenvwrapper.user_scripts creating /home/ubuntu/.virtualenvs/predeactivate
virtualenvwrapper.user_scripts creating /home/ubuntu/.virtualenvs/postdeactivate
virtualenvwrapper.user_scripts creating /home/ubuntu/.virtualenvs/preactivate
virtualenvwrapper.user_scripts creating /home/ubuntu/.virtualenvs/postactivate
virtualenvwrapper.user_scripts creating /home/ubuntu/.virtualenvs/get_env_details
```
- `mkvirtualenv -p python3 env36` 创建基于python3的虚拟环境env36
```
ubuntu@wmsj100:~/.virtualenvs$ mkvirtualenv -p python3 env36
created virtual environment CPython3.6.9.final.0-64 in 184ms
  creator CPython3Posix(dest=/home/ubuntu/.virtualenvs/env36, clear=False, global=False)
  seeder FromAppData(download=False, pip=latest, setuptools=latest, wheel=latest, via=copy, app_data_dir=/home/ubuntu/.local/share/virtualenv/seed-app-data/v1)
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator
virtualenvwrapper.user_scripts creating /home/ubuntu/.virtualenvs/env36/bin/predeactivate
virtualenvwrapper.user_scripts creating /home/ubuntu/.virtualenvs/env36/bin/postdeactivate
virtualenvwrapper.user_scripts creating /home/ubuntu/.virtualenvs/env36/bin/preactivate
virtualenvwrapper.user_scripts creating /home/ubuntu/.virtualenvs/env36/bin/postactivate
virtualenvwrapper.user_scripts creating /home/ubuntu/.virtualenvs/env36/bin/get_env_details
```
- `mkvirtualenv -p python2 env27` 创建基于python2的虚拟环境env27
```
(env36) ubuntu@wmsj100:~/.virtualenvs$ mkvirtualenv -p python2 env27
created virtual environment CPython2.7.17.final.0-64 in 377ms
  creator CPython2Posix(dest=/home/ubuntu/.virtualenvs/env27, clear=False, global=False)
  seeder FromAppData(download=False, pip=latest, setuptools=latest, wheel=latest, via=copy, app_data_dir=/home/ubuntu/.local/share/virtualenv/seed-app-data/v1)
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator
virtualenvwrapper.user_scripts creating /home/ubuntu/.virtualenvs/env27/bin/predeactivate
virtualenvwrapper.user_scripts creating /home/ubuntu/.virtualenvs/env27/bin/postdeactivate
virtualenvwrapper.user_scripts creating /home/ubuntu/.virtualenvs/env27/bin/preactivate
virtualenvwrapper.user_scripts creating /home/ubuntu/.virtualenvs/env27/bin/postactivate
virtualenvwrapper.user_scripts creating /home/ubuntu/.virtualenvs/env27/bin/get_env_details
```
- deactive 推出虚拟环境
- `workon env36` 进入虚拟环境env36

## 参考

- [python virtualenvwrapper 介绍](https://www.cnblogs.com/hougang/p/11423083.html)
