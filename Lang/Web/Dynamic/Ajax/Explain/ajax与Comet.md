---
title: ajax与Comet
date: 2016-06-28
tags: [Ajax,JavaScript,DOM]
categories: Dynamic
---

- 2005年被以网志形式发布
- 微软最早以`XMLHttpRequest`简称`XML`实现.
- 它与数据格式无关.
- 这种技术就是无须刷新页面就可以从服务器获取数据的方法.

```javascript
    var xhr = new XMLHttpRequest();
    var url = "01.php";
    xhr.open("get",url,false);
    xhr.send(null);
```

先创建一个`xhr`实例,
然后通过`open`发起ajax请求,接收3个参数,
- get 和服务器的通信方法,使用`get`, `post`;
- url -- 服务器的地址,必须是同域名内部
- false -- 表示同步,服务器数据会阻塞页面的加载,如果为true,表示异步.

- 完成请求之后,xhr的属性值会被填充
- `xhr.responseText` -- 作为响应主体被返回文本;    //"hello"
- `xhr.status` -- 响应的HTTP状态码;   //200
- `xhr.statusText` -- 响应的状态说明   // "ok"

- `xhr.onreadystatechange`方法为了兼容性,必须在xhr.open之前调用.
- `xhr.setRequestHeader()` -- 可以设置自定义头部,必须在`xhr.open`和`xhr.send`之间调用.

- `xhr.getResponseHeader(name)` -- 获取响应头部为`name`的值
- `xhr.getAllResponseHeader()` -- 获取所以的响应头部的长字符串

查询字符串的名值对都必须使用 -- encodeURIComponent -- 进行编码,然后才可以放到url末尾

- 忽然明白了，其实提交表单时候我可以不使用`form`表单自带的`submit`提交功能，因为那个功能就是会自动跳转页面，而是自定义一个按钮，只不过起名为`submit`，点击时候触发的是`ajax`。这就没问题了。
- 而且这样做的时候，对于防止重复提交的按钮禁用就很方便了。不需要使用那个hack味道十足的内嵌`iframe`方法。

- `formData` -- 我觉得这个应该是很好用的，因为它的功能和我自己的方法是一样的，但唯一的问题是，我该怎么解析那一大串数据，获取我想到的数据。

- `CORS`是`W3C`的方案，通过在被访问的页面动态添加头部来实现，所以被访问的页面不能是静态页面，下面是通过`php`添加的动态头部

```php
<?php
header("Access-Control-Allow-Origin:http://a.com");
$info = '{"name": "wmsj", "age": 10}';
echo $info;
```

- 跨域手段中凡是通过内嵌`iframe`的方法，只能访问静态页面，因为即便传入的是脚本，`iframe`会自动构建为html静态页面
