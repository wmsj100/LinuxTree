---
title: 动态加载图片image获取宽高问题
date: 2016-05-12
tags: [DOM,Ajax]
categories: Dynamic
---

通过javascript动态生成的图片，如何获取图片的宽高呢，尤其引用的是`SVG` 格式的图片，因为图片尺寸可以在`SVG` 中进行调整，但是因为`SVG` 图片是通过js动态引入的，而且宽度是必须设置的，因为会影响到`DOM` 的渲染速度，而且不能在`CSS` 中进行尺寸的限制，因为这样的话，在`SVG` 中更改尺寸就没有意义的，必须来个地方同时更改，这样出错率就太高了。

所以图片的尺寸必须通过js动态获取

```javascript
var image = document.createElement("img");
image.style.width = image.width + "px";
image.style.height = image.height + "px";
```

这样设置就可以了。

```html
<img src="../../img/model/svg/html5.svg" alt="HTML AND HTML5" class="carousel-img" style="width: 50px; height: 50px;">
```

