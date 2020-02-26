---
title: ajax字符串转换DOM标签
date: 2016-4-6 00:11:27
tags: [Ajax,DOM,函数]
categories: Dynamic
---

通过`ajax`得到`ajax.responseText`字符串，
<!-- more -->
`var str=ajax.responseText`;

```javascript
function jsonData(str){
	var jsonStr=JSON.parse(str);
	var info="";
	for(var i in jsonStr){
		info+="<dt>"+i+"</dt><dd>"+jsonStr[i]+"</dd>";
	}
	info=info.replace(info,"<dl>"+info+"</dl>");
	return info;
}//
```

这里用到了`replace`替换自身。