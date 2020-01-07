---
title: unittest
date: 2019-04-09 14:53:05	
modify: 
tag: [test]
categories: Python 
author: wmsj100
mail: wmsj100@hotmail.com
---

# unittest

## 概述
- 这是python的一个测试模块，是自带的标准库，
- 代码必须通过单元测试来执行进行验证代码的健壮性，
- 任何人都可能引入bug

## 使用
- 测试文件以"_test.py"结尾
- 测试类必须以"Test"开头
- `setUp` 每个测试函数在执行之前都会先执行这个方法
- `tearDown` 每个测试函数在执行完成后都会执行这个方法
- `setUpClass` 测试文件在执行之前先执行这个类
- `tearDownClass` 测试文件在执行完成后会执行这个类
- `assertEqual(a,b)` 判断俩个值相等
- `assertTrue(a==b)` 判断返回True
- `assertFalse(a==b)` 判断返回False
- `assertNotEqual(a,b)` 判断俩个值不等

## 参考
- [mock是什么](https://www.cnblogs.com/labc/articles/5012259.html)
