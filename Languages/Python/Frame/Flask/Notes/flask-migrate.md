---
title: flask-migrate
date: 2020-07-27 20:56:41
modify: 
tags: [Notes]
categories: Flask
author: wmsj100
email: wmsj100@hotmail.com
---

# flask-migrate

## 概要

## 命令

- `python manage.py db migrate -m "Initial migration"` 第一次生成数据库文件
- `python manage.py db init` 初始化数据库
- `python manage.py db upgrade` 升级
- `python manage.py db --help` 帮助
- `migrate`每次执行会生成一个文件，同时会刷新数据库，数据库中会新增一个数据表。
- `python manage.py db downgrade` 在当前的提交执行降级操作，
- 每个commitid都对应一个upgrade和downgrade操作
- 这个工具和Django自带的migrate工具类似
- 使用这个工具最大的好处是可以把数据库的结构也纳入版本管理中，且可以随时回退操作

## 范例

```py
from webapp import create_app
from webapp.models import db, OracleUser, OracleUserTable, OracleTableDDL
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app()
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

def make_shell_context():
    return dict(app=app, db=db, OracleUser=OracleUser, OracleUserTable=OracleUserTable, OracleTableDDL=OracleTableDDL)

manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
```

## 参考

- [flask-migrate](https://www.jianshu.com/p/5fd8c2cbad3b)
- [flask-migrate使用教程](https://www.jianshu.com/p/5fd8c2cbad3b)
