---
title: 关于使用CSS选择器替代JS的DOM接口选择
date: 2016-06-11
tags: [DOM]
categories: Dynamic
---

在创建DOM节点之后对于DOM的选择，可以借用`CSS`的选择器，这个不涉及到`HTML`集合的操作，所以性能更好，而且选择更加灵活。代码也更简洁。

```javascript
    function createDom() {
        var frag = document.createDocumentFragment();
        var imgLen = 0;
        while (imgLen < 3) {
            var img = document.createElement("img");
            img.className = "img";
            img.alt = imgLen;
            img.src = "#";
            frag.appendChild(img);
            imgLen++;
        }
        var linkLen = 0;
        while (linkLen < 3) {
            var link = document.createElement("a");
            link.href = "javascript:void(0)";
            link.className = "link";
            link.innerText = "linkLen";
            frag.appendChild(link);
            linkLen++;
        }
        document.body.appendChild(frag);
        createDom.select = document.querySelectorAll(".img, .link");
    }
```

这个的唯一缺陷是因为要通过`CSS`选择器去选择，所以必须先要把`node`节点添加到`DOM`树中然后再去确定选择。

而且通过`querySelectorAll`一次性可以选择多个条件，很是方便。
如果浏览器支持 document.querySelectorAll()，那么最好使用它。
