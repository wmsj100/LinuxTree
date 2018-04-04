---
title: console-log功能简述
date: 2016-03-24 12:18:58
tags: [浏览器]
categories: Dynamic
---
[参考文献](http://www.cnblogs.com/worfdream/articles/1956449.html)[http://www.json.org/](http://www.json.org/)[http://json.org/example.html](http://json.org/example.html)
<!-- more -->
```
var a={
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}
console.log(a);  //Object {glossary: Object}
var b=JSON.stringify(a);    //typeof a  "object"
console.log(b);
//"{"glossary":{"title":"example glossary","GlossDiv":{"title":"S","GlossList":{"GlossEntry":{"ID":"SGML","SortAs":"SGML","GlossTerm":"Standard Generalized Markup Language","Acronym":"SGML","Abbrev":"ISO 8879:1986","GlossDef":{"para":"A meta-markup language, used to create markup languages such as DocBook.","GlossSeeAlso":["GML","XML"]},"GlossSee":"markup"}}}}}";
var c=JSON.parse(b);    
console.log(c);    //Object {glossary: Object}
```
- JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式，采用完全独立于语言的文本格式，是理想的数据交换格式。同时，JSON是 JavaScript 原生格式，这意味着在 JavaScript 中处理 JSON数据不须要任何特殊的 API 或工具包。
- 在JSON中，有两种结构：对象和数组。
 1. 一个对象以“{”（左括号）开始，“}”（右括号）结束。每个“名称”后跟一个“:”（冒号）；“‘名称/值’ 对”之间运用 “,”（逗号）分隔。 名称用引号括起来；值如果是字符串则必须用括号，数值型则不须要。例如：

    var o={"xlid":"cxh","xldigitid":123456,"topscore":2000,"topplaytime":"2009-08-20"}；
- 在数据传输流程中，json是以文本，即字符串的形式传递的，而JS操作的是JSON对象，所以，JSON对象和JSON字符串之间的相互转换是关键。例如：
 JSON字符串:
    var str1 = '{ "name": "cxh", "sex": "man" }';
    JSON对象:
    var str2 = { "name": "cxh", "sex": "man" };
