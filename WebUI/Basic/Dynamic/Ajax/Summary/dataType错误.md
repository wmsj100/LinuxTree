---
title: dataType错误
date: 2016-04-27
tags: [Error]
categories: Dynamic
---

jQuery中的ajax的正确写法

```javascript
$.ajax({
  url: "a.com",
  type: "get",
  datatype: "json",
  data: {"state": 1},
  success: function(data){
   	console.log(data);
	},
  error: function(data){
  console.log("error");
}

})
```

我的错误写法：

```javascript
dataType: "json",
```

我把`datatype`中的`t`大写了，所以老是执行`error`函数，不执行`success` 函数。