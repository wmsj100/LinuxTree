---
title: JS基础类型和复杂类型
date: 2016-03-24 12:18:58
tags: [JavaScript,术语]
categories: Dynamic
---
1. 基础类型有哪些？复杂类型有哪些？有什么特征？
   - 基础类型就是5类原始数据类型，分别是：number, string, boolean, null, undefined;
     这类数据的值在栈内存中，进行复制操作时候就是值的复制，重新在栈内存中指定一个空间存储值，复制结束之后俩元素没有交集，不会互相影响。
     <!-- more -->
   - 复杂类型就是——typeof值为“object”的类型，有function , object , array 。
     这类数据的值是存放在堆内存中，而对值的引用是通过在栈内存中的指针来访问数据。当进行复制操作是，只是进行指针的复制，在栈内存中重新划分一块区域存放指针副本，俩元素指针指向的却是同一个值，所以当一个元素对值进行更改时候，这个更改会同步到另一个元素的引用状态中。是互相影响的。
     如果想消除影响，可以重新指定一个空间来存放复制的值，复制过程是深度复制，在通过遍历对象/数组时候再引入if条件进行判断，这样操作之后俩个值就是完全不想关了。
2. 写一个函数getIntv，获取从当前时间到指定日期的间隔时间；
   ```
   var str = getIntv("2016-01-08");console.log(str); 
   // 距除夕还有 20 天 15 小时 20 分 10 秒
   ```
   代码如下：
   ```
    function getIntv(str) {
        var nowTime = new Date().getTime();
        var toTime = new Date(str);
        var count = toTime / 1000 / 60 / 60 / 24 - nowTime / 1000 / 60 / 60 / 24 - 8 / 24;
        var day = parseInt(count);
        var hour = parseInt((count - day) * 24);
        var minute = parseInt(((count - day) * 24 - hour) * 60);
        var second = parseInt((((count - day) * 24 - hour) * 60 - minute) * 60)
        var result = "距除夕还有 " + day + " 天 " + hour + " 小时 " + minute + " 分 " + second + " 秒 ";
        console.log(result);
        return result;
    }
    var str = getIntv("2016-03-22");  //距除夕还有 0 天 13 小时 22 分 25 秒
   ```
3. 把上面的函数输出的数字日期改成中文日期；
   ```
   var str = getChsDate('2015-01-08');console.log(str);
   // 二零一五年一月八日
   ```
   代码如下：
   ```
   function getChsDate(str){
   var newDate=new Date(str);
   //转换为日期数值类型
   //console.log(newDate) Thu Jan 08 2015 08:00:00 GMT+0800 (ä¸­å½æ åæ¶é´)；
   var year=newDate.getFullYear();
   //读取年份；
   var month=newDate.getMonth()+1;
   //读取月份，注意月份的索引是从0开始，所以要在索引上加1；
   var date=newDate.getDate();
   //读取日；
   var result=[year,month,date];
   //把年月日赋值给result数组；
   for(var i=0;i<result.length;i++){
   result[i]=result[i].toString();
   //遍历result数值，并且把数值内部元素转换为字符串string；
   // console.log(result);//["2015", "01", "08"]
   var splitNum=result[i].split("");
   //把数值元素继续分割为数值；
   // console.log(splitNum);//["2", "0", "1", "5"]
   var j=result[i].length;
   //得到数值元素的length值；
   // console.log(j);//4,2,2
   for(var k=0;k<j;k++){
   //通过for变量元素内部的每一个数字；
   switch(splitNum[k]){
   //通过switch来替换数字为文字；
   case "0":
   splitNum[k]="零";
   break;
   case "1":
   splitNum[k]="一";
   break;
   case "2":
   splitNum[k]="二";
   break;
   case "3":
   splitNum[k]="三";
   break;
   case "4":
   splitNum[k]="四";
   break;
   case "5":
   splitNum[k]="五";
   break;
   case "6":
   splitNum[k]="六";
   break;
   case "7":
   splitNum[k]="七";
   break;
   case "8":
   splitNum[k]="八";
   break;
   case "9":
   splitNum[k]="九";
   break;
   }
   // console.log(splitNum);
   // ["二", "0", "1", "5"]
   // ["二", "零", "1", "5"]
   // ["二", "零", "一", "5"]
   // ["二", "零", "一", "五"]
   // ["一"]
   // ["八"]
   }

   // console.log(splitNum);
   // 查看改变后的数值元素
   // ["二", "零", "一", "五"]
   // ["一"]
   // ["八"]
   result[i]=splitNum.join("");
   // 把元素的数值重新合并为字符串；
   // console.log(result[i]);
   // "二零一五";
   // "一";
   // "八";
   }

   // console.log(result);
   // 查看新生成的数组
   // ["二零一五", "一", "八"]
   var output= result[0]+" 年 "+result[1]+" 月 "+result[2]+" 日 ";
   // console.log(output);
   // 最后查看输出的结果
   // 二零一五 年 一 月 八 日 
   // 满足需求，over！！！
   return output;
   }
   var str = getChsDate('2015-01-08');
   console.log(str);  // 二零一五年一月八日
   ```
