---
title: 关于php文件中的对象写法
date: 2016-07-08
tags: [Ajax,PHP]
categories: Dynamic
---

当通过`ajax`获取后台动态页面`php`的数据时候，`php`中的对象要如何写呢，
如果直接写成`JS`格式的对象是无法通过`ajax`接收到的。
必须写成`json`格式的才可以返回,并且这个对象要使用引号包裹

```php
<?php
$name = $_GET["name"];  // $_REQUEST["name"]
$cont = $_GET["cont"];  // $_REQUEST["cont"]
$info = '{
    "name": "wmsj",
    "age": 10,
    "comment": "hello world"
}';
echo $info;
```

关于`php`是不需要写结束符。