---
title: 表单
date: 2018-07-10 23:01:56	
modify: 
tag: [form]
categories: Angular
author: wmsj100
mail: wmsj100@hotmail.com
---

# 表单

## 概述
- `FormControl` 封装了表单中的输入,并提供了一些可供操作的对象
- `validator` 以任何方式验证表单输入
- `observer` 能够监听表单的变化,并作出相应的回应.

## `FormControl`
- 代表单一的输入字段,他是`Angular`表单中的最小单元
- 封装了这些字段的值和状态,比如是否有效/是否脏(被修改过)或是否有错等

## `FormGroup`
- 大多数表单都拥有不止一个字段,因此需要某种方式来管理多个`FormControl`
- `FormGroup`为一组`FormControl`提供总包接口

## 实用
- 要使用上面提到的俩个模块,必须先导入下面这俩个模块
- `FormsModule` 可以使用例如`ngModel`, 'NgForm'
- `ReactiveFormsModule` 可以使用如 `formControl`, `ngFomrGroup`

## 参考
- []()
