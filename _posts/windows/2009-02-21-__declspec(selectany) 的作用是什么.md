---
categories: windows
---
&nbsp; 在MFC，ATL的源代码中充斥着__declspec(selectany) &nbsp;
的声明。selectany可以让我们在.h文件中初始化一个全局变量而不是只能放在.cpp中。比如有一个类，其中有一个静态变量，那么我们可以在.h
中通过类似" &nbsp; __declspec(selectany) &nbsp; type &nbsp; class::variable &nbsp; = &nbsp; value; &nbsp;
"这样的代码来初始化这个全局变量。既是该.h被多次include，链接器也会为我们剔除多重定义的错误。这个有什么好处呢，我觉得对于
teamplate的编程会有很多便利。