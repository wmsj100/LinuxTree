---
title: 常见错误--`input.value=""`
date: 2016-4-5 23:30:04
tags: [Error]
categories: Dynamic
---

纠结了一下午这个问题，为什么就是得不到`input`输入框的值呢，应该可以得到的呀，可是我为什么就是不行，反反复复的纠结，然后刚刚忽然意识到，变量获得`input.value`在我点击按钮之前，而我点击之后又没有重新获取`input.value`,因为再点击之前，也就是页面的初始阶段，值肯定为空的，
<!-- more -->
```javascript
    <input type="text" class="user" >
    <button class="btn">获取信息</button>
    <div class="show"></div>
    <script>
    var btn=document.querySelector(".btn");
    var show=document.querySelector(".show");
    var user = document.querySelector(".user " ).value;	//此时值肯定为空，因为没有开始输入
    console.log(user);   //空值；
    btn.addEventListener("click",function(){
    var url="02.php"+"?name="+user;
    var xhr=new XMLHttpRequest();
    xhr.onreadystatechange=function(){
    if(xhr.status===200 && xhr.readyState===4){
   		show.innerHTML=xhr.responseText;
    	}
    }
    xhr.open("get",url,true);
    xhr.send();
    	},false);
    </script>
```

这是正确的代码：

```javascript
<input type="text" class="user" >
<button class="btn">获取信息</button>
<div class="show"></div>
<script>
var btn=document.querySelector(".btn");
var show=document.querySelector(".show");
btn.addEventListener("click",function(){
	var user=document.querySelector(".user").value;
	console.log(user);
	var url="02.php"+"?name="+user;
	var xhr=new XMLHttpRequest();
	xhr.onreadystatechange=function(){
	    if(xhr.status===200 && xhr.readyState===4){
	    	show.innerHTML=xhr.responseText;
	    	}
	    }
	    xhr.open("get",url,true);
	    xhr.send();
},false);
</script>
```

