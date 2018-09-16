---
title: 从元素中删除某个class正则教程
date: 2016-05-07
tags: [数组,函数,封装,DOM,正则]
categories: Dynamic
---

想要从一个元素中删除一个classname，能想到的基本就是通过操作元素的`node.className` 来实现，当然了让字符串成为数组的方式除了`split` 还有正则的`match` ，下面就是这俩种思路

```html
<div class=" qwe  w1   e">world</div>
```

```javascript
   function bulletCheck() {
      var array = ct.bullet.childNodes;
      for (var i = 0, len = array.length; i < len; i++) {
         array[i].classList.remove("carousel-btnActive");
      }
      array[ct.start].classList.add("carousel-btnActive");
   }
```

1. 通过`match` 的实现--完美

   ```javascript
   var a = document.querySelector("div");

   function removeClass(node, className) {
   	var classArray = node.className.match(/\S+/g);
   	var num = classArray.indexOf(className);
   	if (num > -1) {
   		classArray.splice(num, 1);
   		node.className = classArray.join(" ");
   	}
   	return node.className;
   }
   var b = removeClass(a, "e");	//"qwe w1"
   ```

2. 通过`split` 的实现--不完美

   ```javascript
   var a = document.querySelector("div");

   function removeClass(node, className) {
   	var classArray = node.className.split(/\s+/g);
   	var num = classArray.indexOf(className);
   	if (num > -1) {
   		classArray.splice(num, 1);
   		node.className = classArray.join(" ");
   	}
   	return node.className;
   }
   var b = removeClass(a, "e");	//" qwe w1" 前面多了个空格
   ```

3. HTML5新增的API--`classList` ,可以获取`node.className` 的数组形式，而且只需要一句话就可以做到上面的事情,但是兼容性不好，只有火狐和谷歌支持，IE9不支持；

   ```javascript
   var a = document.querySelector("div");
   a.classList.remove("e");	
   a.classList	//DOMTokenList [ "qwe", "w1" ]
   ```

   ​

4. 通过正则的方式，最高级，最简洁，最优雅。。。--错误，不能匹配中间的属性

   ```javascript
   var a = document.querySelector("div");
   function removeClass(node, className) {
   	var regexp = new RegExp(".*[^\\b" + className + "\\b]", "g");	//反斜杠需要转义
     //这个正则写的是有问题的；
   	node.className = String(node.className.match(regexp)).match(/\S+/g).join(" ");
   	return node.className;
   }
   var b = removeClass(a, "e");	//"qwe w1"
   ```

   思考过程：

   1. 直接效果测试

      ```javascript
      var a = document.querySelector("div").className;
      a = a.match(/.*[^\be\b]/g).toString().match(/\S+/g).join(" ");
      ```

   2. 把正则转换为构造函数，传入变量

      ```javascript
      var a = document.querySelector("div").className;
      var regexp = new RegExp(".*[^\\b"+className+"\\b]","g");
      a = a.match(regexp).toString().match(/\S+/g).join(" ");
      ```

   3. 用函数封装，

      ```javascript
      var a = document.querySelector("div");
      function removeClass(node,className){
      var regexp = new RegExp(".*[^\\b"+className+"\\b]","g");
      	node.className = node.className.match(regexp).toString().match(/\S+/g).join(" ");
      	return node.className;
      }
      ```

   4. 用`String` 替换`toString` 使代码缩减；

      ```javascript
      var a = document.querySelector("div");
      function removeClass(node,className){
      var regexp = new RegExp(".*[^\\b"+className+"\\b]","g");
      	node.className = String(node.className.match(regexp)).match(/\S+/g).join(" ");
      	return node.className;
      }
      ```

      ​