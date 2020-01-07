---
title: hasClass()——-博主原文
date: 2016-4-1 17:36:44
tags: [DOM,函数,事件]
categories: Dynamic
---

有时候，我们需要判断节点是否含有我们要寻找的class，这里，我们想到原生的JS给我们提供了className这个方法，既可以读又可以写。但class是可以组合的，也就是说，会有这种情况：
<!-- more -->
class="test1 test2"，这样通过className获取出来的，则就是一个"test1 test2"字符串了，达不到我们要查找指定的class的目的。所以，我们有必要写一个可以获取指定class的函数。

思路：既然className能获取一整个class字符串，那我们能不能通过这一个字符串寻找到我们指定要的class字符串呢？我们知道，组合class是通过一个空格或者多个空格组合的，那么，是不是可以利用这个空格将所有class放进一个数组，然后遍历这个数组匹配到我们指定的class呢？答案是肯定的，根据以上分析，我们可以组织到下面的步骤：

1.利用className的特性将各个class存进数组；

2.遍历数组，匹配class；

3.成功匹配返回true，否则返回false。

现在，我们就可以将上面的思路用代码来实现，实现如下：
```
function hasClass(className,node){
        var classNames = node.className.split(/\s+/);    //步骤1

        for(var i = 0; i < classNames.length; i++){         //步骤2
            if(classNames[i] == className){
                return true;
            }
        }

        return false;
} 
```
测试函数代码如下：
```
<script type="text/javascript">
    function hasClass(className,node){
        var classNames = node.className.split(/\s+/);

        for(var i = 0; i < classNames.length; i++){
            if(classNames[i] == className){
                return true;
            }
        }

        return false;
    } 
    window.onload = function(){
        var test = document.getElementById('test');
        alert(hasClass('test1',test));    //true
        alert(hasClass('test2',test));    //true
        alert(hasClass('test3',test));    //false
    }
</script>
</head>
<body>
    <div id="test" class="test1 test2">test</div>
</body>
////////////////////////////////////////////////  华丽丽的分隔线///////////////////////////////////////////////////////
```
2012.3.5 add

一个更简短的写法：
```
1 var hasClass = function(element,className){
2      return new RegExp("(^|\\s)"+className+"(\\s|$)").test(element.className);
3 }
```

