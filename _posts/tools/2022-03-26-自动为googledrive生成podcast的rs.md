生命不息，折腾不止	- cutepig



搞些对自己有用的东西其实挺好玩的。如果能给更多人用就更好了。 -cutepig



# 目的

给定一个google drive链接，里面有很多音频。能否自动生成一个rss添加到播客app里面？



# 工具

- python
- android app: podcast addict。这个工具的好处是能够一键添加opml从而一次订阅多个播客rss



# 步骤

- 下载代码，生成rss - 当然你也可以直接用我现成的rss

```bash
F:\_codes\>git clone https://github.com/cutepig123/podcast_from_google_drive.git

F:\_codes\>cd podcast_from_google_drive

F:\_codes\podcast_from_google_drive>set GOOGLE_APPLICATION_CREDENTIALS=f:\Users\cutepig\Downloads\credentials.json

F:\_codes\podcast_from_google_drive>python test-poadcast-rssmaker.py
'148cr7xvj8A5PjhGCy2m7pcYiR5Dc51RA' in parents
'16ekvCKwDNiBIbb5e4a1Klu7RofxMnRWc' in parents
'1k8UBmpvAcFz9wg3ruIGz7-9s4-FWmim0' in parents
1ko3U0Isbw3th1tpVTVVBeHildFnt1kGD .49 GO语言从入门到实战.课程简介.11 - Map与工厂模式，在Go语言中实现Set.txt
1kjZzy3gZJ2Pyn5WYxZw6EDb51k9l0PC1 .49 GO语言从入门到实战.课程简介.10 - Map 声明、元素访问及遍历.txt
1keDe6NI2HlJiBNl1-8TnKGnrLUQViIJx .49 GO语言从入门到实战.课程简介.09 - 数组和切片.txt
1kchYzN_fUvGC0fUa-f6JiFNsl0vuHS_s .49 GO语言从入门到实战.课程简介.08 - 条件和循环.txt
1k_tnZaA47HnPtWWo0vGkt9BeRTQe4qhR .49 GO语言从入门到实战.课程简介.07 - 运算符.txt
1kZ-M3WewSrQbgftYJ_Mskmdb6LnesG5J .49 GO语言从入门到实战.课程简介.06 - 数据类型.txt
1kRn0zNlXvM2UQ54v2JssX2ZKf3MKmCoU .49 GO语言从入门到实战.课程简介.05 - 变量、常量以及与其他语言的差异.txt
1kRC4LII5roBjNH2mtmGd8j7Lbb8iukbW .49 GO语言从入门到实战.课程简介.04 - 编写第一个Go程序.txt
1kQp_Q-MzDaWuenspYCuFkf2zSZrIe20s .49 GO语言从入门到实战.课程简介.03 - Go 语言简介：历史背景、发展现状及语言特性.txt
1kOgA438snnmiYmfZkSL6b_F-K1tCRiAS .49 GO语言从入门到实战.课程简介.02 - 内容综述.txt
1kCPpRYSI4lZygwE2kLDnLnqxPOSDSeWo .49 GO语言从入门到实战.课程简介.01 - Go语言课程介绍.txt
1dzj34gTf7JjS7i6Crz8WAExe4Kv91uSN .49 GO语言从入门到实战.课程大纲.jpg
1dZdtlMx2Fu1u7ZPAkDwl18sigGXAijoh .49 GO语言从入门到实战.55-结束语.mp4
1dJW1Dl5O5jREvZhQ_yhIkKPvqs5M9RNA .49 GO语言从入门到实战.54-chaos_engineering.mp4
1dDwkY68en4eIc79HRk_eX98pBlZTsuIi .49 GO语言从入门到实战.53-面向恢复的设计.mp4
1czVXgw2HB-gEbnJMpQGtfM_qEW-1PDuY .49 GO语言从入门到实战.52-面向错误的设计.mp4
1cupP1OSDEJZKmLjz7R8fPfXOnpZF4g77 .49 GO语言从入门到实战.51-高效字符串连接.mp4
1ci04_xXQYgN4aL9PpRJr9R3wMMMlveD1 .49 GO语言从入门到实战.50-GC友好的代码.mp4
1cPezEMntD3UX0gTo5lhp4GEYBZ54XdRO .49 GO语言从入门到实战.49-别让性能被锁住.mp4
1cLxap9DRp8kDVpSn48Vn0Iqqctd0LGGA .49 GO语言从入门到实战.48-性能调优示例.mp4
1cIMEHy9u1OeHe3ObDfAZpw23HWDdrXMP .49 GO语言从入门到实战.47-性能分析工具.mp4
1cFbVDa7i_KgigI317jtC1P1hdAVY9efX .49 GO语言从入门到实战.46-构建Restful服务.mp4
1byGRb-GADnOLS_sHkxFiFIoHZBSaMcFw .49 GO语言从入门到实战.45 HTTP服务.mp4
1bgHwYtGkTE7mtuggDIcJCFlm_Hfuy3R9 .49 GO语言从入门到实战.44 easyjson.mp4
1bVIYlc577VeFs-fKynfJNcoMIo8srNE- .49 GO语言从入门到实战.43内置JSON解析.mp4
1b91rwGzYyvGikx8AozXrqRSwmyBczq0Y .49 GO语言从入门到实战.42实现micro-kernelframework.mp4
1b3tYPRmUnHqptJelFXhbLi-i9FiJ7_Qr .49 GO语言从入门到实战.41 实现pipe-filter framework.mp4
1ax1oCNBKaQhAPCzLR54Vz1gkBC-my0tt .49 GO语言从入门到实战.40 不安全编程.mp4
1as8aPfeiVQXwwR1cqym5D6LaMepwJNlU .49 GO语言从入门到实战.39 万能程序.mp4
1aoAHgmIHXsx1AJe94T4rdUFsNd7zcylk .49 GO语言从入门到实战.38 反射编程.mp4
...


```



- 执行python -m http.server -b 0.0.0.0 8080，启动http服务器

  ```bash
  F:\_codes\podcast_from_google_drive>python -m http.server -b 0.0.0.0 8080
  Serving HTTP on 0.0.0.0 port 8080 (http://0.0.0.0:8080/) ...
  
  ```

  

- 手机打开app podcast addict，把 http://IP:8080/opmlresult.opml加入订阅
- DONE！