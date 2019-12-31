---
title: 数据文件
date: 2019-12-31 08:43:20 Tuesday
modify:
tag: [notes]
categories: Hexo
author: wmsj100
mail: wmsj100@hotmail.com
---

# 数据文件

## 概述

- 数据文件其实就是可以复用的数据存储在一个文件中,通过模板来调用渲染
- 就像公共文件,提高复用性

## 用法

- 数据文件和当前使用的主题强相关,因为模板文件需要在主题的`layout`中写入
- 会载入`Hexo`的更目录下的`source/_data`内的`YAML/JSON`文件,如此便可以在网站中复用这些文件了.

## 范例

- `mkdir -p source/_data` 创建数据文件,在hexo的根目录下执行
- `vi source/_data/menu.yml`
	```yml
	Home: /
	Gallery: /gallery/
	Archives: /archives/
	```
- `cd themes/landscape/layout/_widget/` 进入主题目录创建模板
- `vi menu.ejs`
	```ejs
	<% if (site.data.menu) { %> #判断该文件内容是否为空,如果为空就不渲染插件
		<div class="widget tag">
			<h3 class="title">友情链接</h3>
			<ul class="entry">
				<% for (var i in site.data.menu){%>
				<li class="link"><a href="<%- site.data.menu[i] %>"><%= i %></a></li>
				<% } %>
			</ul>
		</div>
	<% } %>
	```
- `vi /home/pi/Documents/myweb/themes/landscape/_config.yml` 修改主题的配置文件,在`widgets`列表中添加渲染插件menu
- `hexo clean;hexo g`重新渲染页面就可以查看到新生成的页面有目标插件

## 参考

- [Hexo数据文件](https://hexo.io/zh-cn/docs/data-files)
- [Hexo数据文件功能添加友情链接](https://www.jianshu.com/p/43eb0819f51a)
