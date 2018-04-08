---
title: 匹配对象元素的数组值
date: 2016-03-24 12:18:58
tags: [函数,封装]
categories: Dynamic
---

<!-- more -->
```
        var obj = {
            className: 'open menu'
        }

        function addClass(data, str) {
            for (var i in data) {
                if (data[i].split(" ").indexOf(str) === -1) {
                    var p = data[i].split(" ");
                    p.push(str);
                    data[i] = p.join(' ')
                    return data[i];
                } else {
                    p = data[i];
                    return data[i];
                }
            }
        }
        console.log(addClass(obj, "new"));
        console.log(addClass(obj, "open"));
        console.log(addClass(obj, "me"));
        console.log(obj.className);

        function removeClass(data, str) {
            for (var i in data) {
                var cat = data[i].split(" ")
                if (cat.indexOf(str) > -1) {
                    var dog = cat.filter(function(e) {
                        return e !== str;
                    });
                    data[i] = dog.join(" ");
                    return data[i];
                } else {
                    return data[i];
                }
            }
        }
        console.log(removeClass(obj, 'open')) // obj.className='menu new me'
         console.log(removeClass(obj, 'balaba'))
         ```
