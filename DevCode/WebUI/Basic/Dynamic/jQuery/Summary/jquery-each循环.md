---
title: jquery each循环
date: 2016-04-22
tags: [jQuery,遍历]
categories: Dynamic
---

`.each()`方法用来让dom循环结构更加简单更不易出错。它会迭代jQuery对象中的每一个dom元素。每次回调函数执行时，会传递当前循环次数作为参数（从0开始计数）。更重要的是，回调函数是在当前DOM元素为上下文的语境中触发的。因此关键字 `this` 总是指向这个元素。

```html
<div class="ct">hello 1</div>
<div class="ct">hello 2</div>
<div class="ct">hello 3</div>
<div class="ct">hello 4</div>
<div class="ct">hello 5</div>
<div class="ct">hello 6</div>
<div class="ct">hello 7</div>
<div class="ct">hello 8</div>
<div class="ct">hello 9</div>
<div class="ct stop">hello 10</div>
<div class="ct">hello 11</div>
<div class="ct">hello 12</div>
<div class="ct">hello 13</div>
<div class="ct">hello 14</div>
<div class="ct">hello 15</div>
<div class="ct">hello 16</div>
<div class="ct">hello 17</div>
<div class="ct">hello 18</div>
<div class="ct">hello 19</div>
<div class="ct" style="color: blue">hello 20</div>
```

```javascript
$("div").each(function(index){
    console.log(index+":"+$(this).text())
    }
```

```javascript
$("div").each(function(index){
  if(this.style.color !== "blue"){
	this.style.color = "blue";
}else{
	this.style.color = "";
}
}
```

通过再each循环中返回`return false`来停止each循环遍历
```javascript
$("div").each(function(index){
  $(this).addClass("blue");
    	if($(this).is(".stop")){
    		$("div").last().text(index);
    		return false;
    	}
}
```

