---
title: 关键字
date: 2020-03-13 19:14:33
modify: 
tags: [Notes]
categories: GoLang
author: wmsj100
email: wmsj100@hotmail.com
---

# 关键字

## 概要

- Go语言的词法元素包括5种,
	- 标识符 (identifier)
	- 关键字 (keyword)
	- 操作符 (operator)
	- 分隔符 (delimiter)
	- 字面量 (literal)

## 关键字

- `break/case/chan/const/continue/default/defer/else/fallthrouth/for/func/go/goto/if/import/interface/map/package/range/return/select/struct/switch/type/var`

## 标识符

- 自己可以定义的变量都是标识符
- `_`是一个特殊标识符,称为空白标识符,可以像其他标识符那样用于变量的声明和赋值,但任何赋值操作的值都会被抛弃,
- 变量使用驼峰命名法,首字母如果大写,表示可以被其它包访问,类似public,如果首字母小写,则表示只能再本包中使用.

## 预定以标识符

- `append/bool/byte/cap/close/complex/complex64/complex128/uint16/uint32/uint64/uint/uint8/uintprt/copy/false/float32/float64/imag/int/int8/int16/int32/int64/iota/len/make/nil/panic/print/println/real/recover/string/true`

## 参考

