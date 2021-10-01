# 目的

傳統ppt面臨的問題

- 文件是二進制，不能方面的做原代碼控制
- 需要手動做格式調整，不夠簡潔

當然它的好處是非常靈活，所見即所得

用markdown寫ppt的好處

- 方便原代碼控制
- 格式統一

壞處是如果想定製一些非常規界面，靈活性可能不夠



# reveal.js

## reveal-md

https://github.com/cutepig123/reveal-md-example

# nodeppt

https://github.com/tiodot/ppt

https://rye-catcher.github.io/2019/10/21/Nodeppt-%E5%85%A5%E5%9D%91%E6%8C%87%E5%8D%97/

npm install -g nodeppt

nodeppt new slides.md
nodeppt serve slides.md
nodeppt build slides.md



# 总结

- 如果是简单的，内部分享，要求不高，要git版本控制的ppt，用reveal之类
- 对外的，用office ppt

# Ref

https://www.zhihu.com/question/52896240

一般需求用 [http://slides.com](https://link.zhihu.com/?target=http%3A//slides.com) 的服务应该能满足大部分场景。但如果需要内嵌脚本之类的，可能就不太够用了。可以手写 HTML/Markdown 然后用 [reveal.js](https://link.zhihu.com/?target=http%3A//lab.hakim.se/reveal-js/) 来展示。

https://jk2k.com/2018/01/how-to-write-presentation-using-markdown/

