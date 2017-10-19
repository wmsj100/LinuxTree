---
title: JavaScript数组-字符串-函数-基本操作方法
date: 2016-03-24 12:18:58
tags: [JavaScript,Array]
categories: Dynamic
---
### 问答
- 数组的方法里push、pop、shift、unshift、join、split分别是什么作用？
- push——可以对数组尾部插入一个或多个元素，并返回更新后的数组长度；
  <!-- more -->
```
var num1=[1,2,3];
    	console.log(num1.push("4"));	//返回数组长度4
    	console.log(num1);		//[1, 2, 3, "4"]
    	console.log(num1.push("5","6"));	//返回数组长度6；
    	console.log(num1);		//[1, 2, 3, "4", "5", "6"]
```
- pop——每次会删除数组结尾的元素，并返回删除的元素，若是对空数组调用pop，则返回undefined；
```
var num1=[1,2];
    	console.log(num1.pop());	
    	//删除数组num1的元素2；并返回2
    	console.log(num1);		//[1];
    	console.log(num1.pop());	
    	//输出数组num1的元素1；并返回1；
    	console.log(num1);		//返回空数组；[]
    	console.log(num1.pop());	
    	//删除空数组的元素；并返回undefined；
    	console.log(num1);	//[]
```
- unshift——可以向数组的开头添加一个或更多元素，并返回新数组的长度；它会把参数插入到数组的头部，已经存在的元素会顺次移动到较高的下标处，以便留出空间，第一个参数的下标为0，第二个下标为1，以后依次递增；
```
var num1=[1,2,3];
    	console.log(num1.unshift(4));
    	//在数组的头部插入元素4，并返回数组长度4；
    	console.log(num1);//[4,1,2,3]
    	console.log(num1.unshift(5,6));
    	//在数组的头部插入元素5，6；并返回数组长度6；
    	console.log(num1);//[5,6,4,1,2,3]
```
- shift——用于将数组的第一个元素删除，并且返回删除的元素，如果数组为空，则不进行任何操作，直接返回undefined；
```
var num1=[1];
    	console.log(num1.shift());
    	//删除数组的第一个元素1，并且返回1；
    	console.log(num1);//[]
    	console.log(num1.shift());
    	//此时数组为空，所以不进行操作，直接返回undefined；
    	console.log(num1);//[]
```
- join——用于将数组元素通过指定的分隔符连接成为一个字符串，其作用和toString()相同，都不会修改原数组，如果不知道分隔符，则默认用逗号分隔；
```
var num1=[1,2,3];
    	console.log(num1.toString());//1，2，3
    	//通过toString()把数组转换为字符串，用逗号分隔；
    	console.log(num1);
    	//并不更改原数组，[1,2,3]
    	console.log(num1.join());//1,2,3
    	//不指定分隔符，默认用逗号分隔，
    	console.log(num1);
    	//不更改原数组[1,2,3]
    	console.log(num1.join("-"));
    	//知道“-”为分隔符，1-2-3
    	console.log(num1);
    	//不更改原数组[1,2,3]
```
- slice——可从原数组中选定并返回从下标为start的元素（包含此元素）到下标为end的元素（不包括此元素）的数组元素。不更改原数组；如果没有给出end参数，那么会选择从start开始的到结束的所以元素；
```
var num1=[1,2,3,4,5,6,7];
    	console.log(num1.slice(2,5));
    	//选择num1[2]~num1[4]的元素，并返回新数组[3,4,5]
    	console.log(num1);
    	//不更改原数组，[1,2,3,4,5,6,7]
```
- splice——用于插入、删除、替换数组元素；下面分别介绍：
  - 插入元素：
```
var num1=[1,2,3];
    	console.log(num1.splice(2,0,"4","5"));
        //在num1[2]元素3之前插入元素4，5，并且返回空数组[]
    	console.log(num1);
        //原数组被修改，[1,2,4,5,3]
```
    - 替换元素
```
var num1=[1,2,3];
        console.log(num1.splice(2,1,4));
        //替换num1[2]的元素3为元素4，并且返回被替换的元素[3]
        console.log(num1);
        //原数组被修改[1,2,4]
        console.log(num1.splice(2,1,5,6));
        //替换num1[2]元素4为元素5，6，并且返回被替换的元素[4]
        console.log(num1);
        //原数组被修改[1,2,5,6]
        console.log(num1.splice(1,3,2,3,4));
        //替换num1[1],num1[2],num1[3]三个元素为2，3，4，
        //并且返回被删除的元素数组[2,5,6]
        console.log(num1);
        //原数组被修改为[1,2,3,4]
```
    - 删除元素
```
var num1=[1,2,3,4,5,6];
        console.log(num1.splice(2,1));
        //输出num1[2]元素，并且返回该元素数组[3]
        console.log(num1);
        //原数组被修改为[1,2,4,5,6]
        console.log(num1.splice(1,3));
        //删除num1[1],num1[2],num1[3]三个元素，
        //并且返回被删除的这三个元素数组[2,4,5]
        console.log(num1);
        //原数组被修改为[1,6]
```
> 参考文献——[数组操作函数总结](http://www.phpernote.com/javascript-function/585.html)
---
### 代码题
1. 数组
- 用splice实现push、pop、shift、unshift方法；
  - splice实现push方法：
```
function splicePush(){
            for(var i=1;i<arguments.length;i++){
                if(typeof arguments[0] === "object" && arguments[0] instanceof Array){
                     arguments[0].splice(arguments[0].length,arguments.length-1,arguments[i]);
                }
                else{
                    console.log("请在第一个参数位置输入数组名称")
                    return;
                }
            }
             return arguments[0];
        }
        var num1=[1,2,3,4,5];
        var num2=splicePush(num1,5,6,7,8,34,123);
        console.log(num2);  //[1, 2, 3, 4, 5, 5, 6, 7, 8, 34, 123]
```
    - splice实现pop（）方法：
```
function splicePop(){
                if(typeof arguments[0] === "object" && arguments[0] instanceof Array){
                     arguments[0].splice(arguments[0].length-1,1);
                }
                else{
                    console.log("请在第一个参数位置输入数组名称")
                    return;
                }
             return arguments[0];
        }
        var num1=[1,2,3,4,5];
        var num2=splicePop(num1);
        console.log(num2);  //[1, 2, 3, 4]
```
    - splice实现unshift:
```
function splicePush(){
            for(var i=arguments.length-1;i>0;i--){
                if(typeof arguments[0] === "object" && arguments[0] instanceof Array){
                     arguments[0].splice(0,0,arguments[i]);
                }
                else{
                    console.log("请在第一个参数位置输入数组名称")
                    return;
                }
            }
             return arguments[0];
        }
        var num1=[1,2,3,4,5];
        var num2=splicePush(num1,3,5,6,7,8);
        console.log(num2);  //[3, 5, 6, 7, 8, 1, 2, 3, 4, 5]
```
    - splice实现shift：
```
function splicePush(){
                if(typeof arguments[0] === "object" && arguments[0] instanceof Array){
                     arguments[0].splice(0,1);
                }
                else{
                    console.log("请在第一个参数位置输入数组名称")
                    return;
                }
             return arguments[0];
        }
        var num1=[1,2,3,4,5];
        var num2=splicePush(num1);
        console.log(num2);  //[2, 3, 4, 5]
```
- 使用数组拼接出如下字符串：