4. 写一个函数获取n天前的日期:
   ```
   var lastWeek = getLastNDays(7);
   // ‘2016-01-08’var lastMonth = getLastNDays(30); //'2015-12-15'
   ```
   代码如下：
   ```
   function getLastNDays(num) {
       var nowDate = new Date().getTime();
       // console.log(nowDate);
       // 获取当前日期数值
       // 1458542349577
       var value = nowDate - (+num) * 24 * 60 * 60 * 1000;
       // console.log(value);
       // 解析输入的天数转换为毫秒数；
       // 然后从当前数值中减去天数，就是所需日期值；
       // 1426574349577；
       var year = new Date(value).getFullYear();
       // console.log(year);
       // 获取年份；
       // 2016
       var month = new Date(value).getMonth() + 1;
       // console.log(month);
       // 获取月份，并给月份值+1；
       // 3
       var day = new Date(value).getDate();
       // console.log(day);
       // 获取日
       // 14
       var result = year + " - " + month + " - " + day;
       console.log(result);
       // 输出所求值；
       // "2016 - 3 - 14"
       return result;
   }
   var lastWeek = getLastNDays(7); // "2016 - 3 - 14"
   var lastMonth = getLastNDays(30); //"2016 - 2 - 20"
   ```
5. 完善如下代码，如：
   ```
   var Runtime = (function(){
    //code here ...
    return {
        start: function(){
              //code here ...
        },
        end: function(){
             //code here ...
        },
        get: function(){
             //code here ...
        }
    };
   }());
   Runtime.start();
   //todo somethint
   Runtime.end();
   console.log(  Runtime.get() );
   ```
   代码如下：
   ```
   var Runtime = (function() {
       var startTime = 0;
       //定义开始时间；
       var endTime = 0;
       //定义结束时间；
       var passTIme = startTime - endTime;
       //计算时间间隔；
       return {
           start: function() {
               startTime = new Date().getTime();
               // console.log(startTime)
               // 1458633766980
               return startTime;
           },
           end: function() {
               endTime = new Date().getTime();
               // console.log(endTime);
               // 1458633774332
               return endTime;
           },
           get: function() {
               passTIme = "时间间隔是 " + Math.floor((endTime - startTime) / 1000) + " S"
               // console.log(passTIme);
               // 时间间隔是 7 S
               return passTIme;
           }
       };
   }());
   Runtime.start();
    //1458633891450
   Runtime.end();
    //1458633907399
   console.log(Runtime.get());
    //"时间间隔是 15 S"
   ```
6. 楼梯有200级，每次走1级或是2级，从底走到顶一共有多少种走法？用代码（递归）实现:
   ```
   function steps(totalSteps) {
    if (totalSteps === 1) {
        return 1;
    } else if (totalSteps === 2) {
        return 2;
    } else {
        return steps(totalSteps - 1) + steps(totalSteps - 2);
    }
   }
   console.log(steps(40)) //165580141
   //这是参考同学的作业，
   //看着还是不太懂，
   //还是需要多多了解一下递归；
   ```
7. 写一个json对象深拷贝的方法，json对象可以多层嵌套，值可以是字符串、数字、布尔、json对象中的任意项
   ```
    function cloneObj(obj) {
        //此处相当于var obj = a;复制了a的指针；
        var str = {};
        for (var key in obj) {
            if (typeof obj[key] === "object") {
                //判断obj元素是不是对象，
                str[key] = cloneObj(obj[key]);
                //此处复制的是cloneObj中参数obj的内部元素；
            } else {
                str[key] = obj[key];
                //如果参数不是对象，直接赋值；
            }
        }
        return str;
    }
    var a = {
        "age": 23,
        "home": [undefined, true, ["name", "wmsj"], {
            "name": "wmsj",
            "hello": "world",
            "num": [1, 2, 3]
        }]
    };
    var b = cloneObj(a);
    //Object {age: 23, home: Object}
    //b["home"][1]=false
    //此时就只有b改变了，a没有变。
   ```
8. 写一个数组深拷贝的方法，数组里的值可以是字符串、数字、布尔、数组中的任意项目:
   ```
    function cloneObj(obj) {
        //此处相当于var obj = a;复制了a的指针；
        var str = [];
        //定义一个空数组
        for (var key in obj) {
            if (typeof obj[key] === "object") {
                //判断obj元素是不是对象，
                str[key] = cloneObj(obj[key]);
                //此处复制的是cloneObj中参数obj的内部元素；
            } else {
                str[key] = obj[key];
                //如果参数不是对象，直接赋值；
            }
        }
        return str;
    }
    var a = [
        "age", 23,undefined, true, ["name", "wmsj"], {"name": "wmsj","hello": "world","num": [1, 2, 3]}];
    var b = cloneObj(a);
    //["age", 23, undefined, true, Array[2], Array[0]]
    //b[4][1]="hao"
    //此时就只有b改变了，a没有变
   ```
9. 写一个深拷贝的方法，拷贝对象以及内部嵌套的值可以是字符串、数字、布尔、数组、json对象中的任意项:
   ```
   function cloneObj(obj) {
        //此处相当于var obj = a;复制了a的指针；
        var str = {};
        //创建一个空对象，等同于str=new Object();
        if (obj instanceof Array) {
            str = [];
            //判断如果obj为数组，就创建空数组；
        }
        for (var key in obj) {
            if (typeof obj[key] === "object") {
                //判断obj元素是不是对象，
                str[key] = cloneObj(obj[key]);
                //此处复制的是cloneObj中参数obj的内部元素；
            } else {
                str[key] = obj[key];
                //如果参数不是对象，直接赋值；
            }
        }
        return str;
    }

    var a = ["name", 123, null, undefined, true, ["name", "wmsj"], {
        "name": "wmsj",
        "hello": "world",
        "num": [1, 2, 3]
    }];
    var b = cloneObj(a);
    //["name", 123, Object, undefined, true, Array[2], Object]
    //b[5][1]="hao"
    //此时就只有b改变了，a没有变。
   ```