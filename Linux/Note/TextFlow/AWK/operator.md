---
title: 运算符
date: 2018-03-12 22:53:28 Mon
tag: [awk]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

# awk运算符

## 运算符分类
- 所有的运算符可以分为算术运算符，逻辑运算符，赋值运算符，关系运算符，正则运算符
- ~ 匹配正则表达式

### 范例
- awk赋值运算符
	- awk 'BEGIN{a=1;print a+=5}' // 6
- awk逻辑运算符
	- awk 'BEGIN{a=1;b=2;print (a>5 && b<2), (a>5 || b<=2)}' // 0 1
	- awk 'BEGIN{a=1;b=2}{print (a>5 && b<2), (a>5 || b<=2)}' // 0 1
- awk正则表达式
	- awk 'BEGIN{a="100Test";if(a ~ /^100*/) {print "ok"}}'
	- awk -v name="$name" 'BEGIN{if(name ~ /^wmsj*/){print "ok"}}'
- awk关系运算符
	- awk 'BEGIN{a=11;if(a>=9){print "ok"}}'
- awk算术运算符
	- awk 'BEGIN{a=9;print a++,++a;}' // 9 11
- awk in 判断变量是否是数组的key值
	- awk 'BEGIN{a="b";arr[0]="b";arr["b"]="c";print(a in arr)}' // 1
