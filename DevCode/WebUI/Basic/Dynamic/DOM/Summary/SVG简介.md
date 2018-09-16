---
title: JavaScript 的新领域 - 动态图片处理（SVG）
date: 2016-05-30
tags: [SVG,DOM]
categories: Dynamic
---

https://www.ibm.com/developerworks/cn/web/1107_pangjun_svgcanvas1/
背景

当 JavaScript 被 Netscape 公司发明出来时，它被用来做一些琐细的事情，比如校验表单、计算日期、提示用户；随着 Web 的迅速发展，这种轻巧而灵活的语言被委以越来越多的任务，动态地修改页面内容，一致地处理事件，甚至无刷新地和服务器交互。然而，与传统的客户端编程相比，JavaScript 操作的对象限制在 DOM 模型之内，无法进行图形编程。所以长久以来，我们在设计网页时都仅仅是在“搭积木”，而且这些积木只有一种形状——长方形。这些长方形的积木就是应用在 HTML 元素上的“盒子”模型（box model）。每个盒子有边框 （border），边缘（margin）和填充（padding）。我们只能控制这些盒子的大小和有限的样式。这些方块的集合对于构建一个传统的文档页面已经足够了。但是 Web 的流行已经使网页承担的任务远远超出了传递文字信息。哪里有流行，哪里就有需求，哪里也就有创新。网页的美工设计已经使静态页面的美观程度丝毫不逊色于传统的客户端程序的界面。而创造更加互动的用户界面更是使在页面上创建和修改图片的可能十分吸引人。于是，两种技术应运而生，使得 JavaScript 的功能扩展到图形领域。

数字化图片的两种方案

在介绍这两种技术之前，我们先来看看图片的数字化。将图片存储为数据有两种方案。其一为位图，也被称为光栅图。即是以自然的光学的眼光将图片看成在平面上密集排布的点的集合。每个点发出的光有独立的频率和强度，反映在视觉上，就是颜色和亮度。这些信息有不同的编码方案，在互联网上最常见的就是 RGB。根据需要，编码后的信息可以有不同的位 (bit) 数——位深。位数越高，颜色越清晰，对比度越高；占用的空间也越大。另一项决定位图的精细度的是其中点的数量。一个位图文件就是所有构成其的点的数据的集合，它的大小自然就等于点数乘以位深。位图格式是一个庞大的家族，包括常见的 JPEG/JPG, GIF, TIFF, PNG, BMP。

第二种方案为矢量图。它用抽象的视角看待图形，记录其中展示的模式而不是各个点的原始数据。它将图片看成各个“对象”的组合，用曲线记录对象的轮廓，用某种颜色的模式描述对象内部的图案（如用梯度描述渐变色）。比如一张留影，被看成各个人物和背景中各种景物的组合。这种更高级的视角，正是人类看世界时在意识里的反映。矢量图格式有 CGM, SVG, AI (Adobe Illustrator), CDR (CorelDRAW), PDF, SWF, VML 等等。

矢量图中简单的几何图形，只需要几个特征数值，就可以确定。比如三角形，只需要确定三个顶点的坐标。圆只需要确定圆心的坐标和半径。描述它的函数已知的曲线也只需要几个参数就能够确定。如正弦曲线、各种螺线等等。如果用位图记录这些几何图案，则需要包含组成线条的各个像素的数据。除了大大节省空间，矢量图还具有完美的伸缩性。因为记录的是图形的特征，图形的尺寸任意变化时，都只是做着相似变换，不会出现模糊和失真。相反位图的图片放大到超出原有大小时，各个像素点之间出现空缺，即使用某种算法填充，也会出现模糊锯齿等现象，不如矢量图精确。因而矢量图很适合用于记录诸如符号、图标等简单的图形。而位图则适合于没有明显规律的、颜色丰富细腻的图片。

两种技术

现在我们回到 Web 上的画图上。对应于图片数字化的两种方案，各有一种技术。我们按照它们产生的时间顺序来说。这篇文章中，笔者会介绍第一种—— SVG。

SVG

第一种技术来自 XML 家族，叫做 SVG(Scalabe Vetor Graphics) - 可缩放矢量图。作为一种通用的数据格式，XML 自诞生之日起，就不断表现出表达一切可表达之物的抱负，不仅要接纳新出现的各种信息，还要接收历史上以其他各种形式存储的数据。其扩张版图的雄心，不亚于任何一位野心勃勃的君主。

