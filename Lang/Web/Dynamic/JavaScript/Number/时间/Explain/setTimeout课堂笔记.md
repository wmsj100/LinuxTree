---
title: setTimeout课堂笔记
date: 2016-3-27 19:42:29
tags: [JavaScript,时间]
categories: Dynamic
---
---
<!-- more -->
```
// for(var i=0;i<5;i++){
// (function(tags){
// 	    setTimeout(function(){
//          console.log('delayer:' + tags );

//     }, 0);
// }(i));
// console.log(i);
// }
	// for (var i = 0; i < 5; i++) {
	//     (function() {
	//         var temp = i;
	//         setTimeout(function() {
	//             console.log('delayer:' + temp);
	//         }, 1000);
	//     }());
	//     console.log(i);
	// }

// for(var i=0;i<5;i++){
//     setTimeout(function(){
//          console.log('delayer:' + i );
//     }, 1000);
//     console.log(i);
// }

//正则表达式
// var str="Visit W3School";
// var patt1=/w3school/i;
// console.log(str.match(patt1));

// var str="Is this all there is?";
// // var patt1=/is/gi;
// // console.log(str.match(patt1))


// var patt1=/e/g;
// console.log(patt1.test("The best thing"))
// console.log(patt1.exec("The best"))

// var patt2=/word/ig;
// var str="hello Word,hello WoRd";
// console.log(patt2.test(str));
// console.log(patt2.exec(str)); 
// console.log(str.match(patt2));
// console.log(str.search(patt2));
// console.log(str.replace(/word/i, "world"));
// console.log(str.replace(/word/ig, "world"));
// var str1="2 plus 3 equla 55";
// console.log(str1.match(/\d+/g));
// var str3="hello hjk   laksd        laksdjf";
// console.log(str3.split(" "));
// console.log(str3.split(/\s+/));
// console.log(str3.replace(/laksd/,"dddd"));

// console.log(/[abco]/.test("hell"));
// console.log("hello".search(/[abco]/));
// console.log("hello".match(/[abco]/));
// console.log("aak234SK5IH".match(/[a-z0-9A-Z]/g));
// console.log("aak234SK5IH".match(/[^0-9]/g));
// console.log("aak234SK5IH".match(/[A-z0-9]/g));
// console.log("hello world my name".match(/he|name/g));
// console.log("that is hot".match(/h.t/g));
// console.log("hello234_we-2+@#$%%^".match(/\w/g));
// console.log("hello234_we-2+@#$%%^".match(/[\w$]/g));
// console.log("hello234_we-2+@#$%%^".match(/\W/g));
// console.log("hello234_we-2+@#$%%^".replace(/\W/g,''));
// console.log("hello234_we-2+@#$%%^".match(/\d/g));
// console.log("hello234_we-2+@#$%%^".match(/\d/g).length>-1);
// console.log("hello234_we-2+@#$%%^".search(/\d/g)>-1);

// console.log("h34_we-2+@%%^".match(/\D/g));

// console.log("h 3   4_    we-2+    @% %^".replace(/\s/g,""));
// console.log("h 3   4_    we-2+    @% %^".split(/\s+/g));

// console.log("h 3   4_    we-2+    @% %^".match(/\S/g));

// console.log("hello worlld my home".match(/\bhel/g))
// console.log("hello worlld my homelld".match(/lld\b/g))
// console.log("hello wohellorlld myhello home".match(/\bhello\b/g))
// console.log("hello wohellorlld my hello home".match(/\shello\s/g))
// console.log("hello wohellorlld my hello home".match(/hello\s/g))

// console.log("hello hhello hhhheoo h".match(/h/g))
// console.log("hello hhello hhhheoo h".match(/h+/g))
	
// console.log("1234 weoirj 234".match(/\d/g));
// console.log("1234 weoirj 234".match(/\d+/g));
// console.log("1234 weoirj 234".match(/[0-9]+/g));

// console.log("a ab abb aab ablskd34abbbbsf344".match(/ab+/g));
// console.log("a ab abb aab ablskd34abbbbsf344".match(/ab*/g));
// console.log("a ab abb aab ablskd34abbbbsf344".match(/ab?/g));
// console.log("100,1000,21000001000".match(/\d{3}/g))
// console.log("100,1000,21000001000".match(/\d{3,4}/g))
// console.log("100,1000,21000001000,12".match(/\d{3,}/g))
// console.log("100,1000,21000001000,12".match(/\d{,4}/g))

// console.log("hellold worlds".match(/ld$/g))
// console.log("hellold world".match(/ld$/g))

// console.log("ldld".match(/^ld$/g))
// console.log("ld".match(/^ld$/g))

// console.log("13111111111".match(/1[3456789]\d{9}/));
// console.log(/^1[3456789]\d{9}$/.test("10934148993"))
// 6,10.
// 
// 
// 
// console.log(/^\w{6,10}$/.test("hedsss"));

console.log(/\S+@\S+\.\S+/.test("wmsj@d.co m"))
```

