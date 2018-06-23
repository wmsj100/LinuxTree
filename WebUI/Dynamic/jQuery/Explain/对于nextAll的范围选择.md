---
title: 对于nextAll的范围选择
date: 2016-07-07
tags: [jQuery]
categories: Dynamic
---

我对这个选择器完全没有印象，昨天就碰到这个场景了，我需要选中目标元素后面的所有同辈元素，但是我没办法，不知道该怎么做。
刚刚看到了这个选择器才发现真的很好用。

```html
    <div>
        <p>hello world</p>
        <spna>hello world</spna>
        <p>hello world</p>
        <div>hello world</div>
        <p>hello world</p>
    </div>

    <script>
        $("div:first :first-child"); // 选中第一个div的第一个子元素
        $("div:first :first-child").nextAll("p");
        // 选中第一个子元素后面的所有同辈的段落元素p，
        $("div:first :first-child").nextAll();
        // 选中第一个子元素后面的所有同辈元素。
    </script>
```

