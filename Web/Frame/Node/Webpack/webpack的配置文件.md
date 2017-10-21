---
title: webpack的配置文件
date: 2016-07-21
tags: [Models, Webpack]
categories: Frame
---

通过 require

注：尽量不要使用这种方式，特别是希望脚本可以环境无关地同时跑在 node.js 和浏览器环境中。优先通过配置文件中的命名惯例来指定加载器，参考下一节。
可以通过 require 语句（或 define、require.ensure 等）来指定加载器，只需要用 ! 来分隔资源即可，每部分都是相对当前目录。

require("./loader!./dir/file.txt");
// => 使用当前目录下的 "loader.js" 来转换 "dir" 目录下的 "file.txt" 文件

require("jade!./template.jade");
// => 使用 "jade-loader" （通过 npm 安装在 "node_modules" 目录）来转换 "template.jade" 文件

require("style!css!less!bootstrap/less/bootstrap.less");
// => 通过 github 来安装在 "node_modules" 目录下的 "bootstrap" 模块里的 "less" 目录里的 "bootstrap.less"
//    文件会先被 "less-loader" 转换，然后再被 "css-loader" 转换，最后被 "style-loader" 转换

### 通过配置文件

可以通过正则来在配置文件中绑定加载器

{
    module: {
        loaders: [
            { test: /\.jade$/, loader: "jade" },
            // => "jade" loader is used for ".jade" files

            { test: /\.css$/, loader: "style!css" },
            // => "style" and "css" loader is used for ".css" files
            // Alternative syntax:
            { test: /\.css$/, loaders: ["style", "css"] },
        ]
    }
}

webpack-dev-server 使用了 webpack 监控模式，同时也阻止了 webpack 生成结果文件到硬盘，而是直接通过内存来提供服务。