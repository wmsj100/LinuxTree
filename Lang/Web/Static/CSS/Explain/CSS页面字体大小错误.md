---
title: CSS页面字体大小错误
date: 2016-03-24 12:18:58
tags: [CSS]
categories: Static
---
我设置的文字大小误差。块级元素里面的文本必须放到行内元素的标签里面，这样文本大小才不会出现错误。
<!-- more -->
```
span{
		font-size: 18px;
	}
 <p>
    	<span>html</span>
    </p>
```
![font-size=18px](http://upload-images.jianshu.io/upload_images/1606281-05ace3fefe220edd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```
p{
		font-size: 18px;
         padding: 0;
		margin: 0;
	}
<p>
    	html
    </p>
```

![font-size=21px](http://upload-images.jianshu.io/upload_images/1606281-9c27d6aa538051f2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
此时即便我把p的padding和margin设置为0，也不行，所以文字要放入文本标签内部。
