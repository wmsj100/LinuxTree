---
title: label input
date: 2016-4-7 10:28:42
tags: [html]
categories: Static
---

`label`绑定`input`时候，不用每次都给`input`添加`id`，因为毕竟`id`还是少用为妙，所以只要用`label`把`input`包裹起来也是同样的效果。

```html
<label >用户名：
    <input type="text" class="username" placeholder = "用户名(hunger被注册过)">
</label>
```