XML 适合于描述结构化的数据，所以你可能猜到了，如它的名字所示，SVG 选择的视角是矢量图。实际上，SVG 远不是第一种用 XML 描述图片的格式，甚至也不是第一种在 Web 上提出的 XML 与矢量图的组合的标准。在它之前的 1998 年，Macromedia 和 Microsoft 向 W3C 提交了 VML(Vector Markup Language)，Adobe 和 Sun 提交了 PGML(Precision Graphics Markup Language)，这两种都是基于 XML 的矢量图规范。随后，不希望互联网上的矢量图片标准被这些巨头垄断的其他公司在 W3C 内成立了一个专门小组 SVG Working Group，在借鉴了前两种提案后，提出了 SVG 规范，随后被接纳为相当于标准的 W3C 推荐（W3C Recommendation）。以下是迄今为止 SVG 的主要发展历程：

2001-9SVG 1.0 成为 W3C 推荐。

2003-1SVG 1.1 成为 W3C 推荐。并演化出 SVG Tiny，SVG Basic 和 SVG Full 不同级别的细则。

SVG 1.2 在之后的几年中一直处于工作草稿（W3C Working Draft）的状态，现已确定会被 SVG 2.0 取代。

SVG 2.0 将会完全重写 SVG 1.2，以加入更多诸如 CSS，HTML5 的新特性。

第一个简单的例子

下面是一个很简单的矢量图的定义。SVG 中各种元素和属性的详细说明可以在专门的参考中找到。本文中会在例子中对一些重要的元素和属性做说明。
清单 1. 一个 SVG 文件

 <?xml version="1.0" standalone="no"?> 
 <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" 
 "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd"> 
 <svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="100%" height="100%" > 
 <circle cx="100" cy="100" r="40" fill="red"/> 
 </svg>

第一行的 XML 指令定义版本，并说明此文件引用到其他文件。第二行是文档类型定义，规定此 XML 中哪些是有效的 SVG 元素。这里引用的 http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd 正是第一行中 standalone 属性为 no 的原因。第三行开始是 SVG 的真正定义。circle 元素指定画一个圆。cx、cy 和 r 属性分别指定圆心的横坐标、纵坐标和半径。fill 属性指定用红色填充此圆内部的区域。

画图比看图容易

将这段“文本”粘贴进任何一个文本编辑器，然后将文件保存为一个 SVG 文件，如 sun.svg。你就已经画完了一幅图——一个红红的太阳。但是想要看它却不那么容易。需要用一些专业的绘图软件，比如 Adobe Illustrator，CorelDRAW 和 GIMP 才能显示这个图片。你的电脑上已经有的 Windows 画图、ACDSee 都不支持这种格式。这是可以理解的，因为 SVG 是作为互联网上图片的一种标准。所以接下来看看怎样在浏览器中显示它——不幸的是，这仍然不像打开一幅 JPG 或者 GIF 那么简单。

各种浏览器对 SVG 的支持不一。总的说来，现在仍旧占据最大市场份额的 IE 不支持，其他主流浏览器，包括现在市场份额第二的 Firefox 以及 Chrome、Safari 和 Opera 都对 SVG 标准有不同程度的支持。IE6、7、8 对 SVG 都没有原生的支持，需要专门的插件（如 Adobe SVG Viewer）才能显示。目前还处于技术预览版的 IE9 将会支持。考虑到 IE 曾经占据的垄断性地位和微软有自身的竞争性的 VML 技术，这种“落后”并不奇怪。

不过这种情况，在发展迅速的浏览器市场瞬息万变。所以最好试试看您使用的浏览器支持下列哪种显示方法。

    使用 <img> 标签。

    <img src= 'sun.svg' >
    将 SVG 与传统的互联网图片格式同等使用（现在只有 Chrome、Safari 和 Opera 支持）。
    使用 <embed> 标签。

    <embed src="sun.svg" width="300" height="100"
    type="image/svg+xml"
    pluginspage="http://www.adobe.com/svg/viewer/install/" />
    pluginspage 属性的值是 Adobe 公司为不原生支持 SVG 的浏览器开发的插件 Adobe SVG Viewer 的安装地址。2009 年 1 月 1 日 Adobe 已经终止对该产品的支持。
    使用 <object> 标签。

     <object data="sun.svg" width="300" height="100"
     type="image/svg+xml"
     codebase="http://www.adobe.com/svg/viewer/install/" />

    使用 <iframe> 标签。

     <iframe src="sun.svg" width="300" height="100" border="0" style="border-width:0"> 
     </iframe>

