---
title: route
date: 2020-02-09 17:38:35
modify: 
tags: [Notes]
categories: Flask
author: wmsj100
email: wmsj100@hotmail.com
---

# route

## 概要

- `@app.route('/')` 使用`route`装饰器来把函数绑定到URL

## 使用

- `<converter:variable_name>` 可以在url中添加变量
- `converter`： 转换器，有一下几种类型
	- `string`: 接受不包含斜杠的文本
	- `int`: 接受正整数
	- `float`: 接受正浮点数
	- `path`: 类似string，但是接受斜杠
	- `uuid`: 接受UUID字符串

## url_for

- 用于构建指定函数的URL
- 它把函数作为第一个参数，可以接受任意个关键字参数，每个关键字参数都对应URL中的变量。
- 为什么不把URL写死在模板中，而要使用反转函数`url_for`动态构建
	- 反转通常比硬编码URL的描述性更好。
	- 你可以在在一个地方改变URL，而不用到处乱找
	- URL创建会为你处理特殊字符和转义和Unicode数据，比较zhiguan
	- 生产环境的路径总是绝对路径，可以避免相对路径产生副作用
	- 如果应用是放在URL跟路径之外的地方，url_for可以妥善处理

## method类型选择

- 一个url可以有不同的访问方式
- 通常一个接口可以使用`GET`来获取数据，`POST`更新数据
- `@app.route('/method', methods=['GET', 'POST'])` 这样指定不同的方式访问接口的处理方式
- 之前在那个项目中，`django`就是因为更新和查询需要使用不同接口让我吐槽来很久，所以就不打算深入学习了
- 测试下面这个可以通过火狐浏览器的接口编辑重发来实现。
```python
@app.route('/method', methods=['GET', 'POST'])
def method_fn():
    if request.method == 'POST':
        return 'This is a POST request'
    elif request.method == 'GET':
        return 'This is a GET request'
```

## 参考

- [flask快速上手](https://dormousehole.readthedocs.io/en/latest/quickstart.html)
