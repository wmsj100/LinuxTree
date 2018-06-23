---
title: javascript 事件处理 鼠标拖动效果
date: 2016-05-29
tags: [封装,JavaScript]
categories: Dynamic
---

这个代码确实让我收益颇多
http://www.cnblogs.com/hyjiacan/archive/2012/05/10/javascript-drag-layer.html

```javascript
        function $id(id){
            return document.getElementById(id);
        }

        var isIE = (window.navigator.userAgent.indexOf("IE") == -1) ? false : true;
        var win = $id("win");
        var header = $id("win_header");
        var pos = function(x,y){
            this.x = x;
            this.y = y;
        }
        var originalPos = new pos(20,20);
        var oldMouse = new pos(0,0);
        var oldPos = new pos(0,0);
        var newPos = new pos(0,0);

        win.style.left = originalPos.x + "px";
        win.style.top = originalPos.y + "px";

        function bind(ev,func){
            if(isIE){
                header.attachEvent("on" + ev, func);
            }else{
                header.addEventListener(ev,func,false);
            }
        }

        function isLeftButton(btn){
            if(isIE){
                if(btn == 1){
                    return true;
                }else{
                    return false;
                }
            }else{
                if(btn == 0){
                    return true;
                }else{
                    return false;
                }
            }
        }

        var mousedown = false;

        function over(e){
            header.style.backgroundColor = "#5d5d5d";
        }

        function out(e){
            header.style.backgroundColor = "#4d4d4d";
            up(e);
        }

        function down(e){
            e = e || event;
            if(!isLeftButton(e.button)){
                return;
            }
            mousedown = true;
            oldMouse.x = e.clientX;
            oldMouse.y = e.clientY;

            oldPos.x = win.offsetLeft;
            oldPos.y = win.offsetTop;
        }

        function up(e){
            // e = e || event;
            if(!isLeftButton(e.button)){
                return;
            }
            mousedown = false;
        }

        function move(e){
            if(!isLeftButton(e.button)){
                return;
            }
            if(mousedown){
                e = e || event;
                newPos.x = e.clientX - oldMouse.x;
                newPos.y = e.clientY - oldMouse.y;
                win.style.left = (oldPos.x + newPos.x) + "px";
                win.style.top = (oldPos.y + newPos.y) + "px";
            }
        }

        bind("mouseover",over);
        bind("mouseenter",over);
        bind("mouseout",out);
        bind("mouseleave",out);
        bind("blur",out);
        bind("mousedown",down);
        bind("mouseup",up);
        bind("mousemove",move);
```

在经历了漫长的时期，终于下定了决心自己写一个层的拖动。
当然了，其它的拖动也是这样的思路和做法，或者说，这样的拖动适合所有的可见元素。

先看看要拖动的层（模拟窗口）的效果图吧。

要实现的拖动效果：鼠标左键在窗口上方的标题栏上按下，同时移动鼠标，窗口跟着移动。

 

窗口：

```javascript
<div id="win">
<div id="win_header"></div>
</div>
```
 

一点准备工作：
要让窗口能自由移动，那么窗口的定位（position）应该采用绝对定位（absolute）；
给窗口添加标题栏，这里使用一个放在窗口顶部的层实现，同时将标题栏的鼠标光标设置为拖动（move）形状（在chrome中拖动的时候，光标会变成文字光标，松开鼠标键后恢复）。
```javascript

#win {
position:absolute;
width:480px;
height:320px;
background-color:#d4d4d4;
border: 1px solid #4d4d4d;
}
#win_header {
width:480px;
height:48px;
background-color:#4d4d4d;
cursor:move;
}

```

 

定义一个工具函数，用来获取指定ID属性的元素：

