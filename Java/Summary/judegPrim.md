---
title: 判断素数
date: 2018-08-14 22:46:31	
modify: 
tag: [skill]
categories: Summary 
author: wmsj100
mail: wmsj100@hotmail.com
---

# 判断素数

## 概述
- 如何判断一个数是素数呢
- 我的写法

	```java
	for (int i = 2; i < 313; i++) {
		if (313 % i == 0) {
			System.out.println("not");
		}

	}
	```
- 别人的写法
	```java
	public class JudgePrime {
		public static void main(String[] args){
			int a = 4549;
			boolean result = true;      
			for (int i=2; i*i <= a; i++) { 
				if (a % i == 0) {  //a依次除以从2到a开方后的数（a能整除5，就一定能整除（a/5））
					result = false;
					break;
				}
			}
			if (result) {
				System.out.println(a+"是素数");
			}
			else
			  System.out.println(a+"不是素数");
		}
	}
	```

## 参考
- [实验楼](https://www.shiyanlou.com/courses/running)
