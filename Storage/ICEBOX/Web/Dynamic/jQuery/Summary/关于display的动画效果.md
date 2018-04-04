---
title: 关于display的动画效果
date: 2016-09-06
tags: [jQuery,Summary]
categories: Dynamic
---

说到动画首先就会想到`animate`,然后就会写出下面这样的代码：

```js
$layer9.animate({"display": "block"},300);
$layer9.animate({"display": "none"},300);
```

然后会去测试，发现为什么完全没有反应，然后就会想到，`animate`只是对`css`样式有动画效果，对于其它的属性是没有作用的，即便是颜色的渐变也是需要使用`jQuery`的`color`插件来实现这个效果。

然后就会回到最开始的`show`和`hide`,忽然意识到这俩个方法是可以添加--延时的，然后就会想到还有类似显示隐藏的方法`fadeIn, fadeOut`,这下就豁然开朗了，可以使用自己想要的方法了，而我这次选择的是`

```js
$layer9.fadeIn(500);	
$(this).fadeOut(500);
```
