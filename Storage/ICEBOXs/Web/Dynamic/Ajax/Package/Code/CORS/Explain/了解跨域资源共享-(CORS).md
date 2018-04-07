---
title: 了解跨域资源共享 (CORS)
date: 2016-04-27
tags: [跨域,浏览器,GitHub]
categories: Blog
---

[http://www.adobe.com/cn/devnet/html5/articles/understanding-cross-origin-resource-sharing-cors.html](http://www.adobe.com/cn/devnet/html5/articles/understanding-cross-origin-resource-sharing-cors.html)

对 JavaScript 和 Ajax 具有基本了解有助于理解本文，但这并不是必需的.

- CORS (跨域资源共享)
  - [了解更多](http://en.wikipedia.org/wiki/Cross-origin_resource_sharing)
- GITHub API
  - [下载并了解更多](http://developer.github.com/v3/)

### 							用户级别

全部

[CORS](http://en.wikipedia.org/wiki/Cross-origin_resource_sharing)代表跨域资源共享，是 HTML5 的一项特性，它允许一个站点访问不同域名下另一个站点的资源。 我将在下文进行详细介绍。 在 CORS 出现之前，人们采用一种名为 Same-Origin Policy（同源策略）的 Web 浏览器安全限制来防止 Web 应用程序调用外部 API。 只有在两个来源使用同一协议（http 和 https）、同一端口及同一域（甚至不同的子域都会导致失败）时，浏览器才会将这两种资源视为同源。

在 CORS 出现之前，您可以通过创建某种形式的服务器端组件传送 API 请求来绕过这个常常过度复杂并且不必要的安全限制。 您也可以在支持 [JSONP](http://json-p.org/) （带填充的 JSON）的 API 中使用 JSONP，但大部分不支持这种做法，并且即使支持，JSONP 也仅限于 GET 请求。

有了 CORS 之后，我在一个域的应用程序就可以自由地与您另一个域上的 API 通信，甚至是使用`POST`、`PUT`和 `DELETE`，前提是您的 API 安全限制指定支持这些做法，并且您已经通过 CORS 规范建立了通信。 这就意味着您可以消除使用服务端组件的需求，并利用 JavaScript 在客户端开展所有 API 通信。

在本文中，您将通过一个简单的代码示例来了解 CORS 规范，即如何启用它，如何在特定的浏览器中使用它，以及如何利用 JSON 对其进行简化等等，这个代码能利用 GET 方法从其他域上的 API 检索信息。

###                 CORS 服务器端设置 

本文的重点是利用 CORS 进行客户端通信，但我们首先来快速浏览一下可用来理解 CORS 客户端设置的资源。 这些设置都是通过浏览器翻译的 response 头文件来确定的。

[CORS 的 W3C 规范](http://www.w3.org/TR/cors/)实际上做得非常好，它提供了一些简单的 response 头文件示例，比如 key 头文件、`Access-Control-Allow-Origin，`以及其他启动 Web 服务器上的 CORS 所必需的头文件。 可以理解这个规范并没有详细介绍任何特定的 Web 服务器（比如 IIS、Apache 等等）。它还讨论了 ”预检请求“ 的概念， 它必须用在诸如 `PUT` 或`DELETE`此类非 ”简单方法“（简单方法专门定义为 `GET`、 `HEAD`和 `POST`）的请求上。

在提供一些有关跨域请求的 [安全建议](http://www.w3.org/TR/cors/#security)后，规范中的[ 语法 ](http://www.w3.org/TR/cors/#syntax)部分将详细介绍您可以在服务器上指定的各种类型的头文件，包括每个头文件的作用。 还有各种各样能确保您优化安全性的头文件，比如` Access-Control-Allow-Credentials` 头文件，如果启用，它将允许您共享像 cookie 和 HTTP 身份验证信息这类内容。 另一个示例是 `Access-Control-Max-Age `头文件，它指定了缓存一个非简单方法请求的预检请求所需的时间。

如果您正在寻找有关如何在各种常见的 Web 服务器上建立 CORS 的具体信息，请查看 [支持 CORS 共享](http://enable-cors.org/) 网站。 网站解释了如何在各种 Web 服务器（从 Apache到 IIS 再到 ExpressJS和其他服务器）上建立`Access-Control-Allow-Origin` response 头文件。 但并未详细介绍如何建立其他 response 头文件或如何处理预检请求。

最后，我推荐大家阅读Monsur Hossain编写的一个优秀的[CORS 使用](http://www.html5rocks.com/en/tutorials/cors/)教程，在[HTML5 Rocks](http://www.html5rocks.com/) 网站上可以找到该教程。 虽然主要着眼于客户端通信，但 Monsur 浏览了各种各样的 response 头文件类型以及如何处理像`PUT `或` DELETE` 这样的复杂请求。 本教程并不是针对任何 Web 服务器，但结合 enable-cors.org中提供的说明应当能够正常启动和运行。

###                 浏览器支持

为了检查浏览器支持情况，我构建了一个简单的示例，用于从跨域 API 执行基本 GET。 尽管 CORS 的浏览器支持面已经相当广泛，并且有越来越多的 API 支持 CORS，但仍有很多API 不支持 CORS。 不久，GitHub API也将支持CORS。 在下面的示例中，我将使用`GET` 请求调用 GitHub API 并基于 "Javascript" 关键字来检索一系列资源库，然后利用结果填充页面。

​        `   CORS Example   function onloadHandler() {      var xhr = new XMLHttpRequest();      xhr.open('GET', 'https://api.github.com/legacy/repos/search/javascript', true);      // Response handlers.      xhr.onload = function () {         var repos = JSON.parse(xhr.response), i, reposHTML = "";         for (i = 0; i < repos.repositories.length; i++) {            reposHTML += "<p><a href='" + repos.repositories[i].url                         + "'>" + repos.repositories[i].name + "</a><br>"                         + repos.repositories[i].description + "</p>";         }         document.getElementById("allRepos").innerHTML = reposHTML;      };         xhr.onerror = function () {         alert('error making the request.');      };         xhr.send();   }   `    

**注意：** 这是我为了方便说明而创建的一个简单示例， 并且故意没有使用任何框架。

这个 `onLoadHandler()` 函数创建了一个 `XMLHttpRequest`， 并通过`GET`请求将它打开到  GitHub API URL。` Open` 方法的第三个参数设置为` true`，并将该请求指定为异步。

接下来，代码片段要为请求创建事件处理程序。 我们只处理 `onload` 和 `onerror ` 事件，但还有很多其他事件使用  CORS，包括`onloadstart`、`onprogress`、`onabort`、`ontimeout` 和`onloadend` 事件。 在这个代码片段的 `onload` 方法中，我解析了 JSON 响应并将几个非常简单的 HTML 填入`div`标签。 在您为 CORS 请求启动 GitHub API，利用代码来创建这些事件处理程序并发送请求后，将不会再遇到安全问题。

#### Chrome、FireFox、Opera 和 Safari 浏览器

从版本 3（这似乎是很久以前了）开始，Chrome 已经通过 XMLHttpRequest level 2 来支持 CORS  了。 在本教程中，您可以了解更多[有关 XMLHttpRequest2 的新技巧](http://www.html5rocks.com/en/tutorials/file/xhr2/)（由  Eric Bidelman  编写）。以上示例可以在 Chrome 上很好地运行。 Firefox 3.5 及以上的版本均支 CORS，并且这些示例在当前版本中也可以很好地运行。 Opera 支持添加的较晚，直到 12版本（当前版本是12.1）时才支持 CORS，但这个示例在当前版本中也可以很好地运行。 我无法在  Safari 浏览器（我现在所在的 Windows 平台已经弃用 Safari ）上测试示例代码，但看到版本 4 中已经添加了支持，我想这个简单的示例应该也能很好地运行。

#### Internet Explorer

遗憾的是， Internet Explorer  是唯一一种有效浏览器。 从技术上讲， Internet Explorer 9（当前版本）支持  CORS，但不是通过 `XMLHttpRequest` 对象支持它。 相反，IE  使用的是 `XDomainRequest ` 对象，对于我们的简单示例，其工作原理几乎完全相同，但调用 `open() ` 时不接受异步参数。 下面是利用  `XDomainRequest`  为 Internet Explorer  编写的代码。

​        `function onloadHandler() {   var xhr = new XDomainRequest();   xhr.open('GET', 'https://api.github.com/legacy/repos/search/javascript');   // Response handlers.   xhr.onload = function () {      var repos = JSON.parse(xhr.response), i, reposHTML = "";      for (i = 0; i < repos.repositories.length; i++) {         reposHTML += "[" + repos.repositories[\].name + "](" + repos.repositories[i].url                       + ")"                       + repos.repositories[i].description + "";      }      document.getElementById("allRepos").innerHTML = reposHTML;   };      xhr.onerror = function () {      alert('error making the request.');   };   xhr.send();}`    

如果测试这个代码示例，会发现它仍然无法运行。 为什么呢？ 原来，正如 [ Eric Law 的博客：XDomainRequest – 限制、局限和变通方案](http://blogs.msdn.com/b/ieinternals/archive/2010/05/13/xdomainrequest-restrictions-limitations-and-workarounds.aspx) 中所描述的那样，`XDomainRequest` 包含很多额外的安全限制。 其中一个安全限制认为不同安全协议间（只针对 HTTP，不包括 HTTPS）的访问限制“过于宽泛”。 虽然从一个安全页面发送不安全的 HTTP 访问会不受欢迎，并且人们可能会加以阻止，但 Internet Explorer 还是会阻止来自不安全页面的安全请求。 因此，由于 GitHub 的 API 调用均通过 HTTPS 实现，您不能从使用不安全 HTTP 的某个页面进行访问。 还有一种 [复杂的解决方案](http://www.webdbg.com/test/xdm/httptohttps.asp) ，但现在看来这些问题将最终在 Explorer 10 中得到解决，它通过 `XMLHttpRequest ` 支持 CORS。在 Internet Explorer 博客 [IE10 中的 XHR CORS ](http://blogs.msdn.com/b/ie/archive/2012/02/09/cors-for-xhr-in-ie10.aspx) 中可以了解更多与此相关的信息。

###                 使用 jQuery

您可以通过依靠 jQuery 进一步简化 CORS 使用，因为它通过 [ jquery.ajax() ](http://api.jquery.com/jQuery.ajax/) 方法支持 CORS 请求。 显然，同样的限制也适用，虽然它不会在 Internet Explorer 9 中运行，但是它可以大大简化您的代码。 例如，下面的 jQuery 代码创建了与以上代码等效的功能，但所用的代码行数少了很多。

​        `   CORS Example   $(function() {      $.ajax("https://api.github.com/legacy/repos/search/javascript").done(function(data) {         var i, repo;         $.each(data.repositories, function (i, repo) {            $("#allRepos").append("<p><a href='" + repo.url + "'>" + repo.name                                      + "</a><br>"+ repo.description + "</p>");         });      });   });    `    

如您所见，到 GitHub API 和处理结果的 CORS 请求大大简化了。

###                 下一步阅读方向

我的代码示例只通过 CORS 研究了一个简单的 `GET` 请求。 很显然，这与您今天通过 JSONP 所达到的效果差不多，但我们并不需要依赖 JSONP 格式。 然而，CORS 真正的优势在于它执行 `POST`、`PUT` 和其他类型请求的能力。 例如，Google 的 YouTube API 早在 5 月份就在博客 [利用 CORS 开发 JavaScript 的潜能](http://apiblog.youtube.com/2012/05/unlocking-javascripts-potential-with.html)中宣布支持 CORS，其中包括 [使用 CORS 完成 YouTube 上传](http://gdata-samples.googlecode.com/svn/trunk/gdata/youtube_upload_cors.html)，从而让用户将视频上传到 YouTube 上。 视频所有的身份认证和发布都通过 Javascript（您也可以查看示例的源代码）在客户端完成。 有关如何创建和处理这类请求的更多信息，强烈推荐查看 [ HTML5Rocks ](http://www.html5rocks.com)网站上的 [CORS 使用](http://www.html5rocks.com/en/tutorials/cors/)教程。

