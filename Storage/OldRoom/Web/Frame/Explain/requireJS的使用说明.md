---
title: requireJS的使用说明
date: 2016-07-11
tags: [Models]
categories: Frame
---

- 首先加载`requirejs`，加载的`script`如下：
`<script data-main="js/main" src="js/lib/require.min.js"></script>`

data-main加载的js脚本可以省略后缀。

- 通过`requirejs`加载的文件都默认为`js`文件，所以不需要加载`.js`后缀。
- 通常requirejs加载文件的目录都是通过`baseUrl + paths`来完成设置，如果满足下面条件之一，会跳过`baseUrl + paths`的配置。
    + 文件以`.js`结束
    + 以`/`开始
    + 包含完整`URL`协议，如`http, https`.
- 如下的配置，`baseUrl`是基于`main.js`文件被引用的地址。
- `paths`是基于`baseUrl`的路径。

```javascript
require.config({
    baseUrl: "js/lib",
    paths: {
        app: "../app"
    }
});
```

- 模块不同于传统的脚本文件，它良好的定义了一个作用域来避免全局名称空间污染，它可以显示的列出其依赖关系，并以函数参数的形式，将这些依赖进行注入，而无需引用全局变量，`requirejs`模块是模块模式的一个扩展，其好处是无需全局地引用其它模块。

- 如果只有


