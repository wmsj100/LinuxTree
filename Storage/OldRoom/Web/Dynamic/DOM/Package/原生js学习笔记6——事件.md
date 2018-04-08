---
title: 原生js学习笔记6——事件
date: 2016-05-30
tags: [DOM,事件]
categories: Dynamic
---

以后对于这种代码还是谨慎的好，因为我基本是不会仔细去看的。

事件对象鼠标事件

event.clientX在可视区中，鼠标点击的x坐标
event.clientY在可视区中，鼠标点击的y坐标

示例：

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <script type="text/javascript">
        document.onclick = function  () {
            alert(event.clientX + ',' + event.clientY);
        }
    </script>
</head>
<body>

</body>
</html>

示例：一个跟随鼠标指针移动的红色块

demo.gif

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
    <style type="text/css">
        #div {
            width: 100px;
            height: 100px;
            background-color :red;
            position: absolute;
        }

    </style>
    <script type="text/javascript">
        // 鼠标移动时触发改事件
        document.onmousemove = function  (ev) {

            // 获取距离文档顶部的高度
            var oScrollTop = document.documentElement.scrollTop || document.body.scrollTop;
            // 获取距离文档左边的的宽度
            var oScrollLeft = document.documentElement.scrollLeft || document.body.scrollLeft;

            // 获取鼠标事件
            var oEvent = event || ev;
            // 获取到div
            var oDiv = document.getElementById('div');

            // 设置div的位置
            oDiv.style.left = oEvent.clientX + oScrollLeft + 'px';
            oDiv.style.top = oEvent.clientY + oScrollTop + 'px';

        }
    </script>
</head>
<body>

    <div id = "div"></div>

</body>
</html>

示例：一串跟着鼠标走的div

demo.gif

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
    <style type="text/css">
        #div {
            width: 10px;
            height: 10px;
            background-color :red;
            position: absolute;
        }

    </style>
    <script type="text/javascript">
        // 鼠标移动时触发改事件
        window.onload = function  () {

            var oDivs = document.getElementsByTagName('div');

            document.onmousemove = function  (ev) {
                var oEvent = ev || event;

                oDivs[0].style.left = oEvent.clientX+'px';
                oDivs[0].style.top = oEvent.clientY+'px';

                for (var i = oDivs.length-1; i > 0; i--) {
                    oDivs[i].style.left = oDivs[i-1].style.left;
                    oDivs[i].style.top = oDivs[i-1].style.top;

                };


            }


        }
    </script>
</head>
<body>

    <div id = "div"></div>
    <div id = "div"></div>
    <div id = "div"></div>
    <div id = "div"></div>
    <div id = "div"></div>
    <div id = "div"></div>
        <div id = "div"></div>
    <div id = "div"></div>
    <div id = "div"></div>
    <div id = "div"></div>
    <div id = "div"></div>
    <div id = "div"></div>
        <div id = "div"></div>
    <div id = "div"></div>
    <div id = "div"></div>
    <div id = "div"></div>
    <div id = "div"></div>
    <div id = "div"></div>
        <div id = "div"></div>
    <div id = "div"></div>
    <div id = "div"></div>
    <div id = "div"></div>
    <div id = "div"></div>
    <div id = "div"></div>
        <div id = "div"></div>
    <div id = "div"></div>
    <div id = "div"></div>
    <div id = "div"></div>
    <div id = "div"></div>
    <div id = "div"></div>


</body>
</html>

键盘事件

    keyCode获取用户按下键盘的哪个按键

如：键盘控制DIV移动

    ctrlKey 返回boolean值，按下时为true
    shiftKey 返回boolean值，按下时为true
    altKey 返回boolean值，按下时为true

示例：用提示框将用户按的按键提示出来：

demo.gif

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <script type="text/javascript">
        // 按动键盘时触发事件
        document.onkeydown = function (ev) {
            var oEvent = ev || event;
            // 获取到按动的是哪个按键
            alert(oEvent.keyCode);
        }
    </script>
