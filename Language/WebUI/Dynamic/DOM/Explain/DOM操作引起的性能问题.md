---
title: DOM操作引起的性能问题
date: 2016-06-11
tags: [JavaScript]
categories: Dynamic
---

```javascript
        function loop() {
            var startT = +new Date();
            var a = document.querySelector("h3");
            for (var i = 0; i < 1000; i++) {
                a.innerText += i + ": \n";
            }
            var endT = + new Date();
            return endT - startT;   //8610
        }
```

上面是对DOM的操作，每次循环都需要对DOM元素访问俩次，一次读取`innerText`属性内容，另一次是写入。可以看到时间持续了8s多。

一个更有效率的版本是使用局部变量存储更新后的内容，然后一次性写入`DOM`；

```javascript
        function loop1() {
            var startT = +new Date();
            var a = document.querySelector("h3");
            var str = "";
            for (var i = 0; i < 1000; i++) {
                str += i + ": \n";
            }
            a.innerText += str;
            var endT = + new Date();
            return endT - startT;   //50；
        }
```

可以看出持续的时间只有50ms。

这些结果清楚地表明，你访问DOM越多，代码的执行速度就越慢。因此，一般经验法则是：轻轻地触摸 DOM，并尽量保持在 ECMAScript 范围内。

### `innerText/ innerHTML` 和 `DOM`的操作 更新页面内容

`innerText/ innerHTML`在老式浏览器中的性能会更好，
`DOM`在最新式浏览器中的性能会稍微好一些。

`element.cloneNode()` -- 

HTML集合是存储DOM节点引用的类数组对象。
除了常规的`document.getElementById`等这些集合外还有一些：如下：
- var b = document.images; -- 获取图片的集合
- var c = document.links; -- 获取链接的集合；

一般来说，对于任何类型的 DOM 访问，如果同一个 DOM 属性或方法被访问一次以上，最好使用一个局部变量缓存此DOM成员。当遍历一个集合时，第一个优化是将集合引用存储于局部变量，并在循环之外缓存 length属性。然后，如果在循环体中多次访问同一个集合元素，那么使用局部变量缓存它。

---

在下面的例子中，在循环中访问每个元素的三个属性。最慢的版本每次都要访问全局的 document，优化后的版本缓存了一个指向集合的引用，最快的版本将集合的当前元素存入局部变量。所有三个版本都缓存了集合的 length 属性。

```javascript
         // slow
        function collectionGlobal() {
            var len = coll.length,
                name = '';
            for (var count = 0; count < len; count++) {
                name = document.getElementsByTagName_r('div')[count].nodeName;
                name = document.getElementsByTagName_r('div')[count].nodeType;
                name = document.getElementsByTagName_r('div')[count].tagName;
            }
            return name;
        };
         // faster
        function collectionLocal() {
            var coll = document.getElementsByTagName_r('div'),
                len = coll.length,
                name = '';
            for (var count = 0; count < len; count++) {
                name = coll[count].nodeName;
                name = coll[count].nodeType;
                name = coll[count].tagName;
            }
            return name;
        };
         // fastest
        function collectionNodesLocal() {
            var coll = document.getElementsByTagName_r('div'),
                len = coll.length,
                name = '',
                el = null;
            for (var count = 0; count < len; count++) {
                el = coll[count];
                name = el.nodeName;
                name = el.nodeType;
                name = el.tagName;
            }
            return name;
        };
```

对于`HTML`集合操作尽可能的存储在局部变量中进行操作和变量，在`for`循环中，`length`属性单独存储。

对于遍历节点时候尽量使用`children`，而不是使用`childNodes`，因为会过滤掉无用的文本节点，性能一般会提升`1-3`倍。

如果可能的话，使用`CSS`选择器去替代`DOM`选择器，因为前者不会涉及到`HTML`集合，会快很多，

```html
    <img src="#" class="img" alt="01">
    <img src="#" class="img" alt="02">
    <img src="#" class="img" alt="03">
    <a class="link" href="#">link1</a>
    <a class="link" href="#">link2</a>
    <a class="link" href="#">link3</a>

    <script>
        var a = document.querySelectorAll(".img, .link");
        a;
        [<img src=​"#" class=​"img" alt=​"01">​, 
        <img src=​"#" class=​"img" alt=​"02">​, 
        <img src=​"#" class=​"img" alt=​"03">​, 
        <a class=​"link" href=​"#">​link1​</a>​, 
        <a class=​"link" href=​"#">​link2​</a>​, 
        <a class=​"link" href=​"#">​link3​</a>​];
    </script>
```

可以看到使用`CSS`选择器会是多么方便，