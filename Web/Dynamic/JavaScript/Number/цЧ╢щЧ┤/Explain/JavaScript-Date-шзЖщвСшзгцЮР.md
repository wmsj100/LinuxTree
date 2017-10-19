---
title: JavaScript-Date-视频解析
date: 2016-03-24 12:18:58
tags: [JavaScript,时间]
categories: Dynamic
---
1. date的方法：
   - Date.now()——获取当前时间的毫秒数；
   - Date()——输出当前日期，并且通过系统自带的toString方法转换为字符串形式——"Sun Mar 20 2016 13:02:58 GMT+0800 (ä¸­å½æ åæ¶é´)"
   - new Date().getFullYear()——通过这种方式可以获取到年份；
     <!-- more -->
2. 注意事项：
   1. 在给变量赋值date函数时候，首先要声明变量为日期函数：
      ```    
      var a = new Date();
      a.getFullYear()    //2016;
      ```
   2. 可以通过在函数前后分别获取当前时间来计算函数的用时；
      ```
      var a1=Date.now();
      for(var i=0;i<10000;i++){
      console.log("hello world");}
      var a2=Date.now();
      console.log(a2-a1);
      10000 hello world
      2097
      ```
      可以看到运行10000次用了2S。
   3. 可以通过计算获取几天/年/月前的时间；
      var a2=new Date(Date.now()-365*24*60*60*1000);
      console.log(a2)   //这样就可以输出字符串形式的日期.

3. date——[查看date详情](http://www.w3school.com.cn/jsref/jsref_obj_date.asp);
4. 如何设置一个时间点；
   - 可以通过Date.parse（“2014”）把毫秒数赋值给一个变量，
     var b=Date.parse("2015-10-25,12:23:34")
     //1445747014000;
     这段时间为指定时间点的毫秒数；
   - 可以通过new.date(毫秒数)来创建一个时间对象。