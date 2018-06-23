---
title: basic
date: 2018-05-08 23:44:10 Tue
modify: 2018-05-08 23:44:10 Tue
tag: [basic]
categories: TypeScript
author: wmsj100
mail: wmsj100@hotmail.com
---

# 基础知识

## 概述
- npm install typescript -g
- tsc greeter.ts 在命令行执行这个命令会在当前目录生成一个同名的.js文件

## 范例
```ts
class Student{
    fullName: string;
    constructor(public firstName, public middleInitial, public lastName){
        this.fullName = firstName + " " + middleInitial + " " + lastName;
    }
}
interface Person {
    firstName: string;
    lastName: string;
}
function greeter(person: Person){
    return "Hello, " + person.firstName + " " + person.lastName;
    }


    let user = new Student("Jane", "m", "User");
    document.body.innerHTML = greeter(user);
```