下面是一个测试浏览器对 html 中各种使用 SVG 的方式是否支持的页面代码。sun.svg 文件与该页面保存于同一目录。
清单 2. 测试浏览器对 SVG 的支持

 <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"> 
 <HTML> 
 <HEAD> 
  <TITLE> SVG in HTML </TITLE> 
 </HEAD> 

 <BODY> 
 1. 使用 &lt;img&gt; 标签
 <br> 
 <img src="sun.svg" width="300" height="100"> 
 <br> 
 2. 使用 &lt;embed&gt; 标签
 <br> 
 <embed src="sun.svg" width="300" height="100"
 type="image/svg+xml"
 pluginspage="http://www.adobe.com/svg/viewer/install/" /> 
 <br> 
 3. 使用 &lt;object&gt; 标签
 <br> 
 <object data="sun.svg" width="300" height="100"
 type="image/svg+xml"
 codebase="http://www.adobe.com/svg/viewer/install/" /> 
 <br> 
 4. 使用 &lt;iframe&gt; 标签
 <br> 
 <iframe src="sun.svg" width="300" height="100" border="0" style="border-width:0"> 
 </iframe> 
 </BODY> 
 </HTML>

动态功能

如果仅仅是将 SVG 作为图片引用，则只发挥了它的静态功能。我们更感兴趣的是应用它的动态功能。SVG 的动态功能包括两个方面。一为动画，二为支持脚本编程。

动画

SVG 在设计时就加入了对动画的支持。这是通过另一种 W3C 颁布的动画语言 SIML(Synchronized Multimedia Integration Language) 实现的。SIML 被应用时，与 SVG 结合得非常紧密。它与 SVG 一样，是一种声明性（declarative）的标记语言，通过元素（element）和属性（attribute）来定义动画的行为。这里只给出一个简单的例子，不做详细介绍。因为浏览器对它的支持还很有限；另外它声明性的本质也使表现力受到限制，不如使用脚本自定义动画灵活。
清单 3. 用 SIML 实现的动画

 <?xml version="1.0" standalone="no"?> 
 <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" 
 "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd"> 
 <svg xmlns="http://www.w3.org/2000/svg"> 
    <polygon points="50,100  100,100  75,50" stroke="#660000" fill="#cc3333"> 
         <animateTransform 
            attributeName="transform"
            begin="0s"
            dur="10s"
            type="rotate"
            from="0 0 0"
            to="360 60 60"
            repeatCount="indefinite" 
        /> 
     </polygon> 
 </svg>

polygon 元素指定画一个多变形，这里给定了三个顶点，所以是一个三角形。将上面的代码保存成一个 SVG 文件，在一个页面中引用，如果您的浏览器支持 SIML，屏幕上会显示一个不断旋转的红色三角形；如果您的浏览器只支持 SVG，将看到一个静止的红色三角形。

脚本可编程性

SVG 是一个 XML 文件，用于 XML 编程的两种模型 DOM 和 SAX 也适用于它。因为 SVG 是被设计用于互联网，所以通过 JavaScript 和 DOM 访问它就是最重要的应用模式。我们已经熟悉通过 JavaScript 和 DOM 动态地修改 HTML，同样我们也可以在浏览器中动态地创建、修改和删除图片，这也将是本文之后在 SVG 方面的重点。

为了演示这些动态功能，我们采取和上面不同的在页面中使用 SVG 的方式——在 XHTML（XML 的 XML 版本）直接写入 SVG 的源文本，而上面的四种方式 SVG 的定义都保存在和页面不同的另一个文件中。这样做有两个原因。一是在支持 XHTML 和 SVG 在浏览器中，可以通过 JavaScript 直接访问和修改 SVG。二是在互联网的未来标准 HTML 5 中，SVG 就可以这样直接在 HTML 中定义，就像其他 HTML 元素一样。

之后的几个例子都可以在 Firefox 中运行，但无法使用 IE。因为要到版本 9，IE 才会加入对 XHTML 的支持（目前的 IE 只支持将 XHTML 作为 HTML 解释），再次显示了拥抱公开标准的迟缓。

我们的第一个例子是一个进度条。在 Firefox 中载入下面的 XHTML 页面，会显示一个绿色的运动的进度条。