```javascript
function $id(id) {
return document.getElementById(id);
}

 

定义一个浏览器核心标识isIE：

var isIE = (window.navigator.userAgent.indexOf("IE") == -1) ? false : true;

 

获取到窗口元素及其标题栏：

var win = $id("win");
var header = $id("win_header");

 

为了方便记录鼠标和窗口的位置信息，创建一个位置：

var pos =function(x, y) {
this.x = x;
this.y = y;
};

 

给窗口设置一个初始位置（css的left值和top值）。
这里不知道是为什么，如果不使用js设置这两个属性，就取不到值，在CSS中指定了也不行。

var originalpos = new pos(20, 20);

 

在拖动窗口的过程中，需要记录的值有：
鼠标按下时鼠标光标的位置

var oldmouse =new pos(0, 0);

 

鼠标按下时窗口的位置

var oldpos = new pos(0, 0);

 

鼠标移动时窗口的新的位置

var newpos = new pos(0, 0);

 

设置窗口的初始位置

win.style.left = originalpos.x + "px";
win.style.top = originalpos.y + "px";

 

又是因为浏览器的差异（IE和非IE），元素绑定事件处理函数的方法不同（IE使用attachEvent，非IE使用addEventListener），为了简化事件绑定的操作，定义一个事件绑定函数：
```

```javascript
function bind(ev, func) {
if(isIE) {
　　header.attachEvent("on" + ev, func);
} else {
　　header.addEventListener(ev, func, false);
}
}
```


 

在做好这些工作后，就可以开始处理鼠标事件了。

在这个程序中，只希望鼠标左键拖动窗口，其它键都不能，所以需要判断是否是鼠标左键按下。而这个判断会在几个函数中都使用到，所以提取出来到一个函数中，通过传入的参数（鼠标键值，即按下了哪个键）判断。在这里，需要注意浏览器间的差异：IE中鼠标左键的值是1，而非IE中值是0.
```javascript

function isLeftButton(btn) {
    if(isIE) {
        if(btn == 1)
            return true;
        else
            return false;
    } else {
        if(btn == 0)
            return true;
        else
            return false;
    }
}
```

```javascript

 

拖动动作是在按下鼠标左键后移动来完成的。把这个动作分享开来，即是鼠标先触发了按下动作（mousedown），然后触发了移动动作（mousemove）。为了判断是否是真的在拖动还是只是鼠标从窗口上经过，设置一个变量来记录鼠标按下的状态：

var mousedown = false;

 

由于CSS中存在的兼容性问题，这里使用js来控制鼠标悬停在窗口标题栏上面的时候的颜色变化。
悬浮

function over(e){
　　header.style.backgroundColor = "#5d5d5d";
}

 


离开

function out(e) {
header.style.backgroundColor = "#4d4d4d";
// 有时候鼠标会在未松开的情况下离开窗口，
// 此时通过触发鼠标的松开事件来使窗口脱离鼠标的控制
up(e);
}

 


按下
在按下事件中，需要先判断是否按下的是鼠标的左键；
若是才记录鼠标和窗口此时的位置，否则不记录。
```

```javascript

function down(e) {
    e = e || event;
    
    if(!isLeftButton(e.button))
        return;
    
    mousedown = true;
    oldmouse.x = e.clientX;
    oldmouse.y = e.clientY;
    
    oldpos.x = parseInt(win.style.left.replace("px", ""));
    oldpos.y = parseInt(win.style.top.replace("px", ""));
}
```

```javascript

 


松开

function up(e) {
    if(!isLeftButton(e.button))
        return;
    mousedown = false;
}
```
 


移动
这里就涉及到鼠标的两个事件：
按下和移动。当且仅当鼠标左键按下时，移动动作才有效。
窗口的新位置，是由鼠标在拖动状态下的移动距离（X和Y的距离）决定的。即：
新的鼠标位置送去按下左键时记录下的位置，得到一个距离，然后将窗口的位置加上鼠标移动的距离得到窗口的新位置。
```javascript

function move(e) {
    if(!isLeftButton(e.button))
        return;
        
    if(mousedown) {
        e =e || event;
        
        newpos.x = e.clientX - oldmouse.x;
        newpos.y = e.clientY - oldmouse.y
    
        win.style.left = (oldpos.x + newpos.x) + "px";
        win.style.top = (oldpos.y + newpos.y) + "px";
    }
}
```

事件处理都写好了，最后来给元素绑定上吧，阿门！
```javascript

bind("mouseover", over);
bind("mouseenter", over);
bind("mouseout", out);
bind("mouseleave", out);
bind("blur", out);
bind("mousedown", down);
bind("mouseup", up);
bind("mousemove", move);
```

不过在FF中的拖动有问题，只能第一次正常拖动，后面就有点乱了！