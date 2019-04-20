---
title: Django渲染json到模板
date: 2018-04-14 11:05:12 Sat
modify: 2018-04-14 11:05:12 Sat
tag: [json]
categories: Django
author: wmsj100
mail: wmsj100@hotmail.com
---

## Django渲染json到模板
- ajax方式渲染页面，动态加载内容
- 直接在视图函数中渲染list和网页部分一起显示在网页上，这样页面内容会被转义，
- `from __future__ import unicode_literals` 在视图层要引用这个必须放置在第一行
- `<script src="/static/learn/js/test3.js" ascy></script>` 在一个app内部可以单独创建一个static静态文件夹，引用的时候就使用绝对路径
- 对于直接在页面内写入变量的传参，不能通过在页面引入js文件然后在js中编辑变量，这样的变量获取会报错，想到的方法是：
- 这个方法最核心的就是要引入json模块，然后调用json.dump方法转换变量值，
- 在页面引用变量的时候要通过safe过滤器来再次转换值
```py views.py
from __future__ import unicode_literals
import json
def test3(request):
    List1 = ['这是练习题', '渲染json']
    Dict1 = {'site': '完美生活', 'author': '王浩'}
    return render(request, 'learn/test/test3.html', {
        'List1': json.dumps(List1),
        'Dict1': json.dumps(Dict1),
    })
```

```html
<p id="test1">1</p>
<script>
    var List1 = {{ List1|safe }};
    var Dict1 = {{ Dict1|safe }};
    $("#test1").data("type", {"List1": List1, "Dict1": Dict1});
</script>
<script src="/static/learn/js/test3.js"></script>
```
```js test3.js
$(document).ready(function(){
    var data = $("#test1").data("type");
    console.log(data.Dict1);
});
```
- 简要概述就是现在页面获取到变量值，然后把获取的值写入到页面的一个隐藏元素的data属性上，然后通过js文件再去获取这个隐藏DOM携带的data属性值。
