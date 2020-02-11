---
title: factory
date: 2020-02-11 13:01:27
modify: 
tags: [Notes]
categories: Flask
author: wmsj100
email: wmsj100@hotmail.com
---

# factory

## 概要

- 开始学习flask时候都是直接通过`app = Flask(__name__)`来创建一个app实例。
- 如果想要为每个实例分配不同的配置，就比较麻烦了。
- 通过调用一个函数来返回一个应用实例。

## 代码

```python
def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)
    from yourapplication.views.admin import admin
    from yourapplication.views.user import user
    app.register_blueprint(admin)
    app.register_blueprint(user)
    return app
```

## 配置启动脚本

```python
from flaskr import create_app

if __name__ == '__main__':
	app = create_app()
	app.run(debug=True, host='0.0.0.0', port=5050)
```

## uwsgi 配置文件

```uwsgi.ini
[uwsgi]
socket = 127.0.0.1:5060
pythonpath = /home/ubuntu/Github/python_study/flask/study4
module = run
wsgi-file = /home/ubuntu/Github/python_study/flask/study4/uwsgi.ini
callable = create_app()
processes = 1
threads = 1
daemonize = /home/ubuntu/Github/python_study/flask/study4/server.log
pidfile=/home/ubuntu/Github/python_study/flask/study4/uwsgi.pid
py-autoreload = 1
```

## 参考

- [flask工厂函数](https://blog.csdn.net/mr_hui_/article/details/83021510)