</head>
<body>

</body>
</html>

示例：通过上下左右按键控制DIV的移动

demo.gif

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style type="text/css">
        #div1 {
            width: 100px;
            height: 100px;
            left:10px;
            top:10px;
            background-color: gray;
            position: absolute;
        }
    </style>

    <script type="text/javascript">
        document.onkeydown = function  (ev) {
            var oEvent = ev || event;
            var oDiv = document.getElementById('div1');

            if (oEvent.keyCode == 37) {
                oDiv.style.left =  oDiv.offsetLeft - 10 +'px';
            } else if (oEvent.keyCode==38) {
                oDiv.style.top = oDiv.offsetTop - 10 +'px';
            } else if (oEvent.keyCode == 39) {
                oDiv.style.left = oDiv.offsetLeft + 10 +'px';
            } else if (oEvent.keyCode == 40) {
                oDiv.style.top = oDiv.offsetTop + 10 +'px';
            };
        }

    </script>
</head>
<body>
    <div id = "div1"> </div>
</body>
</html>

示例：按住control+enter键，提交留言框中的文字到留言板中

demo.gif

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>

    <script type="text/javascript">
        window.onload = function  () {
            var oText1 = document.getElementById('text1');
            var oText2 = document.getElementById('text2');
            var oBtn = document.getElementById('btn');

            // 鼠标点击提交按钮。进行留言
            oBtn.onclick = function  () {
                //点击提交按钮后，把留言框中的文字提交在留言区
                oText1.value += oText2.value + '\n';
                // 清空留言框
                oText2.value = '';
            };    

            // 按下control+enter按钮，进行留言,因为当前焦点在留言框中，所以事件要加载留言框中
            oText2.onkeydown = function  (ev) {
                var oEvent = ev || event;

                // 按下回车键和control键
                if (oEvent.keyCode == 13 && oEvent.ctrlKey) {
                    //点击提交按钮后，把留言框中的文字提交在留言区
                oText1.value += oText2.value + '\n';
                // 清空留言框
                oText2.value = '';
                };
            }
        }
    </script>
</head>
<body>
    <textarea id = 'text1' roes = '10' cols = '40'></textarea>
    <br />

    <input type = "text" id = 'text2'/>
    <input type="button" value = '提交' id = 'btn'/>


</body>
</html>

事件冒泡

子标签发生事件后，向父级发送该事件，一直追溯到document。如：点击一个嵌套在body中的button，则该button的onclick事件也会传递给body、document中，触发他们的onclick里触发的函数.

示例：

    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <title></title>
    <style type="text/css">
        div {
            width: 100px;
            height: 100px;
            background-color: red;
            display: none;
        }
    </style>


    <script type="text/javascript">
        window.onload = function () {

            var oBtn = document.getElementById('button');
            var oDiv = document.getElementById('div');

            // 点击buton后，button的事件会被触发
            oBtn.onclick = function() {
                oDiv.style.display = 'block';
                alert("button被点击了");
            }

            // 由于事件冒泡，作为父级的document的onclick事件也会被触发
            document.onclick = function() {

                oDiv.style.display = 'none';
                alert("document被点击了")
            }
        }
    </script>
    </head>
    <body>
    <input type = "button" value = "显示" id = "button">
    <div id = "div"></div>

    </body>
    </html>

取消冒泡

由于事件冒泡会触发父级的相关方法，所以我们经常会“取消事件冒泡”。

