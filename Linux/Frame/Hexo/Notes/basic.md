---
title: basic
date: 2019-12-27 22:46:53 Friday
modify:
tag: [notes]
categories: Hexo
author: wmsj100
mail: wmsj100@hotmail.com
---

# basic

## 用法

- `npm install -g hexo-cli`
- `hexo init myweb`
- `hexo generate` 生成静态文件
- `hexo generate -w/--watch`  监视文件变动,实时重新渲染文件
- `hexo server -p 8080` 重设端口,默认是4000
- `hexo new --path about/me` "first diary"  在`source/_posts/about/me.md`
- `hexo new [layout] <title>` 创建文章,默认是按照`post`模板来创建目录,可以省略
- `hexo new page "page layout" hello` 按照page的布局来生成文件在目录"`source/hello.md`"
- `hexo new post "page post" hello` "source/_post/hello.md"
- `hexo new draft "page draft" hello` "source/_drafts/hello.md"
- `<!-- more -->` 这个标签前面的内容会被显示为摘要

## 标签

- `{% post_link hexo-4-released %}` 直接引用目标文件,不管文件在哪个目录下,默认显示文章标题
- `{% post_link hexo-4 '文章链接' %}` 自定义链接文字
- `{% post_link hexo-4 '<b>bold</b> title' %}` 默认会对文章进行转义
- `{% post_link hexo-4 '<b>bold</b> title' false %}` 禁止对标题进行转义
- `{% asset_img linux.jpg This is an example image %}` 这样可以在文章的资源文件夹中引用图片,通过相对路径,前提是在`_config.yml`中开启`post_asset_folder:true`,这样通过`hexo new`创建文章时候也会创建一个文章同名的目录,静态文件就可以放入该目录

## 参考
- [参考](https://hexo.io/zh-cn/docs/commands)
