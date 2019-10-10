---
title: jQuery-ajax-视频解析
date: 2016-4-11 00:02:11
tags: [jQuery,Ajax]
categories: Dynamic
---

- empty--把一个元素内部清空，但是元素本身还是存在

- remove--把一个元素清除，包括元素自己。

- addClass / removeClass / toggleClass--切换添加移除class

- toggleClass--可以在class的添加和移除中进行切换

  ```css
  h1{
  		border: solid 1px #999;
  	}
  	.pop{
  		background-color: #E64E4E;
  		color: #fff;
  		font-weight: bold;
  	}
  ```

  ```html
   <h1>wmsj100</h1>
  ```

  ```javascript
  $(".btn").on("click",function(){
      	$("h1").toggleClass("pop");
      })
  ```

  ​

- $("p").css("background-color");-获取背景色

- $("p").css("background-color","yellow");设置背景色为黄色；

  ```javascript
  $('p').css({
  	"background-color":"yellow",
  	"font-size":"200%"
  }); 
  ```

- jquery里面都是函数

- `$(".wrap").children()`可以获取到所有子元素；

- each--可以用来遍历对象。

  ```html
  < div class = "wrap" >
  	< h1 > wmsj100 < /h1>
      <h3>hello kety;</h3 >
  	< div class = "div1" > hello world < /div>
      <button class="btn">click</button >
  	< /div>
      <script>
          $(".wrap").children().each(function() {
      	console.log($(this));
      	if ($(this).text() === "wmsj100") {
      		$(this).addClass("pop");
      	}
      })
   //如果元素的内容是“wmsj100”就给添加class“pop“；
  ```

- find--用于在找到的元素中进行查找内容

  `$(".wrap").find("h3")`

  `$("h3").parents(".wrap").find(".div1").addClass("pop")`

  上面这个是先找到父元素，然后通过`find()`方法来找到兄弟元素；

  ```
  $(".wrap").on("click","h3",function(){
      	$(this).parents(".wrap").find(".div1").addClass("pop");
      })
  //通过时间代理的方式绑定函数，
  ```

  ​

- `<h1>wmsj100</h1>`和`<h1> wmsj100 </h1>`是不一样的。

  ```
  <h1>wmsj100</h1>
  $("h1").text()==="wmsj100";
  <h1> wmsj100 </h1>
  $("h1").text()===" wmsj100 ";
  ```

  所以注意这个空格；

- each--可以用于遍历对象，而且在遍历的过程中还可以传入参数，获得当前遍历元素的`index`和`$(this)`

  ```
  $(".wrap").children().each(function(idx,el){
    console.log(idx+":"+$(el).text());
  })
  ```

- `$.each()`或者`jQuery.each()`

  `$ === jQuery`，他俩都是指向一个函数；

  ```javascript
  $ / jQuery
  function(a,b){return new n.fn.init(a,b)}
  ```

  $.("h1")---这是绑定到函数上面的静态属性，因为函数也是对象，所以也可以绑定对象。

  `$.each(function(key,val))`--可以用于遍历对象、数字，是一个通用的迭代函数，它可以用来无缝迭代对象和数组。数组和类似数组的对象通过一个长度属性（如一个函数的参数对象）来迭代数字索引，从0到length - 1。其他对象通过其属性名进行迭代。

  ```javascript
   var arr={"name":"wmsj","age":28};
      $.each(arr,function(key,value){
      	console.log(key+":"+value);
      })
      //name:wmsj
      //age: 28
  ```

  ```javascript
   var arr=["a","b","c","d"];
      $.each(arr,function(key,value){
      	console.log(key+":"+value);
      })
  //0:a
  //1:b
  //2: c
  //3: d
  ```

- `:checked` 选择器适用于复选框和单选框。对于下拉框元素, 使用 `:selected` 选择器。

- `$(':checkbox')` 等同于 `$('[type=checkbox]')`。如同其他伪类选择器（那些以“:”开始）建议前面加上一个标记名称或其他选择器;否则，默认使用通用选择("*")。换句话说`$(':checkbox')` 等同于 `$('*:checkbox')`，所以应该使用`$('input:checkbox')`来提升效率。

- .map---如果想处理一个简单的数字或对象，可以使用这个。由于返回值是一个jQuery包裹的数组，所以通过会使用`get()`方法将其转换为普通的数组，.map()方法特别适合于获取或设置元素集合中的值，

  ```javascript
  $(":checkbox").map(function(){
    return this.id;
  }).get().join();
  ```

  ​