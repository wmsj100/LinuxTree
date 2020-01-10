---
title: 构造URL
date: 2020-01-10 08:42:20
modify: 
tags: [Notes]
categories: Flask
author: wmsj100
email: wmsj100@hotmail.com
---

# 构造URL

## 概要

- 在Flask中的url建议通过构造的方法来定义，这个就像是Django中的路由页面
- url是可以灵活改变的，而且只是在配置页面定义，引用页面调用的是url的定义函数，
- 这样的优势是修改url时候只需要在配置页面变更url就可以

## 范例
```python
from flask import Flask,url_for
app = Flask(__name__)

@app.route('/')
def index():pass

@app.route('/login/')
def login():pass

@app.route('/user/<username>')
def profile(username): pass

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='wmsj100'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
```

## 参考

- [flask文档](http://docs.jinkan.org/docs/flask/quickstart.html)
