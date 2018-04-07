---
title: JS脚本加载方式
date: 2016-06-11
tags: [JavaScript]
categories: Dynamic
---

JS脚本的加载方式，如下：

```html
<script>
    console.log("hello world");
</script>
```

JS外联脚本，如下：

```html
<script src="1.js"></script>
```

动态加载脚本，这种多用于立即执行脚本，如下

```html
<script>
    var script = document.createElement("script");
    script.src = "01.js";
    document.head.appendChild(script);
</script>
```

使用`ajax`动态创建脚本，这种多用于需要检测脚本是否执行完毕。

```html
<script>
    var xhr = new XMLHttpRequest();
    url = "01.js",
    me = this;
    xhr.open("get", url, true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            if (xhr.status >= 200 && xhr.status < 300 || xhr.status === 304) {
                var script = document.createElement("script");
               script.innerText = xhr.responseText;
               document.head.appendChild(script);
            }
        }
    }
    xhr.send();
</script>
```

此代码向服务器发送一个获取file1.js文件的GET请求。onreadystatechange事件处理函数检查 readyState是不是 4，然后检查 HTTP状态码是不是有效（2XX表示有效的回应，304 表示一个缓存响应）。如果收到了一个有效的响应，那么就创建一个新的<script>元素将它的文本属性设置为从服务器接收到的responseText字符串这样做实际上会创建一个带有内联代码的<script>元素。一旦新<script>元素被添加到文档，代码将被执行并准备使用。
这种方法的主要优点是，你可以下载不立即执行的 JavaScript 代码。由于代码返回在<script>标签之外（换
句话说不受<script>标签约束），它下载后不会自动执行，这使得你可以推迟执行，直到一切都准备好了。
另一个优点是，同样的代码在所有现代浏览器中都不会引发异常。
此方法最主要的限制是：JavaScript 文件必须与页面放置在同一个域内.

有几种方法可以使用非阻塞方式下载 JavaScript：
——为<script>标签添加 defer 属性（只适用于 Internet Explorer 和 Firefox 3.5 以上版本）
——动态创建<script>元素，用它下载并执行代码
——用 XHR 对象下载代码，并注入到页面中
