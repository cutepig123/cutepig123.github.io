Video https://www.youtube.com/watch?v=WLDT1lDOsb4

ppt https://github.com/CppCon/CppCon2017/blob/master/Presentations/Free%20Your%20Functions/Free%20Your%20Functions%20-%20Klaus%20Iglberger%20-%20CppCon%202017.pdf

建议看视频，视频更有感染力

作者的口才很好



作者从以下方面论证了free function更好

Encapsulation
Abstraction / Polymorphism
Cohesion
Flexibility / Extensibility
Reuse / Generality
Testability
Performance



搬出Scott Meyers的话

”Object-oriented principles dictate that data and the functions
that operate on them should be bundled together, and that
suggests that the member function is the better choice.
Unfortunately, this suggestion is incorrect. It’s based on a
misunderstanding of what being object-oriented means. Objectoriented
principles dictate that data should be as encapsulated
as possible. Counterintuitively, the member function [...] actually
yields less encapsulation than the non-member [...].”
(Scott Meyers, Effective C++, 3rd edition)

”面向对象的原则规定数据和功能
对它们进行操作的应该捆绑在一起，并且
表明成员函数是更好的选择。
不幸的是，这个建议是不正确的。 它基于一个
误解了面向对象的含义。 面向对象
原则规定数据应该被封装
尽可能。 与直觉相反，成员函数 [...] 实际上
比非成员产生更少的封装 [...]。”
（Scott Meyers，Effective C++，第 3 版）



搬出cpp作者的话

”Note begin(c) and c.begin() for range-for loops and in general
code. Why do we/someone have to write both? If c.begin()
exists, begin(c) should find it, just as x+y finds the right
implementation. … In early 2014, Herb Sutter and I each
independently decided to propose a unified syntax. … To my
surprise, many people came out strongly against x.f(y) finding
f(x,y) – even if member functions were preferred over freestanding
functions by the lookup rules. I received email accusing
me of “selling out to the OO crowd”.”
(Bjarne Stroustrup)

”注意 begin(c) 和 c.begin() 用于 range-for 循环和一般
代码。 为什么我们/某人必须同时写两者？ 如果 c.begin()
存在，begin(c) 应该找到它，就像 x+y 找到正确的一样
执行。 … 2014 年初，赫伯·萨特和我各自
独立决定提出统一的语法。 ......对我的
令人惊讶的是，许多人强烈反对 x.f(y) 发现
f(x,y) – 即使成员函数比独立函数更受欢迎
功能由查找规则。 我收到电子邮件指责
我“卖给了面向对象的人群”。
(Bjarne Stroustrup)