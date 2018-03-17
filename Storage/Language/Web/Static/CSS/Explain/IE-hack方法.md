---
title: IE hack方法
date: 2016-03-24 12:18:58
tags: [浏览器]
categories: Static
---
### 问题
1. 如何调试IE浏览器
- 可以通过高版本的IE开发者工具选择低版本的渲染模式，这样也可以模拟相应IE版本对页面的渲染结果：
  <!-- more -->
  ![IE版本切换](http://upload-images.jianshu.io/upload_images/1606281-76f9426f8420578f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 因为IE6是没有开发者工具的，所以调试这个版本的IE只能通过虚拟机安装XP系统，然后在IE页面上进行调试；
- 也可以通过其他的IE模拟器来进行调试，但如果条件允许的话还是不建议在这上面进行调试，因为会出现很多意想不到的事情发生，但因为我的电脑配置实在是无法在支撑一个虚拟机的运行，所以只能在这上面进行IE的调试：
  ![IETester](http://upload-images.jianshu.io/upload_images/1606281-a51570aad842ef30.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
1. 什么是CSS hack？在CSS和HTML里如何写hack？在CSS中IE6、7的hack方式？
- CSS hack——由于不同的浏览器，甚至是同一个浏览器的不同版本对CSS的解析认识不一样，导致生成的页面效果不一致，写出针对不同浏览器CSS code就称为CSS hack；
- 常用的CSS hack有三种方式，CSS内部的hack、选择器hack、HTML头部引用hack，其中第一种最常用。
- CSS hack写法有以下几种情形：
  - 在所引用的属性前面加上特定的前缀以表示支持某个特定浏览器。
```
-webkit-transform: rotate;	/* webkit内核浏览器 */
	-moz-transform: rotate;		/* Mozilla内核浏览器 */
	-ms-transform: rotate;		/* IE内核浏览器 */
	-o-transform: rotate;		/* Opera内核浏览器 */
	transform: rotate;			/* W3C标准 */
```
    - 在属性前面加特定符号来针对IE浏览器的不同版本hack，
> 1. ” * “——只有IE6、7浏览器可以识别;
> 2. " + "——只有IE7浏览器可以识别；
> 3. " - "——只有IE6浏览器可以识别；
> 4. " \9 "——IE6～IE10版本都可以识别；
> 5. " \0 "——IE8～IE10版本可以识别；
> 6. " \9\0 "——IE9和IE10版本可以识别；
>    ![IE浏览器CSShack](http://upload-images.jianshu.io/upload_images/1606281-11d2011d704d0d00.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- HTML hack方法——指的是在HTML头部添加类似于程序语句，只能在HTML文件里使用，并且只有在IE浏览器才能执行，这个代码在非IE浏览器下不能执行该条件下的定义，只会被当作是注释条件而被忽略。
```
<!– 默认先调用css.css样式表 –>
<link rel="stylesheet" type="text/css" href="css.css" />
<!–[if IE 7]>
<!– 如果IE浏览器版是7,调用ie7.css样式表 –>
<link rel="stylesheet" type="text/css" href="ie7.css" />
<![endif]–>
<!–[if lte IE 6]>
<!– 如果IE浏览器版本小于等于6,调用ie.css样式表 –>
<link rel="stylesheet" type="text/css" href="ie.css" />
<![endif]–>
```
> lte——Less than or equal to的简写，小于等于的意思；
> lt——LEss than的简写，小于的意思；
> gte——Greater than or equal to的简写，大于等于的意思；
> gt——Greater than简写，也就是大于的意思；
> ！——就是不等于的意思。
- hack语句的顺序排列遵循的规律：先一般，再特殊，因为特殊的语句会覆盖一般的语句。
  参考文献——[CSS hack](http://www.cnblogs.com/dolphinX/p/3292630.html#undefined)
1. 列举几种浏览器兼容问题：
- 不同浏览器的标签默认的外补丁和内补丁不同；
  - 比如各自版本的标签margin和padding差异较大
  - 不同浏览器的默认控件样式差异较大，例如button按钮、table表格、form表单里面的单选和多选样式，input输入框的样式等，差异较大；
- 不同浏览器对于同样的CSS和HTML标签的支持程度不一致，新标准里面的标签和属性在老版本浏览器里面不支持，比如对于display：inline-block，IE6、7就不支持，无法使块级元素转换为行内元素，需要进行相应的hack方法。
- 即便是现代浏览器，对于标准的支持程度、外观表现和理解也不一致，比如fieldset这个属性IE11就不支持，但是chrome和oprea是支持的。
- 说到的兼容性问题其实最多的还是和IE各版本之间差异性，比如display：inline-block，IE6、7完全不认识，只能通过其他hack方式解决。
1. 针对兼容、多浏览器覆盖有什么看法？渐进增强和优雅降级是什么意思？
- 说到兼容和多浏览器覆盖，首先要针对项目本身进行调研，查看目标人群使用的浏览器情况，一般情况对于使用人群小于5%的就可以忽略了，因为所谓的兼容和覆盖全部浏览器这本身就是不现实和，而且涉及到时间和成本的问题，还有一些暂时无法解决的兼容性bug等，这些都需要综合考虑。
- 渐进增强——针对低版本浏览器进行构建页面，保证最基本的功能，然后再针对高级浏览器进行效果、交互等改进和追加功能达到更好的用户体验，这个观点更受大公司的欢迎。
- 优雅降级——一开始就构建完整的功能，然后再针对低版本浏览器进行兼容。
- 区别——优雅降级是从复杂的现在开始，并试图减少用户体验的供给，而渐进增强则是从一个非常基础的，能够起作用的版本开始，并不断扩充，以适应未来环境的需要。降级意味着往回看（功能衰减）；而渐进增强意味着朝前看，同时保证根基处于安全地带。
> 参考文献——[沫鱼的前端世界](http://www.cnblogs.com/mofish/p/3822879.html)
1. reset.css和normalize.css分别是做什么的？为什么推荐使用normalize.css？
- Normalize.css——只是一个很小的CSS文件，但它在默认的HTML元素样式上提供了跨浏览器的高度一致性。相比于传统的CSS reset，Normalize.css是一种现代化的、为HTML5准备的优质替代方案。
- reset通常为几乎所有的元素施加默认样式，强行使得元素有相同的视觉效果。相比之下，Normalize.css保持了许多默认样式的浏览器样式。这就意味着你不用再为所有公共的排版元素重新设置样式。当一个元素在不同浏览器中有不同默认样式时，Normalize.css会力求让这些样式保持一致并尽可能与现代标准符合。
- Normalize.css修复了常见的桌面端和移动端浏览器的bug，这往往超出了reset所能做到的范畴。关于这一点，Normalize.css修复的问题包含了HTML5元素的显示设置、与格式化文字的fontsize问题、在IE9中SVG的溢出、许多出现在各浏览器和操作系统中的与表单相关的bug。
- Normalize.css不会让调试工具变得杂乱。而使用reset最让人困扰的地方莫过于在浏览器调试工具中大段大段的继承链。
- Normalize.css是模块化的，它已经被拆分为多个相关却又独立的部分，这使得你能够很容易也很清楚地知道哪些元素被设置了特殊的值。因此这能让你选择性的移除某些永远也用不到的部分。
- Normalize.css拥有详细的文档，它的代码基于详细而全面的跨浏览器研究与测试。这个文件拥有详细的代码说明并在Github Wiki中有进一步的说明。这意味着你可以找到每一行代码具体完成了什么工作、为什么写这句代码、浏览器之间的差异，并且你可以更容易的进行自己的测试。
- #### 无论从适用范畴还是实施上，Normalize.css与Reset都有着极大的不同。Normalize.css是一种CSS reset的替代方案。
> 参考文献——[Normalize.Css介绍和使用，Normalize与CSS Reset的区别](http://www.yxxme.com/1034.html)
> github——[normalize.css](https://github.com/necolas/normalize.css)

### 操作
1. 安装VirtualBox，下载安装虚拟机
- 我的电脑是奔腾P6200的处理器，不打算去尝试装这个虚拟机了，因为我知道它肯定得歇菜，当然了这个虚拟机我玩ubantu的时候用过，基础的操作会使用。
1. 在IE6、7、8中展示盒模型inline-block、max-width的区别。
   [代码](http://s.codepen.io/wmsj100/debug/oxjyeL)
   可以看到IE6对于俩个属性都不支持：
   ![IE6盒模型](http://upload-images.jianshu.io/upload_images/1606281-fccfb0baf15642d5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
   IE7支持max-width属性，但是对于inline-bloxk属性不支持：
   ![IE7盒模型](http://upload-images.jianshu.io/upload_images/1606281-1a19d6c79754403c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
   IE8对于俩个属性都有很好的支持：
   ![IE8盒模型](http://upload-images.jianshu.io/upload_images/1606281-06d216d8e7cd67ab.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
