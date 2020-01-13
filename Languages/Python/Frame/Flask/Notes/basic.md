---
title: basic
date: 2020-01-12 18:07:01
modify: 
tags: [Notes]
categories: Flask
author: wmsj100
email: wmsj100@hotmail.com
---

# basic

## 概要

- flask是python的轻量级框架，启动flask本身操作也比较简单
- `export FLASK_ENV=development` # 开启开发者模式，这样启动flask服务器后，如果python文件变动了会自动加载
- `export FLASK_APP=hello.py`
- `flask run --host=0.0.0.0` 默认启动后只允许本地服务器访问，配置host参数后可以在其他电脑中通过IP来访问
- hello.py代码如下
```python
from flask import Flask,escape
app = Flask(__name__)

@app.route('/')
def index():
    return "index page"

@app.route('/hello')
def hello():
    return 'hello page'

@app.route('/user/<username>')
def show_user(username):
    return "User %s" % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'Subpath %s' % escape(subpath)
```

## 参考

