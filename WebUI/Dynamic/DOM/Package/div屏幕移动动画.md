---
title: div屏幕移动动画
date: 2016-06-11
tags: [JavaScript,动画,DOM]
categories: Dynamic
---

[div屏幕移动动画](http://jsbin.com/recaliz/2/edit?html,js,output)

```html
<style>
        div{
            height: 200px;
            width: 200px;
            background-color: yellow;
            position: absolute;
            top: 100px;
            left: 100px;
        }
</style>

<div></div>

<script>
        var a = document.querySelector("div");
        var moveBox = {
            init: function(node, len, max) {
                this.node = node;
                this.len = len;
                this.max = max;
                this.clock = 0;
                this.left = this.node.offsetLeft;
                this.top = this.node.offsetTop;
                this.bind();
            },

            bind: function() {
                if (this.left < this.max) {
                    this.timeOut();
                } else {
                    return;
                }
            },

            timeOut: function() {
                var me = this;
                this.clock = setTimeout(function() {
                    if (me.left < me.max) {
                        me.left += me.len;
                        me.top += me.len;
                        me.moveAnimate();
                        me.timeOut();

                    } else {
                        clearTimeout(me.clock);
                    }
                }, 10);

            },

            moveAnimate: function() {
                this.node.style.left = this.left + "px";
                this.node.style.top = this.top + "px";
            }
        };
        moveBox.init(a, 1, 500);
    </script>
```



