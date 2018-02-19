---
title: jQuery中的事件和动画
date: 2016-07-04
tags: [jQuery]
categories: Dynamic
---

`$(document).ready(function(){})` 表示`DOM`树加载完成就会执行，而使用`window.onload = function(){}` -- 表示页面的所有资源加载完成才会执行。所以速度会快很都的。
`jQuery`也有一个`load`方法，表示元素加载完成之后触发，如果绑定到`window`上就和`window.onlaod`是一样的。
`$(window).load(function(){})`/.

`$(document).ready(function(){})` =>
`$().ready(function(){})` =>
`$(function(){})`

- 当文档转载完成后，如果想要对特定的元素绑定事件可以使用`bind`。
- bind方法有3个参数。事件类型、可选参数、事件处理函数
- 事件类型 -- `blur, focus, load, resize, scroll, unload, click, dblclick, mousedown, mouseup, mousemove, mouseover, mouseout, mouseenter, mouseleave, change, select, submit, keydown, keypress, keyup,. error`
- 可选参数 -- 作为`event.data`属性值传递给事件对象

```javascript
$(function(){
            $("p").bind("click",function(){
                $(this).next().show();  // 点击显示下一个元素
            });
        })
```

- 下面的代码是通过点击开显示和隐藏下一个元素

```javascript
$(function(){
            $("p").bind("click",function(){
                var $current = $(this).next();
                if($current.is(":visible")){    // 通过is来判断是否显示
                    $current.hide();
                }else{
                    $current.show();
                }
            });
        })
```

改变事件为`mouseover, mouseout`

```javascript
    $(function(){
            $("p").bind("mouseover",function(){
                $(this).next().show();
            }).bind("mouseout",function(){
                $(this).next().hide();
            })
        });
    <!-- 简化代码，使用简写版 -->
        $(function() {
        $("p").mouseover(function() {
            $(this).next().show();
        }).mouseout(function() {
            $(this).next().hide();
        })
    });
```

- 合成事件 `hover, toggle`

- `hover` -- 可以模拟光标鼠标悬停事件，`hover(enter,leave)` 接受俩个参数，分别表示鼠标进入和离开的动作。上面的代码改写之后如下

```javascript
    $(function() {
        $("p").hover(function() {
            $(this).next().show();
        }, function() {
            $(this).next().hide();
        });
    })
```

增加了一个效果

```javascript
    $("p").hover(function(){
        $(this).next().toggle();
        $(this).toggleClass("light");
    },function(){
        $(this).next().toggle();
        $(this).toggleClass("light");
    });
```

---

`function(event){}` -- 只需要为函数传入参数，就可以使用事件对象


```html
<p>
    <a href="#">hello</a>
</p>
<script>
     $("p").on("click",function(){
        console.log("para");
    }).find("a").on("click",function(){
        console.log("link");
        return false;
    })
</script>
```

上面这个例子通过给`a`链接返回`return false`来禁用默认事件和事件冒泡，所以点击之后只会打印出`link`.

`e.type` -- 返回事件的类型

`jQuery` -- 版本选择 -- `1.9`

`e.target` -- 获取目标元素

- `pageX / pageY` -- 获取鼠标相对于页面的座标。`jQuery`没有`clientX`，它封装到了`pageX`中，

- `e.which` -- 获取按钮的值。`1. 左键， 2，中键， 3.右键`

- `one` -- 表示绑定的事件只会被执行一次，然后就解除了。

- `trigger` -- 模拟用户操作 -- `$("#btn").trigger("click")` -- 模拟点击事件

- `自定义事件` -- 常见的事件也就是鼠标事件和键盘事件，还有一些表格事件`focue, submit, blur..` ,但是还可以有自定义事件，只不过自定义事件的触发条件比较特殊，只能通过`trigger`来触发，

```javascript
$("button").on("myclick", function() {  // 创建自定义事件`myclick`
        console.log("hello");
    });
    $("button").trigger("myclick"); // 通过模拟操作来触发这个事件
```

- 通过事件绑定的函数，第一个参数永远都是传递事件`event`，之后就可以传递自定义参数，如下

```javascript
    $("button").on("myclick", function(event,a) {
        console.log("hello " + a);
    });
    $("button").trigger("myclick",["wmsj"]);    // hello wmsj
```

`trigger` -- 在触发元素的事件时候会触发浏览器的默认行为，比如`focus`事件，在触发时候，文本框也会得到焦点。但是使用`triggerHandler`就不会触发浏览器的默认行为。

