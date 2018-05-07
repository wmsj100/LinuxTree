---
title: basic
date: 2018-05-07 22:57:23 Mon
modify: 2018-05-07 22:57:23 Mon
tag: [webpack]
categories: WEB
author: wmsj100
mail: wmsj100@hotmail.com
---

# Webpack基础

## 概述
- Webpack可以将多种静态资源js, css, less转换成一个静态文件，减少了页面的请求。

## 安装
- 依赖node
- npm install webpack -g
- 它依赖cli模块打包文件
- cnpm install webpack-cli -g
- webpack t1.js t.js 会进行打包，文件打包到dist/main.js
- webpack本身只能处理js模块，如果要处理其他类型的文件，需要使用`loader`进行转换
- 如果需要在应用中添加css文件，就需要使用css-loader和style-loader
	- css-loader 遍历css文件，找到url()表达式然后处理他们
	- style-loader 把原来css代码插入到页面的一个style标签
- cnpm install css-loader style-loader	

