---
title: 介绍如何为 hexo 写一个本地的搜索引擎。
date: 2016-3-30 23:07:41
tags: [Hexo,博客]
categories: Frame
---

早在我最初[从 Ruhoh 迁移博客到 Hexo](http://hahack.com/codes/from-ruhoh-to-hexo/) 时，我就有动手写一个本地的搜索引擎的想法。比起使用第三方服务的站内搜索，本地搜索引擎有几个好处：
<!-- more -->
1. 更可靠。不用担心~~由于某些显而易见的原因导致~~第三方服务不可访问。
2. 速度更快。不管是 Google 还是 Swiftype ，第三方搜索服务的加载速度总是比较慢，影响浏览体验。
3. 定制性更强。由于是自己写的插件，检索的具体策略、界面样式都可以自己定义，满足极客们 Bigger than Bigger 的需求。

这个想法起初是受了 Christian Fei 的 [Simple Jekyll Search](https://github.com/christian-fei/Simple-Jekyll-Search) 启发。在了解了它的原理后，我认为在 Hexo 上实现一个本地搜索引擎并不复杂。大致的思路是：

- 写一个 generator ，生成站点所有文章的索引数据；
- 当在搜索框中输入关键词时，触发 Javascript 的特定函数，在这个索引数据里头检索包含该关键词的文章；
- 利用 jQuery 在页面中动态插入检索结果。

想法对头，就开始动手撸吧。我和一个朋友 [maoshuhao](https://github.com/maoshuhao) 一起合作完成了 [hexo-generator-search](https://github.com/PaicHyperionDev/hexo-generator-search) 插件，用来生成站点的索引数据。有了它，后面的搜索引擎就非常容易实现了。

你可以访问这个 [404页面](http://wzpan.github.io/hexo-theme-freemind/404.html) 试试这个本地搜索引擎的效果。如你所见，这个搜索引擎还是一个 live search engine ，即一旦检测到搜索框有修改，就会立即触发检索 1 1对于文章太多的站点，如果认为 live search 影响性能，可以改为回车触发搜索。。

下面介绍如何给自己的博客搭建这样的一个搜索引擎。

最新版本的 [hexo-theme-freemind](http://github.com/wzpan/hexo-theme-freemind/) 已提供了本地搜索功能。如果懒得折腾，欢迎使用这个主题。

## 安装和配置 hexo-generator-search

```
$ npm install --save hexo-generator-search
```

然后，在站点根 `_config.yml` 里头添加设置项：

```
search:
  path: search.xml
  field: post
```

其中：

- **path** - 指定生成的索引数据的文件名。默认为 search.xml 。
- **field** - 指定索引数据的生成范围。可选值包括：**post** - 只生成博客文章（post）的索引（默认）；**page** - 只生成其他页面（page）的索引；**all** - 生成所有文章和页面的索引。

完成后，可以试试访问预览站点的 search.xml 页面。例如，如果你的预览站点域名是 http://0.0.0.0:4000 ，那么可以访问 http://0.0.0.0:4000/search.xml 看看是否会打开一个 xml 页面。

## 编写搜索界面

搜索界面由一个输入框（input）和一个用于动态插入搜索结果的 div 组成。例如：

```
<div id="site_search">
  <input type="text" id="local-search-input" name="q" results="0" placeholder="search my blog..." class="form-control"/>
  <div id="local-search-result"></div>
</div>
```

你也可以根据自己的喜好写成其他的形式，例如把用于插入结果的 div 移动到页面的其他地方。

## 实现本地搜索函数

接下来编写一个 search.js 脚本，用来实现基于 search.xml 的本地检索函数 searchFunc ：

```
var searchFunc = function(path, search_id, content_id) {
    'use strict';
    $.ajax({
        url: path,
        dataType: "xml",
        success: function( xmlResponse ) {
            // get the contents from search data
            var datas = $( "entry", xmlResponse ).map(function() {
                return {
                    title: $( "title", this ).text(),
                    content: $("content",this).text(),
                    url: $( "url" , this).text()
                };
            }).get();

            var $input = document.getElementById(search_id);
            var $resultContent = document.getElementById(content_id);

            $input.addEventListener('input', function(){
                var str='<ul class=\"search-result-list\">';                
                var keywords = this.value.trim().toLowerCase().split(/[\s\-]+/);
                $resultContent.innerHTML = "";
                if (this.value.trim().length <= 0) {
                    return;
                }
                // perform local searching
                datas.forEach(function(data) {
                    var isMatch = true;
                    var content_index = [];
                    var data_title = data.title.trim().toLowerCase();
                    var data_content = data.content.trim().replace(/<[^>]+>/g,"").toLowerCase();
                    var data_url = data.url;
                    var index_title = -1;
                    var index_content = -1;
                    var first_occur = -1;
                    // only match artiles with not empty titles and contents
                    if(data_title != '' && data_content != '') {
                        keywords.forEach(function(keyword, i) {
                            index_title = data_title.indexOf(keyword);
                            index_content = data_content.indexOf(keyword);

                            if( index_title < 0 && index_content < 0 ){
                                isMatch = false;
                            } else {
                                if (index_content < 0) {
                                    index_content = 0;
                                }
                                if (i == 0) {
                                    first_occur = index_content;
                                }
                            }
                        });
                    }
                    // show search results
                    if (isMatch) {
                        str += "<li><a href='"+ data_url +"' class='search-result-title'>"+ data_title +"</a>";
                        var content = data.content.trim().replace(/<[^>]+>/g,"");
                        if (first_occur >= 0) {
                            // cut out 100 characters
                            var start = first_occur - 20;
                            var end = first_occur + 80;

                            if(start < 0){
                                start = 0;
                            }

                            if(start == 0){
                                end = 100;
                            }

                            if(end > content.length){
                                end = content.length;
                            }

                            var match_content = content.substr(start, end); 

                            // highlight all keywords
                            keywords.forEach(function(keyword){
                                var regS = new RegExp(keyword, "gi");
                                match_content = match_content.replace(regS, "<em class=\"search-keyword\">"+keyword+"</em>");
                            });
                            
                            str += "<p class=\"search-result\">" + match_content +"...</p>"
                        }
                        str += "</li>";
                    }
                });
                str += "</ul>";
                $resultContent.innerHTML = str;
            });
        }
    });
}
```

searchFunc 包含三个参数：

- **path** - 用 hexo-generator-search 生成的搜索索引文件的路径。注意这个 `path` 和前面 hexo-generator-search 的 `path` 选项有所不同。这里的 path 才是指这个文件的路径，而前面的 `path` 指的是生成的文件名 2 2也许第二个 `path` 叫 `filename` 更合适。；
- **search_id** - 搜索框的 id 。对于我们的例子，就是 `local-search-input`;
- **content_id** - 结果框的 id 。对于我们的例子，就是 `local-search-result`。

## 调用搜索函数

有了上面的检索函数，接下来可以在适当时机调用它。由于 path 的实际地址是根 `_config.yml` 里 `config.root` + `config.search.path` 两个值组成，所以我们最好将这个调用写在页面模板中，以方便获取站点的设置信息。例如，对于 ejs 模板：

```
<script type="text/javascript">      
     var search_path = "<%= config.search.path %>";
     if (search_path.length == 0) {
     	search_path = "search.xml";
     }
     var path = "<%= config.root %>" + search_path;
     searchFunc(path, 'local-search-input', 'local-search-result');
</script>
```

至此就完成了本地检索引擎的实线，最后的工作就是修改样式，让检索页面更美观。在 searchFunc 函数中，我已经为几个关键的页面元素设定了 css 名：

- ul.search-result-list - 搜索结果列表的样式名；
- a.search-result-title - 搜索结果文章标题的样式名；
- p.search-result - 搜索结果每篇文章的预览段落的样式名；
- em.search-keyword - 搜索结果每篇文章的预览段落中匹配关键词的样式名。

最后给出 [hexo-theme-freemind](http://wzpan.github.io/hexo-theme-freemind/) 主题的相关样式：

```
ul.search-result-list {
  padding-left: 10px;
}

a.search-result-title {
  font-weight: bold;
}

p.search-result {
  color=#555;
}

em.search-keyword {
  border-bottom: 1px dashed #4088b8;
  font-weight: bold;
}
```

