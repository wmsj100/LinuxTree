---
title: mock
date: 2019-04-09 14:38:46	
modify: 
tag: [mock]
categories: Python 
author: wmsj100
mail: wmsj100@hotmail.com
---

# mock

## 概述
- 可以mock伪造数据，不用调用接口或者连接数据库
- python3.3之前的版本需要单独安装mock模块，
- python3.3之后的版本mock被集成在unittest模块中

## 使用
- panduanchengji_0409.connectDB = mock.Mock(return_value=[[1, 'alice', 23, 12], [2, 'wmsj100', 89, 99]])
- 设置函数的返回值为mock的值，这样调用函数时候就不会进入函数内部，直接使用mock的值

## 参考
- []()
