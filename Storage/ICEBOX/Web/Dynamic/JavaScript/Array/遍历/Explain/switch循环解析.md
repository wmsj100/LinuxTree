---
title: switch循环解析
date: 2016-06-07
tags: [Book,JavaScript]
categories: Dynamic
---

- switch结构不利于代码重用，往往可以用对象形式重写。

```javascript
function getItemPricing(customer, item) {
  switch(customer.type) {
    case 'VIP':
      return item.price * item.quantity * 0.50;
    case 'Preferred':
      return item.price * item.quantity * 0.75;
    case 'Regular':
    case default:
      return item.price * item.quantity;
  }
}

//上面的case内部逻辑都是一样的，可以使用对象属性。
//如果价格档次再多一些，对象属性写法的简洁优势就更明显了。

var pricing = {
    "VIP": 0.50,
    "Preferred": 0.75,
    "Regular": 1
}

function getItemPricing(customer, item) {
    if (customer.type) {
        return item.price * item.quantity * pricing[customer.type];
    } else {
        return item.price * item.quantity;
    }
}
```