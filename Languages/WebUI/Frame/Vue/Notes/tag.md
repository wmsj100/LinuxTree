---
title: tag
date: 2020-02-15 18:38:49
modify: 
tags: [Notes]
categories: Vue
author: wmsj100
email: wmsj100@hotmail.com
---

# tag

## 概要

- 标签，自定义标签

## template

- 这个是vue定义的一个标签，可以用它来包裹DOM，然后通过在template标签上通过条件判断来执行动作
```html
<template v-if="loginType == 'user'">
	<label for="">Usernanme<input type="" placeholder="请输入用户名"></label>
</template>
<template v-else>
	<label for="">Password<input type="" placeholder="青输入邮箱"></label>
</template>
```

## 参考

