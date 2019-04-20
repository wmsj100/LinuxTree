---
title: 高效率批量修改DOM的三种方法
date: 2016-06-11
tags: [DOM]
categories: Dynamic
---

### 批量修改 DOM

当需要对`DOM`进行多次操作时候，可以通过以下方法减少重绘和重排版次数。
- 从文档流中摘除该元素，
- 进行多次`DOM`操作
- 把文档重新加入文档流
整个这个操作只需要重绘俩次，即第一步和最后一步。

有三种方法把`DOM`从文档流中摘除。
- 隐藏元素，进行修改，重新显示
- 使用一个代码片段在`DOM`树之外创建一个子树，然后将它拷贝到文档中。**推荐**
- 将原始元素拷贝到脱离文档的节点中，修改副本，然后覆盖原始节点。

[效果-jsbin](http://jsbin.com/zucopux/1/edit?html,js,output);

基础数据和要添加的`json`数据

```html
<ul id="mylist">
    <li><a href="http://phpied.com">Stoyan</a></li>
    <li><a href="http://julienlecomte.com">Julien</a></li>
</ul>

<script>
    var data = [{
        "name": "Nicholas",
        "url": "http://nczonline.net"
    }, {
        "name": "Ross",
        "url": "http://techfoolery.com"
    }];

    var mylist = document.querySelector("#mylist");
</script>
```

1. 方法1 -- 隐藏元素

```javascript
    function hideNode(node, data) {
        var wrap = node,
            json = data;
        wrap.style.display = "none";
        for (var i = 0, len = json.length; i < len; i++) {
            var li = document.createElement("li");
            var link = document.createElement("a");
            link.href = json[i]["url"];
            link.innerText = json[i]["name"];
            li.appendChild(link);
            wrap.appendChild(li);
        }
        wrap.style.display = "block";
    }
    hideNode(mylist, data);
```

对于这个过程需要改进的地方在于不要在循环内部创建`li`和`link`，放到循环外面。

```javascript
    function hideNode(node, data) {
        var wrap = node,
            json = data，
            li,
            link;
        wrap.style.display = "none";
        for (var i = 0, len = json.length; i < len; i++) {
            li = document.createElement("li");
            link = document.createElement("a");
            link.href = json[i]["url"];
            link.innerText = json[i]["name"];
            li.appendChild(link);
            wrap.appendChild(li);
        }
        wrap.style.display = "block";
    }
    hideNode(mylist, data);
```

2. 方法2 -- 代码片段 fragment

```javascript
    function fragWay(node, data) {
        var li,
            link;
        list = node,
        json = data,
        frag = document.createDocumentFragment();

        for (var i = 0, len = json.length; i < len; i++) {
            li = document.createElement("li");
            link = document.createElement("a");
            link.href = json[i]["url"];
            link.innerText = json[i]["name"];
            li.appendChild(link);
            frag.appendChild(li);
        }
        list.appendChild(frag);
    }

    fragWay(mylist, data);
```

3. 通过克隆 -- cloneNode(true);

```javascript
    function cloneNodeWay(node, data) {
        var i,
            link,
            json = data,
            cloneWrap = node.cloneNode(true);
        for (var i = 0, len = json.length; i < len; i++) {
            li = document.createElement("li");
            link = document.createElement("a");
            link.href = json[i]["url"];
            link.innerText = json[i]["name"];
            li.appendChild(link);
            cloneWrap.appendChild(li);
        }
        node.innerHTML = cloneWrap.innerHTML;
    }
    cloneNodeWay(mylist, data);
```

对于如何把`cloneWrap`的内容替换`node`的内容，我刚开始想到了要从父节点去下手，但是没考虑到`replace`这个属性，所以慢慢的就想到了`innerHTML`，然后就使用了`node.innerHTML = cloneWrap.innerHTML`；
说实话想到这一点我还是比较高兴的，因为我感觉我这个要比`道格拉斯`的方法好，因为不需要遍历父节点也省去了替换的过程，直接重置内容，简单省事。

**道格拉斯的方法***

```javascript
node.parentNode.replaceChild(cloneWrap, node);
```

> 推荐尽可能使用文档片断（第二种解决方案）因为它涉及最少数量的 DOM 操作和重排版;
