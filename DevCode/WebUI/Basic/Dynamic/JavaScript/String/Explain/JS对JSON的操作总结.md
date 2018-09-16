---
title: JS对JSON的操作总结
date: 2016-3-30 20:38:37
tags: [JSON,JavaScript]
categories: Dynamic
---
---
[查看原始文档](http://getpocket.com/redirect?url=http%3A%2F%2Fwww.cnblogs.com%2Fcsj222%2Farchive%2F2013%2F04%2F11%2F3013667.html)		[javascript](chrome-extension://mjcnijlhddpbdemagnpefmlkjdagkogk/a/queue/grid/javascript)	[json](chrome-extension://mjcnijlhddpbdemagnpefmlkjdagkogk/a/queue/grid/json)

对于前端完全是菜鸟，迫于无奈，工作中要用到JS，尤其对JSON的处理为多，网上搜了一下，所讲的基本雷同。

<!-- more -->

所以把平时用的比较多的JSON处理方法总结了一下，权当加深记忆。


**一、概述**

JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式，采用完全独立于语言的文本格式，是理想的数据交换格式。同时，JSON是 JavaScript 原生格式，这意味着在 JavaScript 中处理 JSON数据不须要任何特殊的 API 或工具包。

在JSON中，有两种结构：对象和数组。

**1.****对象**

一个对象以“{”开始，“}”结束。每个“key”后跟一“:”，“‘key/value’ 对”之间运用 “,”分隔。

packJson = {"name":"nikita", "password":"1111"}

**2.****数组**

packJson = [{"name":"nikita", "password":"1111"}, {"name":"tony", "password":"2222"}];

数组是值的有序集合。一个数组以“[”开始，“]”结束。值之间运用 “,”分隔。

**二、****JSON****对象和****JSON****字符串的转换**

在数据传输流程中，json是以文本，即字符串的形式传递的，而JS操作的是JSON对象，所以，JSON对象和JSON字符串之间的相互转换是关键。例如：

JSON字符串：

var jsonStr = '{"name":"nikita", "password":"1111"}';

JSON对象：

var jsonObj = {"name":"nikita", "password":"1111"};

对于前端完全是菜鸟，迫于无奈，工作中要用到JS，尤其对JSON的处理为多，网上搜了一下，所讲的基本雷同。所以把平时用的比较多的JSON处理方法总结了一下，权当加深记忆。

**一、概述**

JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式，采用完全独立于语言的文本格式，是理想的数据交换格式。同时，JSON是 JavaScript 原生格式，这意味着在 JavaScript 中处理 JSON数据不须要任何特殊的 API 或工具包。

在JSON中，有两种结构：对象和数组。

**1.****对象**

一个对象以“{”开始，“}”结束。每个“key”后跟一“:”，“‘key/value’ 对”之间运用 “,”分隔。

packJson = {"name":"nikita", "password":"1111"}

**2.****数组**

packJson = [{"name":"nikita", "password":"1111"}, {"name":"tony", "password":"2222"}];

数组是值的有序集合。一个数组以“[”开始，“]”结束。值之间运用 “,”分隔。

**二、****JSON****对象和****JSON****字符串的转换**

在数据传输流程中，json是以文本，即字符串的形式传递的，而JS操作的是JSON对象，所以，JSON对象和JSON字符串之间的相互转换是关键。例如：

JSON字符串：

var jsonStr = '{"name":"nikita", "password":"1111"}';

JSON对象：

var jsonObj = {"name":"nikita", "password":"1111"};

2、String转换为Json

```
var myObject = eval('(' + myJSONtext + ')'); 

```

eval是js自带的函数，不是很安全，可以考虑用json包。

**三、遍历****JSON****对象**

```
myJson = {"name":"nikita", "password":"1111"};

for(var p in myJson){//遍历json对象的每个key/value对,p为key

   alert(p + " " + myJson[p]);

}

```

**运行结果：**

![](filesystem:chrome-extension://mjcnijlhddpbdemagnpefmlkjdagkogk/persistent/images/7fd651e735426cc3284fd1f7206d0c0b.png)

**四、遍历****JSON****数组**

```
packJson = [

{"name":"nikita", "password":"1111"},

{"name":"tony", "password":"2222"}

];

for(var p in packJson){//遍历json数组时，这么写p为索引，0,1

   alert(packJson[p].name + " " + packJson[p].password);

}

```

我更倾向于这种写法：

```
for(var i = 0; i < packJson.length; i++){

   alert(packJson[i].name + " " + packJson[i].password);

}

```

运行结果：

![](filesystem:chrome-extension://mjcnijlhddpbdemagnpefmlkjdagkogk/persistent/images/cb539eb1486378f3d39c7e219e18a701.png)

**五、将两个****JSON****对象组装到一个里面**

```
//targetJson 目标JSON，packJson 被组装JSON

function addGroupJson(targetJson, packJson){

    if(targetJson && packJson){

       for(var p in packJson){

           targetJson[p] = packJson[p];

       }

    }

}

```

用法如下：

```
var json1 = {"name":"nikita"};
var json2 = {"password":"1111"};
addGroupJson(json1, json2);
alert(json2str(json1));
```

运行结果：

![](filesystem:chrome-extension://mjcnijlhddpbdemagnpefmlkjdagkogk/persistent/images/dfc21f74c31cdba2f149d5f89522b094.png)