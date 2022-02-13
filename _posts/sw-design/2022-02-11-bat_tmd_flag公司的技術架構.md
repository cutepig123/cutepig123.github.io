



# ref

**腾讯**：QUIC 协议在腾讯的实践和优化

**阿里**：使用标准的 ANSI SQL 驱动大数据流计算

**华为**：边缘计算 IoT 云服务应用实践

**微博**：AI 时代精准的个性化推荐

**唯品会**：统一检索平台的演进和探索

**今日头条**：大型直播互动系统的设计与实践

**微众银行**：金融业务中区块链技术架构解析

**菜鸟网络**：全球跨域 RPC 架构设计

**网易严选**：售后服务架构演变实践

**eBay**：QE 团队向工程效率团队转型的实践之路

**Pinterest**：大数据平台的过去与未来

**前 Tesla 深度深度学习负责人**：自动驾驶中的计算机视觉技术

https://www.infoq.cn/article/2018/04/battotmd



https://www.cnblogs.com/hacker-caomei/p/13741252.html

​             [     batj ，tmd用的都是什么技术。         ](https://www.cnblogs.com/hacker-caomei/p/13741252.html)         

b: c++ php

a: java 阿里云：java c++ go

t: c++ go 

j：java 

t：go (python ）

m： java

d： go （php）

 

知乎：Go(python)

饿了么：Java（python）

 

# 1 阿里淘宝：（PHP->JAVA）

https://www.cnblogs.com/wchukai/p/4311195.html

https://www.cnblogs.com/52czm/p/11097156.html

https://blog.csdn.net/jayjaydream/article/details/94925945

https://studygolang.com/articles/14898

 

# 知乎：（Python->Go）

https://www.zhihu.com/question/314356555/answer/616838029

https://www.zhihu.com/question/314356555/answer/625772570

# 滴滴（php->Go）

https://blog.csdn.net/ra681t58cjxsgckj31/article/details/80177303

 

 

# Youtube：(Python->c++)

之前的youtube：

https://blog.csdn.net/iteye_15498/article/details/81647877
Apache
Python
Linux(SuSe)
MySQL
psyco，一个动态的Python到C的编译器
lighttpd代替Apache做视频查看

现在的youtube：

[https://zhuanlan.zhihu.com/p/22339441 ](https://zhuanlan.zhihu.com/p/22339441)

YouTuber历尽千辛万苦，还是将代码分出来严格的Web前端和API层，API层严格划分出了服务模块，各层和模块间只能采用Protocol Buffer的RPC API交互。虽然由于各种不得已这个严格划分好了的Python  codebase（居然）还是要整体发布，但是现在逐个模块重写，至少在技术上成了可能。

轰轰烈烈的 #YTFExit 运动开始了（YTFE = YouTube  FrontEnd），运动还有一个契机：MySQL是真的撑不住了，就算技术上撑得住，Google  SRE也不愿再为YouTube维护一套全Google唯一的巨型MySQL环境了。YouTube决定将所有存储迁移到Spanner,  并且重新设计表结构，那坨绕不开的数据访问Python代码横竖都是要重写的了。YouTube决定将API层的服务逐个用C++重写成独立部署的微服务，最大限度利用Google完善的C++ infrastructure,  prefork什么的自然不会存在，性能的话，其实不管用什么语言只要把陈年代码推倒重写一次都能有显著提升，更别说是C++了。最后只剩下Web层还是Python, 而由于YouTube Web前端已经迁移到Polymer,  可以直接跟API层通信，需要服务器拼接Web页面的地方越来越少，剩下的Web层代码也越来越少，最终也将迁出Python体系。YouTube也将不再是一个Python项目了



https://www.youtube.com/watch?v=G-lGCC4KKok

# Instagram

https://www.youtube.com/watch?v=hnpzNAPiC0E

Timestamps [0:00](https://www.youtube.com/watch?v=hnpzNAPiC0E&t=0s)  Introduction (Lisa Guo)  [2:21](https://www.youtube.com/watch?v=hnpzNAPiC0E&t=141s)  1. Scale out [5:11](https://www.youtube.com/watch?v=hnpzNAPiC0E&t=311s)  1.1 Instagram Stack Overview [5:46](https://www.youtube.com/watch?v=hnpzNAPiC0E&t=346s)  1.2 Storage vs Computing [6:29](https://www.youtube.com/watch?v=hnpzNAPiC0E&t=389s)  1.3 Scale out: Storage [8:13](https://www.youtube.com/watch?v=hnpzNAPiC0E&t=493s)  1.4 Scale out: Computing [8:52](https://www.youtube.com/watch?v=hnpzNAPiC0E&t=532s)  1.5 Memcache + consistency issues [12:05](https://www.youtube.com/watch?v=hnpzNAPiC0E&t=725s) 1.6 DB load problem [14:01](https://www.youtube.com/watch?v=hnpzNAPiC0E&t=841s) 1.7 Memcache Lease [15:12](https://www.youtube.com/watch?v=hnpzNAPiC0E&t=912s) 1.8 Results, Challenges, Opportunities  [17:03](https://www.youtube.com/watch?v=hnpzNAPiC0E&t=1023s) 2. Scale up [17:57](https://www.youtube.com/watch?v=hnpzNAPiC0E&t=1077s) 2.1 Monitor (Collect Data) [20:07](https://www.youtube.com/watch?v=hnpzNAPiC0E&t=1207s) 2.2 Analyze (C-Profile) [23:06](https://www.youtube.com/watch?v=hnpzNAPiC0E&t=1386s) 2.3 Optimize [26:19](https://www.youtube.com/watch?v=hnpzNAPiC0E&t=1579s) 2.3a Memory Optimizations [29:06](https://www.youtube.com/watch?v=hnpzNAPiC0E&t=1746s) 2.3b Network Latency Optimizations [30:40](https://www.youtube.com/watch?v=hnpzNAPiC0E&t=1840s) 2.4 Challenges, Opportunities  [31:36](https://www.youtube.com/watch?v=hnpzNAPiC0E&t=1896s) 3. Scale Dev Team  [33:06](https://www.youtube.com/watch?v=hnpzNAPiC0E&t=1986s) 3.1 What We Want [33:30](https://www.youtube.com/watch?v=hnpzNAPiC0E&t=2010s) 3.2 Tao Infrastructure [34:33](https://www.youtube.com/watch?v=hnpzNAPiC0E&t=2073s) 3.3 Source Control [36:17](https://www.youtube.com/watch?v=hnpzNAPiC0E&t=2177s) 3.4 How to ship code with 1 master approach? [37:54](https://www.youtube.com/watch?v=hnpzNAPiC0E&t=2274s) 3.5 How often do we ship code?  [40:03](https://www.youtube.com/watch?v=hnpzNAPiC0E&t=2403s) Wrap-up [41:15](https://www.youtube.com/watch?v=hnpzNAPiC0E&t=2475s) Q&A

