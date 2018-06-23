---
title: 原生javascript实现鼠标拖动效果
date: 2016-05-30
tags: [DOM,事件]
categories: Dynamic
---

之前使用最多的鼠标事件也就这些`mouseenter`, `mouseleave`, `click`, 至于`mouseover`, `mouseout`,我不知道和前俩个有什么区别，反正我自己是没有用到过这俩个的场景，一般都使用前俩个了。
这一次又接触到一个新的事件`mousemove`,这个就是鼠标在对象上面移动时候会时刻触发事件，直接上代码吧，之前看了别人的代码，这个也是他的缩减版，但这是我自己的理解，去掉了那些兼容性的东西。
```javascript
var a = document.querySelector("div");

function pos(x, y) {
    this.x = x;
    this.y = y;
}
var oldMouse = new pos(0, 0);
var oldPos = new pos(0, 0);
var newPos = new pos(0, 0);

function bind(eventType, handler) {
    a.addEventListener(eventType, handler, false);
}
var mousedown = false;  //设置的锁

function isLeft(btn) {
    if (btn == 0) {
        return true;
    }
    return false;
}


function down(e) {
    if (!isLeft(e.button)) {
        return;
    }
    mousedown = true;
    oldMouse.x = e.clientX;
    oldMouse.y = e.clientY;
    oldPos.x = a.offsetLeft;
    oldPos.y = a.offsetTop;
    // a.style.cursor = "move";          
}

function move(e) {

    if (!isLeft(e.button)) {
        return;
    }
    if (mousedown) {
        var x = e.clientX - oldMouse.x;
        var y = e.clientY - oldMouse.y;
        newPos.x = oldPos.x + x;
        newPos.y = oldPos.y + y;
        a.style.left = newPos.x + "px";
        a.style.top = newPos.y + "px";
    }
}

function up(e) {
    if (!isLeft(e.button)) {
        return;
    }
    mousedown = false;
}

bind("mousedown", down);
bind("mousemove", move);
bind("mouseup", up);
bind("mouseout", up);   //设置锁，防止拖动文字意外拖动框
bind("mouseleave", up); //设置锁，防止拖动文字意外拖动框
```

[效果](http://jsbin.com/fiqivo/1/edit?html,css,js,output)