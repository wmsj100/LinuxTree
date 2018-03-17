---
title: link的伪类叠加结合伪类和访问记录
date: 2016-06-16
tags: [CSS]
categories: Static
---

对于`a`链接来说，可以使用伪类的叠加，如下；

```html
<style>
    a:link:hover{
        color: red;
    }
    a:visited:hover{
        color: yellow;
    }
</style>
<a href="http://www.erheizi.com">erheizi</a>
<a href="http://www.erheizi.com">e2rheizi</a>
```

上面的额代码访问区别了访问过的和未访问过得代码。

对于`a`链接，它区分是否访问是查看浏览器缓存的链接地址，即如果俩个链接的地址是相同的，那么他们的访问效果也是一样的。即便链接的文本显示不同。

它与顺序没有关系，`a:link:hover` => `a:hover:link`