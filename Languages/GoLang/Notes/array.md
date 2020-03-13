---
title: array
date: 2020-03-13 21:58:03
modify: 
tags: [Notes]
categories: GoLang
author: wmsj100
email: wmsj100@hotmail.com
---

# array

## 概要

- go的数组和C类似,也是需要同类型固定长度,

## 使用

- `var list2 [5]int = [5]int{4, 5}` 这样声明一个数组,为赋值的位置默认为0
- 在数组的定义中,如果数组长度位置出现'...',则表示数组长度是根据初始化值的个数来计算的.
- `q := [...]int{1, 2, 3}`
- 数组的长度是数组类型的一个组成部分,数组的长度必须再编译阶段能确定.
- 俩个数组只要长度相等,值相等,就可以判断这俩个数组相等,
```go
a1 := [2]int{2, 3}
a2 := [...]int{2, 3}
fmt.Println(a1 == a2) // true
```
- 不能比较俩个类型不同的数组,否则编译报错
- `list1 := [...]string{"wmsj100", "wanghao", "male"}` 定义字符串数组,字符串必须用双引号包裹
- 遍历数组使用`range`方法,
```go
list1 := [...]string{"wmsj100", "wanghao", "male"}
for key,val := range list1 {
	fmt.Println(key,val)
}
// 0 wmsj100
// 1 wanghao
// 2 male
```
- 多维数组是被允许使用,适合用来管理父子关系或坐标系数据
```go
func fn_array_test3() {
	// 指定初始化
    list1 := [4][2]int{{10, 11}, {20, 21}, {30, 31}, {40, 41}}
	// 使用数组字面量来声明并初始化一个二维数组
    list2 := [4][2]int{1: {20, 21}, 3: {40, 41}}
	// 声明并初始化数组中指定的元素
    list3 := [4][2]int{1: {0: 20}, 3: {1: 41}}

    fmt.Println(list1, "/n")
    fmt.Println(list2, "/n")
    fmt.Println(list3, "/n")
}
Press ENTER or type command to continue
[[10 11] [20 21] [30 31] [40 41]] /n
[[0 0] [20 21] [0 0] [40 41]] /n
[[0 0] [20 0] [0 0] [0 41]] /n
```

## 参考

- [go 数组](http://c.biancheng.net/view/4117.html)
