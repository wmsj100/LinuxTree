---
title: 解析并获取url的搜索信息
date: 2016-05-05
tags: [BOM,函数,Package]
categories: Static
---

解析搜索地址的信息：
`var url = "http://localhost/php/Month/June/12.html?name=%E7%8E%8B%E6%B5%A9&age=20&male=male#3"`

7. 我自己的封装

```javascript
      var args = (function(){
            var search = location.search,
                  searchStr = (search.length > 0) ? search.substr(1) : "",
                  arr = (searchStr.length > 0) ? searchStr.split("&") : [],   
                  num = arr.length,
                  args = {},
                  searchArr = [];
                  key = null,
                  value = null;
            while(num--){
               searchArr = arr[num].split("=");
               key = decodeURIComponent(searchArr[0]);
               value = decodeURIComponent(searchArr[1]);
               if(key.length){
                  args[key] = value;
               }
            }
            return args;
      })();
```

6. 尼古拉丝自己的方法，

   ```javascript
   function getQueryStringArgs() {
      //取得查询字符串并去掉开头的问号
      var qs = (location.search.length > 0 ? location.search.substring(1) : ""),
         //保存数据的对象
         args = {},
         //取得每一项
         items = qs.length ? qs.split("&") : [],
         item = null,
         name = null,
         value = null,
         //在 for 循环中使用
         i = 0,
         len = items.length;
      //逐个将每一项添加到 args 对象中
      for (i = 0; i < len; i++) {
         item = items[i].split("=");
         name = decodeURIComponent(item[0]);
         value = decodeURIComponent(item[1]);
         if (name.length) {
            args[name] = value;
         }
      }
      return args;
   }
   ```




1. 结果为一个对象，很容易就可以读取对象的内容；

   ```javascript
   var link = location.search ? location.search.substring(1) : "";
   var linkArray = link.length ? link.split("&") : [];
   var linkInfo = {},
   	linkName = null,
   	linkValue = null;
   for (var i = 0; i < linkArray.length; i++) {
   	linkName = decodeURIComponent(linkArray[i].split("=")[0]);
   	linkValue = decodeURIComponent(linkArray[i].split("=")[1]);
   	if (linkName.length) {
   		linkInfo[linkName] = linkValue;
   	}
   }
   link	//"%E5%A7%93%E5%90%8D=wmsj100&%E6%80%A7%E5%88%AB=male"
   linkInfo	//Object { 姓名: "wmsj100", 性别: "male" }	
   ```

2. 结果为一个数组，但是这个数组的内容不好读取，因为数组内部是字符串；

   ```javascript
   var link = location.search ? location.search.substring(1) : "";
   var linkArray = link.length ? link.split("&") : [];
   var linkInfo = [],
   	linkName = [],
   	linkValue = [];
   for (var i = 0; i < linkArray.length; i++) {
   	linkName.push(decodeURIComponent(linkArray[i].split("=")[0]));
   	linkValue.push(decodeURIComponent(linkArray[i].split("=")[1]));
   	linkInfo.push(linkName[i] + " : " + linkValue[i]);
   }
   link	//"%E5%A7%93%E5%90%8D=wmsj100&%E6%80%A7%E5%88%AB=male"
   link.Info	//[ "姓名:wmsj100", "性别:male" ]
   ```

3. 在2的基础上改进，把数组内部转换为对象：

   ```javascript
   var link = location.search ? location.search.substring(1) : "";
   var linkArray = link.length ? link.split("&") : [];
   var linkInfo = [],
   	
   for (var i = 0; i < linkArray.length; i++) {
   	linkName = decodeURIComponent(linkArray[i].split("=")[0]);
   	linkValue = decodeURIComponent(linkArray[i].split("=")[1]);
   	var linkObj = {};
   	linkObj[linkName] = linkValue;
   	linkInfo[i] = linkObj;
   }
   link	//"%E5%A7%93%E5%90%8D=wmsj100&%E6%80%A7%E5%88%AB=male"
   linkInfo	//[{姓名: "wmsj100"}, {性别: "male"}];
   ```

4. 把整个过程进行封装，思路是把需要的值全部附加到函数的原型上面，通过构造函数来调用这些值；-这应该是我封装的最好的一个函数了。

   ```javascript
   function linkInfo() {
   	var link = location.search ? location.search.substring(1) : "",
   		linkArray = link.length ? link.split("&") : [];
   	linkInfo.prototype = {
   		linkObj: new Object(),
   		linkName: new Array(),
   		linkValue: new Array(),
   		constructor: "linkInfo"
   	};
   	for (var i = 0; i < linkArray.length; i++) {
   		linkInfo.prototype.linkName.push(decodeURIComponent(linkArray[i].split("=")[0]));
   		linkInfo.prototype.linkValue.push(decodeURIComponent(linkArray[i].split("=")[1]));
   		linkInfo.prototype.linkObj[linkInfo.prototype.linkName[i]] = linkInfo.prototype.linkValue[i];
   	}
   };
   linkInfo();
   var a = new linkInfo();
   location.search	
   //"?%E5%A7%93%E5%90%8D=wmsj100&%E6%80%A7%E5%88%AB=male"
   console.log(a.linkName); //Array [ "姓名", "性别" ]
   console.log(a.linkValue); //Array [ "wmsj100", "male" ]
   console.log(a.linkObj); //Object { 姓名: "wmsj100", 性别: "male" }
   ```

5. 把`for` 循环替换为`forEach` 循环

   ```javascript
   function linkInfo() {
   	var link = location.search ? location.search.substring(1) : "",
   		linkArray = link.length ? link.split("&") : [];
   	linkInfo.prototype = {
   		linkObj: new Object(),
   		linkName: new Array(),
   		linkValue: new Array(),
   		constructor: "linkInfo"
   	};
   	linkArray.forEach(function(item, i) {
   		linkInfo.prototype.linkName.push(decodeURIComponent(linkArray[i].split("=")[0]));
   		linkInfo.prototype.linkValue.push(decodeURIComponent(linkArray[i].split("=")[1]));
   		linkInfo.prototype.linkObj[linkInfo.prototype.linkName[i]] = linkInfo.prototype.linkValue[i];
   	});
   };
   linkInfo();
   var a = new linkInfo();
   location.search	
   //"?%E5%A7%93%E5%90%8D=wmsj100&%E6%80%A7%E5%88%AB=male"
   console.log(a.linkName); //Array [ "姓名", "性别" ]
   console.log(a.linkValue); //Array [ "wmsj100", "male" ]
   console.log(a.linkObj); //Object { 姓名: "wmsj100", 性别: "male" }
   ```

   ​


