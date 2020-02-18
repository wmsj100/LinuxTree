---
title: webpack
date: 2020-02-18 20:16:56
modify: 
tags: [Notes]
categories: TypeScript
author: wmsj100
email: wmsj100@hotmail.com
---

# webpack

## 概要

- 运行ts的webpack的配置

## 配置

- tsconfig

```tsconfig.json
{
  "compilerOptions": {
    "target": "es5", 
    "module": "ESNext",
    "lib": ["es2015", "dom"],
    "allowJs": true,        
    "strict": true,    
    "moduleResolution": "node"

  }
}
```

- webpack.config.js
```webpack.config.js
const path = require('path')
//const { CheckerPlugin } = require('awesome-typescript-loader')
const {CleanWebpackPlugin} = require('clean-webpack-plugin')

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
	],
	resolve: {
		extensions: ['.tsx', '.ts', '.js']
	}
}
```

- package.json
```package.json
{
  "name": "study2",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "build": "webpack --mode development",
    "prod": "webpack --mode production",
    "watch": "webpack --watch"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "awesome-typescript-loader": "^5.2.1",
    "clean-webpack-plugin": "^3.0.0",
    "ts-loader": "^6.2.1",
    "typescript": "^3.7.5",
    "webpack": "^4.41.6",
    "webpack-cli": "^3.3.11"
  }
}
```

## 参考

- [ts webpack配置](https://www.jianshu.com/p/f6917e257b7a)