```javascript
    $("input").focus(function(){
        console.log("focus");
    });
    $("input").triggerHandler("focus"); // 文本框不会获得焦点
```

- 一次可以绑定多个事件，通过空格分割。下面的代码会通过鼠标划入和划出来触发事件

```javascript
    $("input").on("mouseover mouseout",function(){
        $(this).toggleClass("over");
    })
```

- 关于函数的命名空间，方便一次性删除所有自己定义的事件，而不影响到别人的。

```javascript
    $("input").on("mouseover.my",function(){
        console.log("mouseover");
    }).on("mouseout.my",function(){
        console.log("mouseout");
    }).on("click",function(){
        console.log("click");
    });
    $(".btn").on("click",function(){
        $("input").off(".my");  // 点击之后会删除出click之外的所以.my绑定的事件
    })
```

- 自定义事件其实可以很方便的被其它按钮通过事件来触发，如下，在文本框绑定了俩个`click`事件，只不过一个是在命名空间内，然后通过按钮`btn`来触发命名空间`click.my`的点击事件

```javascript
    $("input").on("click", function(){
        console.log("click");
    }).on("click.my", function(){
        console.log("click my");
    })
    $(".btn").on("click", function() {
         $("input").trigger("click.my");
    })
```


- `show, hide`可以接受一个数值参数，单位为毫秒，表示多少毫秒之内动画完成，同时会改变元素的宽度、高度、透明度。
- `fadeIn, fadeOut`只会在一段时间内改变元素的不透明度。
- `slideDown, slideUp` -- 元素改变垂直方向的尺寸。

--- 

### 动画 animate

`+=` - 触发累加操作。
`$(this).animate({"left": "500px"},1000). animate({"height": "200px"});`- 对于多个动画可以通过链条的方式链接起来。

```javascript
    $(".panel").on("click.my", function() {
            $(this).css("opacity", "0.5").animate({
                "height": "200px",
                left: "500px",
                "opacity": "1"
            }, 1000).
            animate({
                "top": "200px",
                width: "200px",
                opacity: "0.5"
            }, 1000).
            fadeOut("slow");
        });
```

- `animate`有一个动画队列，所有的动画都在在这个队列中被执行，而`css`设置的样式不会参与这个队列，所以它是被立即执行的。如果想在动画过程中设置`css`样式，那么就需要把`css`样式放到`animate`的回调函数中，对非动画方法实现排序。

```javascript
    $(".panel").on("click.my", function() {
            $(this).css("opacity", "0.5").animate({
                "height": "200px",
                left: "500px",
                "opacity": "1"
            }, 1000).
            animate({
                "top": "200px",
                width: "200px",
                opacity: "0.5"
            }, 1000, function(){
                $(this).css({"border": "solid 1px blue", "border-radius": "10px"});
            });
        });
```

- 对于鼠标的`hover`事件，如果想要避免动画的累计，即便鼠标先`hover`，然后又`out`，此刻虽然鼠标已经离开了，但是`out`事件只是添加到了动画队列，需要等待`hover`执行完成之后才会执行`out`事件。这样交互就很差劲了。
- 为了避免这种情况需要在每个状态之前先清空动画列表，然后开始执行动画，这样就不会有动画积累效果了。

```javascript
    $(".panel").hover(function(){
        $(this).stop() // 每次动画之前先清空动画
                .animate({height: "200px", left: "200px"},200);
    },function(){
        $(this).stop() // 每次动画之前先清空动画
                .animate({height: "100px", left: 0},300);
    })
```

- `stop(clearQueue, gotoEnd)` -- 接受俩个参数，清空未执行的队列和直接将当前正在执行的动画跳到最后。

- 因为动画元素会产生动画积累，为了避免这种情况，在执行动画之前需要先进行判断，如果当前正在执行动画，则不添加动画列表，

```javascript
    $(".panel").on("click",function(){
        if(!$(this).is(":animated")){
            $(this).animate({"left": "+=100px"},1000);
        }
    });
```

- `delay` -- 可以通过在动画执行过程中添加`delay`来控制间隔执行时间。

- `toggle()`-- 切换元素的可见状态。
- `slideToggle` -- 通过改变高度来切换元素的可见。
- `fateTo(600,0.3)` -- 改变透明度
- `fadeToggle()` -- 改变元素的透明度来改变元素的可见性，

