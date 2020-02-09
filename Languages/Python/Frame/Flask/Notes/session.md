---
title: session
date: 2020-02-09 20:18:15
modify: 
tags: [Notes]
categories: Flask
author: wmsj100
email: wmsj100@hotmail.com
---

# session

## 概要

- 允许在不同请求之间存储信息
- 这个对象相当于用密钥签名加密的cookie
- 用户可以查看cookie，但是因为没有密钥，所以无法解密cookie
- 使用session，必须先设置一个密钥

## 设置密钥

- 生成随机数的关键在于一个好的随机种子，因此一个好的密钥应当有足够的随机性。
- `os.urandom(16)` 生成16位的随机数

## 范例

- 通过`index`访问，如果在session中读取不到`username`，就跳转到`login`进行登录操作
- `logout`进行登出，从session中删除`username`

```python
from flask import Flask
from flask import request
from flask import url_for
from flask import redirect
from flask import session
from flask import escape
import os

app = Flask(__name__)

app.secret_key = os.urandom(16)
def index_fn():
    if 'username' in session:
        return 'Login in as {}'.format(escape(session['username']))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index_fn'))
    return '''
        <form action="" method="post">
            <p><input type="text" name="username"></p>
            <p><input type="submit" value="login"></p>
        </form>
        '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index_fn'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
## 参考

- [flask](https://dormousehole.readthedocs.io/en/latest/quickstart.html)
