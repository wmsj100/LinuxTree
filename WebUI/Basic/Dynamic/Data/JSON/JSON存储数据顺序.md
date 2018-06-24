---
title: JSON存储数据顺序变化
date: 2016-05-24
tags: [JSON]
categories: Dynamic
---

`JSON`存储的数据可以存在在数组中，也可以存放在对象中；这俩者最大的区别就是存在在数组中的数据是严格按照存放顺序读取的，而存放在对象中的数据是默认按照键值对的键名称字母排序的顺序，所以读取的数据顺序和数据存放顺序很可能完全不一样，例如
```json
"src": {
        "git": "img/git.svg",
        "javascript": "img/javascript.svg",
        "less": "img/less.svg",
        "html5": "img/html5.svg"
        }
```
读取的数据顺序为
git : "img/git.svg" / html5 : "img/html5.svg" / javascript : "img/javascript.svg" / less : "img/less.svg"；
完全是乱序，就是按照字母排序的，这不是想要的结果，
所以把数据放置到对象中，然后用数组包裹就可以了。
```json
"src": [
        {"git": "img/git.svg"},
        {"javascript": "img/javascript.svg"},
        {"less": "img/less.svg"},
        {"html5": "img/html5.svg"}
    ]
```
读取数据的顺序为
src : Array[4]
0 : Object git : "img/git.svg"
1 : Object javascript : "img/javascript.svg"
2 : Object less : "img/less.svg"
3 : Object html5 : "img/html5.svg"
这样就是我想要的数据了，严格按照我的数据顺序
所以如果是有顺序要求，就把数据放置到数组中，感觉一般都是想按照传入顺序排列的，所以就放置到数组中吧