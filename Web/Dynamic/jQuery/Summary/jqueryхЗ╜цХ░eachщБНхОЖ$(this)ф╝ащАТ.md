---
title: jquery函数each遍历$(this)传递
date: 2016-04-23
tags: [jQuery,遍历,this]
categories: Dynamic
---

在`jQuery`的`each`函数进行遍历的时候，有时候想把遍历的对象下标传递出去，到另一个函数进行处理，但如果此时直接把当前对象`$(this)`通过函数`dealData($(this))`这样传递过去，然后在函数`dealData($(this))`中引用的时候，就会出问题。因为函数中的`$(this)`指代的是`dealData()`本身，所以有俩中方法可以实现把`$(this)`传递出去，

1. 在`each`函数内部，把`$this()`赋值给一个变量`current`，然后通过变量来使用，并且给函数传递的参数也是变量形式`dealData(current)`，然后函数内部使用的时候就比较随意了。`function dealData(cur){ }`这样也是可以的。
2. 不需要把当前变量`$(this)`赋值给变量，而是直接传递给函数`dealData($(this))`，但是在函数内部必须要使用变量`function dealData(cur){ }`，这样也可以把`each` 中的`$(this)`传递到函数内部；
3. 如果是这样`dealData($(this))`，然后这样调用函数`function dealData($(this)){ }`这样就会报错了，因为此时`$(this)`指代的是函数`dealData`本身。

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<title>01</title>
<meta name="description" content="">
<meta name="keywords" content="">
<link href="" rel="stylesheet">
<script src="http://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js"></script>
</head>
<body>
    <div>hello 1</div>
    <div>hello 2</div>
    <div>hello 3</div>
    <div>hello 4</div>
    <div>hello 5</div>
    <div>hello 6</div>
    <div>hello 7</div>
    <div>hello 8</div>
    <div class="stop">hello 9</div>
    <div>hello 10</div>
    <div>hello 11</div>
    <div>hello 12</div>
    <div>hello 13</div>
    <div>hello 14</div>
    <div>hello 15</div>
    <div>hello 16</div>
    <div>hello 17</div>
    <div>hello 18</div>
    <div>hello 19</div>
    <div>hello 20</div>
</body>
</html>
```

方法1: 直接使用`$(this)`

```javascript
<script>
$("div").each(function(index) {
	// var current = $(this);
	if ($(this).attr("class") === "stop") {
		return false;
	} else {
		dealData($(this));
	}
});

function dealData(cur) {
	console.log(cur.text());
	cur.css({
		"color": "blue"
	});
}
    </script>
```

方法2: 把`$(this)`赋值给变量`current`

```javascript
    <script>
$("div").each(function(index) {
	var current = $(this);
	if (current.attr("class") === "stop") {
		return false;
	} else {
		dealData(current);
	}
});

function dealData(cur) {
	console.log(cur.text());
	cur.css({
		"color": "blue"
	});
}
    </script>
```

