---
categories: networking tool jekyll
---
jekyll github 博客

# 搭建一个免费的，无限流量的Blog----github Pages和Jekyll入门

http://www.ruanyifeng.com/blog/2012/08/blogging_with_jekyll.html

https://zhuanlan.zhihu.com/p/51240503

## **第三步，使用Github内置主题**

选择好主题，过一会刷新网站地址就已经能看到效果了，而在`Code`页面仅有两个文件。

![img](jekyll%20github%20%E5%8D%9A%E5%AE%A2.assets/v2-dadf8865c36f0b0802da9885a6849641_720w.jpg)


编辑README.md文件的内容，就会默认显示在网站首页，`_config.yml` 是jekyll的全局配置文件，现在里面只有一句话，`theme: jekyll-theme-modernist`。我们可以手动修改这个theme主题配置，网站就会应用不同的主题。

Github内置支持的几个主题，官方的仓库在这里：[https://pages.github.com/themes](https://link.zhihu.com/?target=https%3A//pages.github.com/themes)，每个README.md里都有介绍如何设置。



# gem

https://www.runoob.com/ruby/ruby-rubygems.html

# jekyll

https://halfrost.com/jekyll/

```vim
//使用gem安装Jekyll
gem install jekyll


//使用Jekyll创建你的博客站点
jekyll new blog  #创建你的站点


//开启Jekyll服务
//进入blog目录,记得一定要进入创建的目录，否则服务无法开启
cd blog    	 
jekyll serve 	 #启动你的http服务 
```

https://jekyllrb.com/docs/installation/windows/

1. 从开始菜单中打开一个新的命令提示符窗口，以便对`PATH`环境变量所做的更改生效。使用以下命令安装Jekyll和Bundler`gem install jekyll bundler`
2. 检查Jekyll是否已正确安装： `jekyll -v`