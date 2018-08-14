---
title: 数组
date: 2018-08-14 23:37:55	
modify: 
tag: [summary]
categories: Java 
author: wmsj100
mail: wmsj100@hotmail.com
---

# 数组

## 概述
- 输出矩阵1~100
- 我的代码:
	```java
	for (int i = 1; i <= 10; i++) {
		int x = (i - 1) * 10 + 1;
		for (int j = x; j < x + 10; j++) {
			System.out.printf("%5d", j);
		}
		System.out.println();
	}
	```
- 别人的代码
	```java
	int [][] nums = new int[10][10];
	int count = 0;
	for(int i=0;i<10; i++) {
		for(int j=0;j<10;j++) {
			nums[i][j] = ++count;
			System.out.printf("%5d", count);
		}
		System.out.println();
	}
	```

## 参考
- []()
