---
categories: jekyll
---
为Jekyll博客添加目录与ScrollSpy效果

ref: http://t.hengwei.me/post/%E4%B8%BAjekyll%E5%8D%9A%E5%AE%A2%E6%B7%BB%E5%8A%A0%E7%9B%AE%E5%BD%95%E4%B8%8Escrollspy%E6%95%88%E6%9E%9C.html

# 1-a 纯JS版本

本文所用的便是纯javascript版的toc插件[jekyll-table-of-contents](https://github.com/ghiculescu/jekyll-table-of-contents). 其README也很详细，照着一步步配即可。
\* 在待添加插件的模板中首先加入`jquery.js`的依赖，然后是把该`toc.js`放在其后。

```
<script src="/javascripts/jquery-2.1.4.min.js" type="text/javascript"></script>
<script src="/javascripts/toc.js" type="text/javascript"></script>
```

- 在需要显示目录结构的地方加上如下div。

```
<div id="toc"></div>
```

- 把toc.js调用函数放在最后（如``之前）即可。

```
<script type="text/javascript">
$(document).ready(function() {
    $('#toc').toc();
}); </script>
```