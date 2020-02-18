---
title: html-webpack-plugin
date: 2020-02-18 23:31:57
modify: 
tags: [Plugin]
categories: Webpack
author: wmsj100
email: wmsj100@hotmail.com
---

# html-webpack-plugin

## 概要

- 自动生成html，对于单页面应用，现在很少需要自己手动写入html
- index.html只是一些引入的js或css文件，还有一些头部声明，可以从模板继承。
- 使用这个plugin可以保证html全部在src中。

## 配置

- title: 生成html的文件标题
- filename: 输出的html文件名
- template: 继承的模板
- inject: script的位置
- minify: 默认是否对html进行压缩
- hash: 是否给生成的js文件一个独特的hash值

## 范例
```webpack.config.js
const path = require('path')
//const { CheckerPlugin } = require('awesome-typescript-loader')
const {CleanWebpackPlugin} = require('clean-webpack-plugin')
const HtmlWebpackPlugin = require('html-webpack-plugin')

module.exports = {
	entry: './src/index.ts',
	output: {
		filename: 'bundle.js',
		path: path.resolve(__dirname, 'dist')
	},
	module: {
		rules: [
			{
				test: /\.tsx?$/,
//				use: 'awesome-typescript-loader',
				use: 'ts-loader',
				exclude: /node_modules/
			}
		]
	},
	plugins: [
		new CleanWebpackPlugin(),
//		new CheckerPlugin()
		new HtmlWebpackPlugin({
			title: 'wmsj100 typescript',
			minify: {
				removeComments: true,
				collapseWhitespace: true,
				minifyCSS: true
			},
			hash: true,
			filename: 'index.html',
//			template: './src/template.html'
		})
	],
	resolve: {
		extensions: ['.tsx', '.ts', '.js']
	}
}
```

## 参考

- [html-webpack-plugin讲解](https://www.jianshu.com/p/08a60756ffda)