取消事件冒泡的方法:event.cancelBubble=true

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
    <title></title>
    <style type="text/css">
        div {
            width: 100px;
            height: 100px;
            background-color: red;
            display: none;
        }
    </style>


    <script type="text/javascript">
        window.onload = function () {

            var oBtn = document.getElementById('button');
            var oDiv = document.getElementById('div');

            // 点击buton后，button的事件会被触发
            oBtn.onclick = function(ev) {
                oDiv.style.display = 'block';
                alert("button被点击了");
                // 在这里取消事件冒泡，防止事件向父级传递
                // 兼容性考虑，有的浏览器的事件并不是'event'，所以把点击事件作为参数传递过来
                var oEvent = ev || event;
                oEvent.cancelBubble=true;

            }

            // 由于事件冒泡，作为父级的document的onclick事件也会被触发
            document.onclick = function() {

                oDiv.style.display = 'none';
                alert("document被点击了")
            }
        }
    </script>
    </head>
    <body>
    <input type = "button" value = "显示" id = "button">
    <div id = "div"></div>

    </body>
    </html>

事件的默认行为

浏览器自带的行为就是默认行为
阻止默认行为

只要将默认的事件return false，就可以组织默认行为的执行。

示例：自定义右键菜单：默认的右键菜单是系统提供的选项，我们可以阻止默认的右菜单，来自定义新右键菜单样式

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
    <style type="text/css">
        ul {
            list-style-type: none;
            display:none;
            position:absolute;
        }
        * {
            margin: 0;
            padding: 0;
        }
    </style>
    <script type="text/javascript">

        // 鼠标右键触发的时间
        document.oncontextmenu = function  (ev) {
            var oUl = document.getElementById('ul1');
            var oEvent = ev || event;
            oUl.style.display = 'block';

            oUl.style.left = oEvent.clientX + 'px';
            oUl.style.top = oEvent.clientY + 'px';

            return false;
        }

        // 鼠标左键触发的事件
        document.onclick  = function  (ev) {
            var oUl = document.getElementById('ul1');
            oUl.style.display = 'none';

        }
    </script>
</head>
<body>

    <!-- 自定义右键菜单 -->
    <ul id = 'ul1' >
        <li>首页</li>
        <li>登录</li>
        <li>注册</li>
    </ul>

</body>
</html>

示例：输入框中只能输入数字和退格

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <script type="text/javascript">
        window.onload = function  () {
            var oText = document.getElementById('text');
            oText.onkeydown = function  (ev) {
                var oEvent = ev || event;
                if ( (oEvent.keyCode < 40 && oEvent.keyCode != 8) || oEvent.keyCode > 57 ) {
                    return false;
                };

            }
        }
    </script>
</head>
<body>
    <input type = "text"  id = "text">

</body>
</html>

拖拽

拖拽时，鼠标经历三个事件：

    onmousedown 鼠标按下时，存储当前鼠标距离拖拽对象左上角的距离
    onmousemove 鼠标移动时，根据鼠标移动的距离移动拖拽对象的位置
    onmouseup 鼠标抬起时，停止拖拽

示例：鼠标拖拽一个div

demo.gif

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style type="text/css">
        #div1 {
            width: 100px;
            height: 100px;
            background-color : red;
            position: absolute;
        }
    </style>

    <script type="text/javascript">
        window.onload = function  () {

            var oDiv = document.getElementById('div1');
            // 当鼠标按下时计算鼠标距离div左上角的位置
            oDiv.onmousedown = function  (ev) {
                var oEvent = ev || event;
                var oX = oEvent.clientX - oDiv.offsetLeft;
                var oY = oEvent.clientY - oDiv.offsetTop;

                // 当鼠标开始移动，重新设置div的位置
                document.onmousemove = function  (ev) {
                    var oEvent = ev || event;
                    oDiv.style.left = oEvent.clientX - oX + 'px';
                    oDiv.style.top = oEvent.clientY - oY + 'px';

                };

                // 当鼠标抬起，结束移动，清除移动事件的函数
                document.onmouseup = function  () {
                    document.onmousemove = null;
                    document.onmouseup = null;
                };


            };

        };
    </script>
</head>
<body>
    <div id = "div1"></div>
</body>
</html>

推荐拓展阅读 

文／小全同学（简书作者）
原文链接：http://www.jianshu.com/p/f48da9338cd0