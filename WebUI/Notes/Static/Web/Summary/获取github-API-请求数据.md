---
title: 获取GitHub API 请求数据
date: 2016-04-27
tags: [GitHub,跨域,浏览器]
categories: Dynamic
---

俩中方式，获取github上面的数据。

1.原生js

```javascript
<html>
<head>
   <title>CORS Example</title>
<script>
   function onloadHandler() {
      var xhr = new XMLHttpRequest();
      xhr.open('GET', 'https://api.github.com/legacy/repos/search/javascript', true);
      // Response handlers.
      xhr.onload = function () {
         var repos = JSON.parse(xhr.response), i, reposHTML = "";
         for (i = 0; i < repos.repositories.length; i++) {
            reposHTML += "<p><a href='" + repos.repositories[i].url
                         + "'>" + repos.repositories[i].name + "</a><br>"
                         + repos.repositories[i].description + "</p>";
         }
         document.getElementById("allRepos").innerHTML = reposHTML;
      };
   
      xhr.onerror = function () {
         alert('error making the request.');
      };
   
      xhr.send();
   }
</script>
</head>
<body onload="onloadHandler()">
   <div id="allRepos"></div>
</body>
</html>
```

1. 借助jQuery

```javascript
<html>
<head>
   <title>CORS Example</title>
<script src="../../../jquery.min.js"></script>
<script>
   $(function() {
      $.ajax("https://api.github.com/legacy/repos/search/javascript").done(function(data) {
         var i, repo;
         $.each(data.repositories, function (i, repo) {
            $("#allRepos").append("<p><a href='" + repo.url + "'>" + repo.name 
                                     + "</a><br>"+ repo.description + "</p>");
         });
      });
   });
</script>
</head>
<body>
   <div id="allRepos"></div>
</body>
</html> 
```



