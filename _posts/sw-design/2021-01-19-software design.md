---
categories: sw-design
---
[TOC]



# software design

https://i.cs.hku.hk/~kpchan/csis0521/

| [25/9] [Software Requirement](http://www.cs.hku.hk/~kpchan/csis0521/Notes/4-Requirements.pdf) | [27/9] [Software Architecture](http://www.cs.hku.hk/~kpchan/csis0521/Notes/Architecture.pdf) | [29/9] [Software Design](http://www.cs.hku.hk/~kpchan/csis0521/Notes/Design.pdf) |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |                                                              |

https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-005-software-construction-spring-2016/readings/

可以在[6.005 Github页面](https://github.com/mit6005/)上找到一些读数的示例代码。

| 阅读                                                         | 主题                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [1：静态检查](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/01-static-checking/) | 种类静态检查与动态检查数组和集合反复进行方法变异变量与重新分配变量记录假设 |
| [2：基本Java](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/02-basic-java/) | 快照图Java集合Java API文档                                   |
| [3：测试](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/03-testing/) | 验证方式测试优先编程通过分区选择测试用例黑盒和白盒测试记录测试策略覆盖范围单元测试和存根自动化测试和回归测试 |
| [4：代码审查](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/04-code-review/) | 不要重复自己需要评论快速失败避免魔术数字每个变量一个目的使用好名字使用空格帮助读者不要使用全局变量方法应返回结果，而不是打印结果 |
| [5：版本控制](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/05-version-control/) | 发明版本控制Git：复制，提交，拉，推，合并                    |
| [6：规格](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/06-specifications/) | 为什么要规格？行为对等规格结构空引用规范可以谈论什么测试与规格突变方法规格错误通知的异常特殊结果的例外已检查和未检查的异常可抛出的层次结构异常设计注意事项滥用例外 |
| [7：设计规范](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/07-designing-specs/) | 确定性与不确定性规范声明性规范与操作规范较弱者规格更强图表规格设计良好的规格前置条件还是后置条件？关于访问控制关于静态方法与实例方法 |
| [8：避免调试](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/08-avoiding-debugging/) | 第一道防线：消除错误第二防御：本地化错误断言断言什么什么不断言增量发展模块化和封装 |
| [9：可变性和不变性](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/09-immutability/) | 变异性变异的风险混淆是使变异具有风险的原因突变方法规格遍历数组和列表突变破坏了迭代器突变与契约有用的实现类型 |
| [10：递归](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/10-recursion/) | 为问题选择正确的分解递归实现的结构辅助方法选择正确的递归子问题递归问题与递归数据重入代码何时使用递归而不是迭代递归实现中的常见错误 |
| [11：调试](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/11-debugging/) | 重现错误了解错误的位置和原因修正错误                         |
| [12：抽象数据类型](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/12-abstract-data-types/) | 抽象是什么意思分类类型和操作设计抽象类型代表独立用Java实现ADT概念测试和抽象数据类型 |
| [13：抽象函数和Rep不变量](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/13-abstraction-functions-rep-invariants/) | 不变量Rep不变和抽象函数记录Rep曝光的AF，RI和安全性ADT不变式替换前提条件 |
| [14：接口](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/14-interfaces/) | 介面亚型示例：MyString示例：设置通用接口为什么要接口？用Java实现ADT概念，第二部分 |
| [15：平等](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/15-equality/) | 平等的三种方式== vs.equals（）不变类型的相等对象合同可变类型的相等Equals（）和hashCode（）的最终规则 |
| [16：递归数据类型](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/16-recursive-data-types/) | 递归函数不可变列表递归数据类型定义递归数据类型上的函数调整代表空与空声明类型与实际类型示例：布尔公式用ADT编写程序使用ADT进行编程的食谱示例：矩阵乘法 |
| [17：正则表达式和语法](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/17-regex-grammars/) | 文法常用表达                                                 |
| [18：解析器生成器](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/18-parser-generators/) | 解析器生成器副语法生成解析器调用解析器遍历解析树构造抽象语法树处理错误 |
| [19：并发](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/19-concurrency/) | 并发编程的两种模型进程，线程，时间分片示例：共享内存交织比赛条件调整代码无济于事重新排序示例：消息传递并发很难测试和调试 |
| [20：线程安全](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/20-thread-safety/) | 线程安全是什么意思策略1：禁闭策略2：不变性策略3：使用Threadsafe数据类型如何提出安全论点 |
| [21：套接字和网络](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/21-sockets-networking/) | 客户端/服务器设计模式网络插座输入输出封锁使用网络套接字有线协议测试客户端/服务器代码 |
| [22：队列和消息传递](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/22-queues/) | 两种并发模型带线程的消息传递使用队列实现消息传递正在停止带有消息传递的线程安全参数 |
| [23：锁定和同步](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/23-locks/) | 同步化僵局开发ThreadSafe抽象数据类型锁定监控模式带有同步的线程安全参数原子操作设计并发数据类型死锁抬起丑陋的头并行程序设计的目标实践中的并发 |
| [24：图形用户界面](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/24-graphical-user-interfaces/) | 查看树如何使用视图树输入处理将前端与后端分离图形用户界面中的后台处理 |
| [25：地图，过滤器，缩小](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/25-map-filter-reduce/) | 抽象控制流地图作为价值的功能过滤降低抽象控制的好处Java中的一流函数Java中的Map / Filter / ReduceJava中的高阶函数 |
| [26：小语言](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/26-little-languages/) | 将代码表示为数据建立解决问题的语言音乐语言                   |
| [27：团队版本控制](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/27-team-version-control/) | Git工作流程查看提交历史提交图团队使用版本控制                |

#  软件构造要素

## 课程特色

- [演讲笔记](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-005-elements-of-software-construction-fall-2008/lecture-notes)
- [项目（无示例）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-005-elements-of-software-construction-fall-2008/labs-and-projects)
- [作业：问题集（无解决方案）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-005-elements-of-software-construction-fall-2008/assignments)
- [作业：使用示例编程](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-005-elements-of-software-construction-fall-2008/assignments/)

# 软件工程基础

## 课程特色

- [作业：演示文稿（无示例）](https://ocw.mit.edu/courses/civil-and-environmental-engineering/1-124j-foundations-of-software-engineering-fall-2000/projects/)
- [作业：使用示例编程](https://ocw.mit.edu/courses/civil-and-environmental-engineering/1-124j-foundations-of-software-engineering-fall-2000/assignments/)
- [作业：书面（无示例）](https://ocw.mit.edu/courses/civil-and-environmental-engineering/1-124j-foundations-of-software-engineering-fall-2000/projects/)
- [考试和解决方案](https://ocw.mit.edu/courses/civil-and-environmental-engineering/1-124j-foundations-of-software-engineering-fall-2000/exams)

# Mathematics for Computer Science

## Course Features

- [Video lectures](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-spring-2015/proofs/tp1-1/)
- [Captions/transcript](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-spring-2015/proofs/tp1-1/)
- [Interactive assessments](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-spring-2015/proofs/)
- [Online textbooks](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-spring-2015/readings/)
- [Lecture notes](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-spring-2015/lecture-slides/)
- [Assignments: problem sets (no solutions)](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-spring-2015/assignments/)
- [Exams (no solutions)](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-spring-2015/exams/)
- [Resource Index](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-spring-2015/resource-index)

# AI

| 讲义                                                         | 主题                                   |
| :----------------------------------------------------------- | :------------------------------------- |
| [教程1（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-034-artificial-intelligence-fall-2010/tutorials/MIT6_034F10_tutor01.pdf) | 基于规则的系统，搜索                   |
| [教程2（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-034-artificial-intelligence-fall-2010/tutorials/MIT6_034F10_tutor02.pdf) | 游戏，约束满足问题                     |
| [指南3（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-034-artificial-intelligence-fall-2010/tutorials/MIT6_034F10_tutor03.pdf) | K近邻，决策树，神经网络                |
| [教程4（PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-034-artificial-intelligence-fall-2010/tutorials/MIT6_034F10_tutor04.pdf)） | 自顶向下的神经网络方法                 |
| [教程5（PDF） ](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-034-artificial-intelligence-fall-2010/tutorials/MIT6_034F10_tutor05.pdf) | 支持向量机，提升                       |
| [指南6（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-034-artificial-intelligence-fall-2010/tutorials/MIT6_034F10_tutor06.pdf) | 概率，贝叶斯网络，朴素贝叶斯，模型选择 |

# 计算思维与数据科学导论

| SES编号 | 演讲幻灯片                                                   | 代码和附加文件                                               |
| :------ | :----------------------------------------------------------- | :----------------------------------------------------------- |
| 1个     | [第1课：简介和优化问题（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-slides-and-files/MIT6_0002F16_lec1.pdf) | [第1课（ZIP）的其他文件](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-slides-and-files/Lecture1.zip)（此ZIP文件包含：1个.txt文件和1个.py文件） |
| 2       | [第2课：优化问题（PDF-6.9MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-slides-and-files/MIT6_0002F16_lec2.pdf) | [第2课（ZIP）的其他文件](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-slides-and-files/Lecture2.zip)（此ZIP文件包含：1个.txt文件和1个.py文件） |
| 3       | [第3课：图论模型（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-slides-and-files/MIT6_0002F16_lec3.pdf) | [第3课（PY）的代码文件](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-slides-and-files/lectureGraphs.py) |
| 4       | [讲座4：随机思维（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-slides-and-files/MIT6_0002F16_lec4.pdf) | [第4课（PY）的代码文件](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-slides-and-files/lecture4.py) |
| 5       | [讲座5：随机漫步（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-slides-and-files/MIT6_0002F16_lec5.pdf) | [第5课（PY）的代码文件](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-slides-and-files/lect5.py) |
| 6       | [讲座6：蒙特卡洛模拟（PDF-1.2MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-slides-and-files/MIT6_0002F16_lec6.pdf) | [第6课（PY）的代码文件](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-slides-and-files/lect6.py) |
| 7       | [第7课：置信区间（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-slides-and-files/MIT6_0002F16_lec7.pdf) | [第7课（PY）的代码文件](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-slides-and-files/lect7.py) |
| 8       | [第8讲：采样和标准误差（PDF-1.3MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-slides-and-files/MIT6_0002F16_lec8.pdf) | [第8课的其他文件（ZIP-1.6MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-slides-and-files/Lecture8.zip)（此ZIP文件包含：1个.csv文件和1个.py文件） |
| 9       | [第9课：了解实验数据（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-slides-and-files/MIT6_0002F16_lec9.pdf) | [第9课（ZIP）的其他文件](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-slides-and-files/Lecture9.zip)（此ZIP文件包含：4个.txt文件和1个.py文件） |
| 10      | [第10课：了解实验数据（续）（PDF-1.3MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-slides-and-files/MIT6_0002F16_lec10.pdf) | [第10课的其他文件（ZIP-1.7MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-slides-and-files/Lecture10.zip)（此ZIP文件包含：1个.csv文件，7个.txt文件和2个.py文件） |
| 11      | [第11课：机器学习简介（PDF-1.1MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-slides-and-files/MIT6_0002F16_lec11.pdf) | [第11课（PY）的代码文件](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-slides-and-files/lectureCode.py) |
| 12      | [第十二课：聚类（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-slides-and-files/MIT6_0002F16_lec12.pdf) | [第12课（ZIP）的其他文件](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-slides-and-files/Lecture12.zip)（此ZIP文件包含：1个.txt文件和2个.py文件） |
| 13      | [第13课：分类（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-slides-and-files/MIT6_0002F16_lec13.pdf) | [第13课（ZIP）的其他文件](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-slides-and-files/Lecture13.zip)（此ZIP文件包含：1个.txt文件和1个.py文件） |
| 14      | [第十四课：分类和统计罪（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-slides-and-files/MIT6_0002F16_lec14.pdf) | [第14课（ZIP）的其他文件](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-slides-and-files/Lecture14.zip)（此ZIP文件包含：1个.txt文件和1个.py文件） |
| 15      | [第15课：统计罪与总结（PDF-1.1MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-slides-and-files/MIT6_0002F16_lec15.pdf) | [第15课（PY）的代码文件](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-slides-and-files/lect15.py) |

# Topics in Mathematics with Applications in Finance

| LEC编号 | 主题                                                         |
| :------ | :----------------------------------------------------------- |
| 1个     | [简介与财务条款和概念（PDF）](https://ocw.mit.edu/courses/mathematics/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/lecture-notes/MIT18_S096F13_lecnote1.pdf) |
| 2       | [线性代数（PDF）](https://ocw.mit.edu/courses/mathematics/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/lecture-notes/MIT18_S096F13_lecnote2.pdf) |
| 3       | [概率论（PDF）](https://ocw.mit.edu/courses/mathematics/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/lecture-notes/MIT18_S096F13_lecnote3.pdf) |
| 4       | Matrix Primer [没有讲义，但请参阅[Morgan Stanley Matrix TM微型网站](http://www.morganstanley.com/matrixinfo/)以获取有关此主题的信息] |
| 5       | [随机过程I（PDF）](https://ocw.mit.edu/courses/mathematics/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/lecture-notes/MIT18_S096F13_lecnote5.pdf) |
| 6       | [回归分析（PDF）](https://ocw.mit.edu/courses/mathematics/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/lecture-notes/MIT18_S096F13_lecnote6.pdf) |
| 7       | [风险价值（VAR）模型（PDF-1.1MB）](https://ocw.mit.edu/courses/mathematics/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/lecture-notes/MIT18_S096F13_lecnote7.pdf) |
| 8       | [时间序列分析I（PDF）](https://ocw.mit.edu/courses/mathematics/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/lecture-notes/MIT18_S096F13_lecnote8.pdf) |
| 9       | [波动率建模（PDF）](https://ocw.mit.edu/courses/mathematics/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/lecture-notes/MIT18_S096F13_lecnote9.pdf) |
| 10      | [正则定价和风险模型（PDF-2.0MB）](https://ocw.mit.edu/courses/mathematics/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/lecture-notes/MIT18_S096F13_lecnote10.pdf) |
| 11      | [时间序列分析II（PDF）](https://ocw.mit.edu/courses/mathematics/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/lecture-notes/MIT18_S096F13_lecnote11.pdf) |
| 12      | [时间序列分析III（PDF）](https://ocw.mit.edu/courses/mathematics/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/lecture-notes/MIT18_S096F13_lecnote12.pdf) |
| 13      | [商品模型（PDF-1.1MB）](https://ocw.mit.edu/courses/mathematics/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/lecture-notes/MIT18_S096F13_lecnote13.pdf) |
| 14      | [投资组合理论（PDF）](https://ocw.mit.edu/courses/mathematics/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/lecture-notes/MIT18_S096F13_lecnote14.pdf) |
| 15      | [因子建模（PDF）](https://ocw.mit.edu/courses/mathematics/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/lecture-notes/MIT18_S096F13_lecnote15.pdf) |
| 16      | [投资组合管理（PDF）](https://ocw.mit.edu/courses/mathematics/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/lecture-notes/MIT18_S096F13_lecnote16.pdf) |
| 17      | [随机过程II（PDF）](https://ocw.mit.edu/courses/mathematics/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/lecture-notes/MIT18_S096F13_lecnote17.pdf) |
| 18岁    | [伊藤微积分（PDF）](https://ocw.mit.edu/courses/mathematics/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/lecture-notes/MIT18_S096F13_lecnote18.pdf) |
| 19      | [Black-Scholes公式和风险中性评估（PDF）](https://ocw.mit.edu/courses/mathematics/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/lecture-notes/MIT18_S096F13_lecnote19.pdf) |
| 20      | 期权价格和概率对偶[无讲义]                                   |
| 21      | [随机微分方程（PDF）](https://ocw.mit.edu/courses/mathematics/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/lecture-notes/MIT18_S096F13_lecnote21.pdf) |
| 22      | 变异演算及其在FX执行中的应用[无演讲笔记]                     |
| 23      | [Quanto信贷对冲（PDF-1.1MB）](https://ocw.mit.edu/courses/mathematics/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/lecture-notes/MIT18_S096F13_lecnote23.pdf) |
| 24      | [HJM利率和信贷模型（PDF）](https://ocw.mit.edu/courses/mathematics/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/lecture-notes/MIT18_S096F13_lecnote24.pdf) |
| 25      | [罗斯恢复定理（PDF）](https://ocw.mit.edu/courses/mathematics/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/lecture-notes/MIT18_S096F13_lecnote25.pdf) |
| 26      | [交易对手信用风险结论简介（PDF）](https://ocw.mit.edu/courses/mathematics/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/lecture-notes/MIT18_S096F13_lecnote26.pdf) |

# signal & processing

以下注释主要是讲座视频中看到的幻灯片和演示板的静止图像。它们可用于参考每个讲座的内容。

| LEC编号 | 主题                                 | 演讲笔记                                                     |
| :------ | :----------------------------------- | :----------------------------------------------------------- |
| 1个     | 介绍                                 | （[PDF](https://ocw.mit.edu/resources/res-6-007-signals-and-systems-spring-2011/lecture-notes/MITRES_6_007S11_lec01.pdf)） |
| 2       | 信号与系统：第一部分                 | （![此资源可能无法在屏幕阅读器中正确呈现。](software%20design.assets/inacessible.gif)[PDF](https://ocw.mit.edu/resources/res-6-007-signals-and-systems-spring-2011/lecture-notes/MITRES_6_007S11_lec02.pdf)） |
| 3       | 信号和系统：第二部分                 | （![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[PDF](https://ocw.mit.edu/resources/res-6-007-signals-and-systems-spring-2011/lecture-notes/MITRES_6_007S11_lec03.pdf)） |
| 4       | 卷积                                 | （![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[PDF](https://ocw.mit.edu/resources/res-6-007-signals-and-systems-spring-2011/lecture-notes/MITRES_6_007S11_lec04.pdf)） |
| 5       | 线性时不变系统的性质                 | （![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[PDF](https://ocw.mit.edu/resources/res-6-007-signals-and-systems-spring-2011/lecture-notes/MITRES_6_007S11_lec05.pdf)） |
| 6       | 用微分和差分方程表示的系统           | （![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[PDF](https://ocw.mit.edu/resources/res-6-007-signals-and-systems-spring-2011/lecture-notes/MITRES_6_007S11_lec06.pdf)） |
| 7       | 连续时间傅立叶级数                   | （![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[PDF](https://ocw.mit.edu/resources/res-6-007-signals-and-systems-spring-2011/lecture-notes/MITRES_6_007S11_lec07.pdf)） |
| 8       | 连续时间傅立叶变换                   | （![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[PDF](https://ocw.mit.edu/resources/res-6-007-signals-and-systems-spring-2011/lecture-notes/MITRES_6_007S11_lec08.pdf)） |
| 9       | 傅立叶变换特性                       | （![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[PDF](https://ocw.mit.edu/resources/res-6-007-signals-and-systems-spring-2011/lecture-notes/MITRES_6_007S11_lec09.pdf)） |
| 10      | 离散傅立叶级数                       | （![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[PDF](https://ocw.mit.edu/resources/res-6-007-signals-and-systems-spring-2011/lecture-notes/MITRES_6_007S11_lec10.pdf)） |
| 11      | 离散傅立叶变换                       | （![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[PDF](https://ocw.mit.edu/resources/res-6-007-signals-and-systems-spring-2011/lecture-notes/MITRES_6_007S11_lec11.pdf)） |
| 12      | 筛选                                 | （![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[PDF](https://ocw.mit.edu/resources/res-6-007-signals-and-systems-spring-2011/lecture-notes/MITRES_6_007S11_lec12.pdf)） |
| 13      | 连续时间调制                         | （![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[PDF](https://ocw.mit.edu/resources/res-6-007-signals-and-systems-spring-2011/lecture-notes/MITRES_6_007S11_lec13.pdf)） |
| 14      | 调幅演示                             | （![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[PDF](https://ocw.mit.edu/resources/res-6-007-signals-and-systems-spring-2011/lecture-notes/MITRES_6_007S11_lec14.pdf)） |
| 15      | 离散时间调制                         | （![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[PDF](https://ocw.mit.edu/resources/res-6-007-signals-and-systems-spring-2011/lecture-notes/MITRES_6_007S11_lec15.pdf)） |
| 16      | 采样                                 | （![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[PDF](https://ocw.mit.edu/resources/res-6-007-signals-and-systems-spring-2011/lecture-notes/MITRES_6_007S11_lec16.pdf)） |
| 17      | 插补                                 | （![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[PDF](https://ocw.mit.edu/resources/res-6-007-signals-and-systems-spring-2011/lecture-notes/MITRES_6_007S11_lec17.pdf)） |
| 18岁    | 连续时间信号的离散时间处理           | （![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[PDF](https://ocw.mit.edu/resources/res-6-007-signals-and-systems-spring-2011/lecture-notes/MITRES_6_007S11_lec18.pdf)） |
| 19      | 离散时间采样                         | （![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[PDF](https://ocw.mit.edu/resources/res-6-007-signals-and-systems-spring-2011/lecture-notes/MITRES_6_007S11_lec19.pdf)） |
| 20      | 拉普拉斯变换                         | （![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[PDF](https://ocw.mit.edu/resources/res-6-007-signals-and-systems-spring-2011/lecture-notes/MITRES_6_007S11_lec20.pdf)） |
| 21      | 连续时间二阶系统                     | （![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[PDF](https://ocw.mit.edu/resources/res-6-007-signals-and-systems-spring-2011/lecture-notes/MITRES_6_007S11_lec21.pdf)） |
| 22      | z转换                                | （![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[PDF](https://ocw.mit.edu/resources/res-6-007-signals-and-systems-spring-2011/lecture-notes/MITRES_6_007S11_lec22.pdf)） |
| 23      | 将连续时间过滤器映射到离散时间过滤器 | （![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[PDF](https://ocw.mit.edu/resources/res-6-007-signals-and-systems-spring-2011/lecture-notes/MITRES_6_007S11_lec23.pdf)） |
| 24      | 巴特沃思过滤器                       | （![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[PDF](https://ocw.mit.edu/resources/res-6-007-signals-and-systems-spring-2011/lecture-notes/MITRES_6_007S11_lec24.pdf)） |
| 25      | 反馈                                 | （![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[PDF](https://ocw.mit.edu/resources/res-6-007-signals-and-systems-spring-2011/lecture-notes/MITRES_6_007S11_lec25.pdf)） |
| 26      | 反馈示例：倒立摆                     | （![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[PDF](https://ocw.mit.edu/resources/res-6-007-signals-and-systems-spring-2011/lecture-notes/MITRES_6_007S11_lec26.pdf)） |

# 編譯原理

本节包含选定的讲义。前一个学期的音频和视频讲座可在2005年秋季的“ 6.035[讲座笔记”](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-035-computer-language-engineering-sma-5502-fall-2005/lecture-notes)部分中找到。

| SES编号 | 主题                                 | 演讲笔记                                                     |
| :------ | :----------------------------------- | :----------------------------------------------------------- |
| 1个     | 介绍                                 | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-035-computer-language-engineering-spring-2010/lecture-notes/MIT6_035S10_lec01.pdf)） |
| 2       | 使用正则表达式和无上下文语法指定语言 | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-035-computer-language-engineering-spring-2010/lecture-notes/MIT6_035S10_lec02.pdf)） |
| 3       | 移位减少解析简介解析表构造           | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-035-computer-language-engineering-spring-2010/lecture-notes/MIT6_035S10_lec03.pdf)）（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-035-computer-language-engineering-spring-2010/lecture-notes/MIT6_035S10_lec03b.pdf)） |
| 4       | 自上而下的解析                       | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-035-computer-language-engineering-spring-2010/lecture-notes/MIT6_035S10_lec04.pdf)） |
| 5       | 中间格式                             | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-035-computer-language-engineering-spring-2010/lecture-notes/MIT6_035S10_lec05.pdf)） |
| 6       | 语义分析                             | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-035-computer-language-engineering-spring-2010/lecture-notes/MIT6_035S10_lec06.pdf)） |
| 7       | 未优化的代码生成                     | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-035-computer-language-engineering-spring-2010/lecture-notes/MIT6_035S10_lec07.pdf)） |
| 8       | 未优化的代码生成（续）               | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-035-computer-language-engineering-spring-2010/lecture-notes/MIT6_035S10_lec08.pdf)） |
| 9       | 程序分析和优化简介                   | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-035-computer-language-engineering-spring-2010/lecture-notes/MIT6_035S10_lec09.pdf)） |
| 10      | 数据流分析简介                       | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-035-computer-language-engineering-spring-2010/lecture-notes/MIT6_035S10_lec10.pdf)） |
| 11-12   | 数据流分析的基础                     | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-035-computer-language-engineering-spring-2010/lecture-notes/MIT6_035S10_lec11_12.pdf)） |
| 13      | 代码优化简介：指令调度               | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-035-computer-language-engineering-spring-2010/lecture-notes/MIT6_035S10_lec13.pdf)） |
| 14      | 循环优化：指令调度                   | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-035-computer-language-engineering-spring-2010/lecture-notes/MIT6_035S10_lec14.pdf)） |
| 15      | 更多循环优化                         | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-035-computer-language-engineering-spring-2010/lecture-notes/MIT6_035S10_lec15.pdf)） |
| 16      | 寄存器分配                           | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-035-computer-language-engineering-spring-2010/lecture-notes/MIT6_035S10_lec16.pdf)） |
| 17      | 并行化                               | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-035-computer-language-engineering-spring-2010/lecture-notes/MIT6_035S10_lec17.pdf)） |
| 18岁    | 内存优化                             | （![此资源可能无法在屏幕阅读器中正确呈现。](software%20design.assets/inacessible-1611069464510.gif)[PDF-2.5MB](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-035-computer-language-engineering-spring-2010/lecture-notes/MIT6_035S10_lec18.pdf)） |
| 19      | 全部放在一起                         |                                                              |
| 20      | 讨论编译器中的研究项目               |                                                              |

# Automata, Computability, and Complexity

| LEC编号 | 主题                                                | 演讲笔记                                                     |
| :------ | :-------------------------------------------------- | :----------------------------------------------------------- |
| 1个     | 介绍                                                | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-045j-automata-computability-and-complexity-spring-2011/lecture-notes/MIT6_045JS11_lec01.pdf)） |
| 2       | 逻辑，电路和门                                      | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-045j-automata-computability-and-complexity-spring-2011/lecture-notes/MIT6_045JS11_lec02.pdf)） |
| 3       | 确定性有限自动机（DFAs）和非确定性有限自动机（NFA） | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-045j-automata-computability-and-complexity-spring-2011/lecture-notes/MIT6_045JS11_lec03.pdf)） |
| 4       | NFA和正则表达式                                     | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-045j-automata-computability-and-complexity-spring-2011/lecture-notes/MIT6_045JS11_lec04.pdf)） |
| 5       | 非常规语言和抽水现象                                | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-045j-automata-computability-and-complexity-spring-2011/lecture-notes/MIT6_045JS11_lec05.pdf)） |
| 6       | 图灵机                                              | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-045j-automata-computability-and-complexity-spring-2011/lecture-notes/MIT6_045JS11_lec06.pdf)） |
| 7       | 可判定性                                            | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-045j-automata-computability-and-complexity-spring-2011/lecture-notes/MIT6_045JS11_lec07.pdf)） |
| 8       | 不确定的问题和邮政对应问题（PCP）                   | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-045j-automata-computability-and-complexity-spring-2011/lecture-notes/MIT6_045JS11_lec08.pdf)） |
| 9       | 映射可约性与莱斯定理                                | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-045j-automata-computability-and-complexity-spring-2011/lecture-notes/MIT6_045JS11_lec09.pdf)） |
| 10      | 自指和递归定理                                      | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-045j-automata-computability-and-complexity-spring-2011/lecture-notes/MIT6_045JS11_lec10.pdf)） |
| 11      | 密码学导论                                          | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-045j-automata-computability-and-complexity-spring-2011/lecture-notes/MIT6_045JS11_lec11.pdf)） |
| 12      | 复杂性理论                                          | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-045j-automata-computability-and-complexity-spring-2011/lecture-notes/MIT6_045JS11_lec12.pdf)） |
| 13      | 伪随机数发生器和单向函数                            | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-045j-automata-computability-and-complexity-spring-2011/lecture-notes/MIT6_045JS11_lec13.pdf)） |
| 14      | 公钥加密                                            | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-045j-automata-computability-and-complexity-spring-2011/lecture-notes/MIT6_045JS11_lec14.pdf)） |
| 15      | 更多复杂性理论                                      | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-045j-automata-computability-and-complexity-spring-2011/lecture-notes/MIT6_045JS11_lec15.pdf)） |
| 16      | NP完整性更高                                        | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-045j-automata-computability-and-complexity-spring-2011/lecture-notes/MIT6_045JS11_lec16.pdf)） |
| 17      | 概率图灵机和复杂度等级                              | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-045j-automata-computability-and-complexity-spring-2011/lecture-notes/MIT6_045JS11_lec17.pdf)） |
| 18岁    | 活板门单向功能和零知识证明                          | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-045j-automata-computability-and-complexity-spring-2011/lecture-notes/MIT6_045JS11_lec18.pdf)） |
| 19      | 大概正确（PAC）学习                                 | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-045j-automata-computability-and-complexity-spring-2011/lecture-notes/MIT6_045JS11_lec19.pdf)） |
| 20      | 更多PAC学习                                         | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-045j-automata-computability-and-complexity-spring-2011/lecture-notes/MIT6_045JS11_lec20.pdf)） |
| 21      | 量子概论                                            | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-045j-automata-computability-and-complexity-spring-2011/lecture-notes/MIT6_045JS11_lec21.pdf)） |
| 22      | 量子力学和BQP                                       | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-045j-automata-computability-and-complexity-spring-2011/lecture-notes/MIT6_045JS11_lec22.pdf)） |
| 23      | 量子算法                                            | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-045j-automata-computability-and-complexity-spring-2011/lecture-notes/MIT6_045JS11_lec23.pdf)） |

# 算法

| LEC编号 | 演讲笔记                                                     |
| :------ | :----------------------------------------------------------- |
| 1个     | ![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[引言，中位数发现（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2012/lecture-notes/MIT6_046JS12_lec01.pdf) |
| 2       | ![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[中位数查找，间隔计划（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2012/lecture-notes/MIT6_046JS12_lec02.pdf) |
| 3       | ![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[最小生成树I （PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2012/lecture-notes/MIT6_046JS12_lec03.pdf) |
| 4       | ![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[最小生成树II （PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2012/lecture-notes/MIT6_046JS12_lec04.pdf) |
| 5       | ![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[快速傅立叶变换（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2012/lecture-notes/MIT6_046JS12_lec05.pdf) |
| 6       | ![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[全对最短路径I （PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2012/lecture-notes/MIT6_046JS12_lec06.pdf) |
| 7       | ![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[全对最短路径II （PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2012/lecture-notes/MIT6_046JS12_lec07.pdf) |
| 8       | ![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[随机算法I （PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2012/lecture-notes/MIT6_046JS12_lec08.pdf) |
| 9       | ![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[随机算法II （PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2012/lecture-notes/MIT6_046JS12_lec09.pdf) |
| 10      | ![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[散列和摊销（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2012/lecture-notes/MIT6_046JS12_lec10.pdf) |
| 11      | ![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[摊销分析（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2012/lecture-notes/MIT6_046JS12_lec11.pdf) |
| 12      | ![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[竞争分析（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2012/lecture-notes/MIT6_046JS12_lec12.pdf) |
| 13      | ![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[网络流（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2012/lecture-notes/MIT6_046JS12_lec13.pdf) |
| 14      | ![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[插曲：解决问题（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2012/lecture-notes/MIT6_046JS12_lec14.pdf) |
| 15      | ![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[van Emde Boas数据结构（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2012/lecture-notes/MIT6_046JS12_lec15.pdf) |
| 16      | ![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[不相交的数据结构（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2012/lecture-notes/MIT6_046JS12_lec16.pdf) |
| 17      | ![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[复杂性和NP完整性（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2012/lecture-notes/MIT6_046JS12_lec17.pdf) |
| 18岁    | ![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[多项式时间近似（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2012/lecture-notes/MIT6_046JS12_lec18.pdf) |
| 19      | ![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[压缩和霍夫曼编码（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2012/lecture-notes/MIT6_046JS12_lec19.pdf) |
| 20      | ![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[亚线性时间算法（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2012/lecture-notes/MIT6_046JS12_lec20.pdf) |
| 21      | ![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[聚类（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2012/lecture-notes/MIT6_046JS12_lec21.pdf) |
| 22      | ![此资源可能无法在屏幕阅读器中正确呈现。](https://ocw.mit.edu/images/inacessible.gif)[去随机化（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2012/lecture-notes/MIT6_046JS12_lec22.pdf) |
| 23      | ![此资源可能无法在屏幕阅读器中正确呈现。](software%20design.assets/inacessible-1611069513779.gif)[计算几何（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2012/lecture-notes/MIT6_046JS12_lec23.pdf) |

# Introduction to Convex Optimization

| LEC编号 | 主题                                                         | 演讲笔记                                                     |
| :------ | :----------------------------------------------------------- | :----------------------------------------------------------- |
| 1个     | 介绍数学优化；最小二乘和线性规划；凸优化 课程目标和主题；非线性优化。 | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-079-introduction-to-convex-optimization-fall-2009/lecture-notes/MIT6_079F09_lec01.pdf)） |
| 2       | 凸集凸台和圆锥；一些常见和重要的例子；保留凸度的操作。       | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-079-introduction-to-convex-optimization-fall-2009/lecture-notes/MIT6_079F09_lec02.pdf)） |
| 3       | 凸函数凸函数；常见的例子；保留凸度的操作；拟凸和对数凸函数。 | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-079-introduction-to-convex-optimization-fall-2009/lecture-notes/MIT6_079F09_lec03.pdf)） |
| 4       | 凸优化问题凸优化问题；线性和二次程序；二阶锥和半定程序；拟凸优化问题；向量和多准则优化。 | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-079-introduction-to-convex-optimization-fall-2009/lecture-notes/MIT6_079F09_lec04.pdf)） |
| 5       | 二元性拉格朗日对偶函数和问题；示例和应用程序。               | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-079-introduction-to-convex-optimization-fall-2009/lecture-notes/MIT6_079F09_lec05.pdf)） |
| 6       | 逼近和拟合范数逼近；正规化；强大的优化。                     | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-079-introduction-to-convex-optimization-fall-2009/lecture-notes/MIT6_079F09_lec06.pdf)） |
| 7       | 统计估计最大似然和MAP估计；探测器设计；实验设计。            | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-079-introduction-to-convex-optimization-fall-2009/lecture-notes/MIT6_079F09_lec07.pdf)） |
| 8       | 几何问题投影; 极体椭球; 定心; 分类; 放置和位置问题。         | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-079-introduction-to-convex-optimization-fall-2009/lecture-notes/MIT6_079F09_lec08.pdf)） |
| 9       | 滤波器设计和均衡FIR滤波器 通用和对称低通滤波器设计；切比雪夫均衡；通过频谱分解进行幅度设计。 | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-079-introduction-to-convex-optimization-fall-2009/lecture-notes/MIT6_079F09_lec09.pdf)） |
| 10      | 杂项应用多周期处理器速度调度；最短时间最佳控制；抓力优化；最佳广播发射机功率分配；相控阵天线波束成形；最佳接收器位置。 | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-079-introduction-to-convex-optimization-fall-2009/lecture-notes/MIT6_079F09_lec10.pdf)） |
| 11      | *l* 1个凸基数问题的方法凸基数问题和例子；*l* 1启发式；解释为放松。 | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-079-introduction-to-convex-optimization-fall-2009/lecture-notes/MIT6_079F09_lec11.pdf)） |
| 12      | *l* 1个解决凸基数问题的方法（续）总变异重建；迭代重新加权*l* 1；秩最小化和双重频谱范式启发式。 | （[PDF-1.4MB](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-079-introduction-to-convex-optimization-fall-2009/lecture-notes/MIT6_079F09_lec12.pdf)） |
| 13      | 随机编程随机编程；“等价性”问题；违反/短缺限制和处罚；蒙特卡洛采样方法；验证。 | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-079-introduction-to-convex-optimization-fall-2009/lecture-notes/MIT6_079F09_lec13.pdf)） |
| 14      | 机会约束优化机会约束和百分位优化；对数凹面分布的机会约束；机会约束的凸近似。 | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-079-introduction-to-convex-optimization-fall-2009/lecture-notes/MIT6_079F09_lec14.pdf)） |
| 15      | 数值线性代数背景基本线性代数运算；因子分解法 稀疏矩阵方法。  | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-079-introduction-to-convex-optimization-fall-2009/lecture-notes/MIT6_079F09_lec15.pdf)） |
| 16      | 无约束最小化梯度和最陡下降法；牛顿法 自一致性复杂度分析。    | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-079-introduction-to-convex-optimization-fall-2009/lecture-notes/MIT6_079F09_lec16.pdf)） |
| 17      | 等式约束最小化消除方法；牛顿法 不可行的牛顿法。              | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-079-introduction-to-convex-optimization-fall-2009/lecture-notes/MIT6_079F09_lec17.pdf)） |
| 18岁    | 内点法屏障法；顺序无约束最小化；自一致性复杂度分析。         | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-079-introduction-to-convex-optimization-fall-2009/lecture-notes/MIT6_079F09_lec18.pdf)） |
| 19      | 纪律凸编程和CVX凸优化求解器；建模系统；严格的凸规划；CVX。   | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-079-introduction-to-convex-optimization-fall-2009/lecture-notes/MIT6_079F09_lec19.pdf)） |
| 20      | 结论                                                         |                                                              |

# 理论计算机科学的伟大思想

| LEC编号 | 主题                                                         |
| :------ | :----------------------------------------------------------- |
| 1个     | 简介（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-080-great-ideas-in-theoretical-computer-science-spring-2008/lecture-notes/lec1.pdf)） |
| 2       | 逻辑（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-080-great-ideas-in-theoretical-computer-science-spring-2008/lecture-notes/lec2.pdf)） |
| 3       | 电路和有限自动机（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-080-great-ideas-in-theoretical-computer-science-spring-2008/lecture-notes/lec3.pdf)） |
| 4       | 图灵机（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-080-great-ideas-in-theoretical-computer-science-spring-2008/lecture-notes/lec4.pdf)） |
| 5       | 还原性和哥德尔（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-080-great-ideas-in-theoretical-computer-science-spring-2008/lecture-notes/lec5.pdf)） |
| 6       | 思想和机器（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-080-great-ideas-in-theoretical-computer-science-spring-2008/lecture-notes/lec6.pdf)） |
| 7       | 复杂性（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-080-great-ideas-in-theoretical-computer-science-spring-2008/lecture-notes/lec7.pdf)） |
| 8       | 多项式时间（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-080-great-ideas-in-theoretical-computer-science-spring-2008/lecture-notes/lec8.pdf)） |
| 9       | P和NP（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-080-great-ideas-in-theoretical-computer-science-spring-2008/lecture-notes/lec9.pdf)） |
| 10      | NP完整性（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-080-great-ideas-in-theoretical-computer-science-spring-2008/lecture-notes/lec10.pdf)） |
| 11      | 实际中的NP完整性（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-080-great-ideas-in-theoretical-computer-science-spring-2008/lecture-notes/lec11.pdf)） |
| 12      | 空间复杂性及更多（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-080-great-ideas-in-theoretical-computer-science-spring-2008/lecture-notes/lec12.pdf)） |
| 13      | 随机性（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-080-great-ideas-in-theoretical-computer-science-spring-2008/lecture-notes/lec13.pdf)） |
| 14      | 概率复杂度类（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-080-great-ideas-in-theoretical-computer-science-spring-2008/lecture-notes/lec14.pdf)） |
| 15      | 非随机化/加密双重功能（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-080-great-ideas-in-theoretical-computer-science-spring-2008/lecture-notes/lec15.pdf)） |
| 16      | 私钥加密（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-080-great-ideas-in-theoretical-computer-science-spring-2008/lecture-notes/lec16.pdf)） |
| 17      | 公钥加密（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-080-great-ideas-in-theoretical-computer-science-spring-2008/lecture-notes/lec17.pdf)） |
| 18岁    | 加密协议（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-080-great-ideas-in-theoretical-computer-science-spring-2008/lecture-notes/lec18.pdf)） |
| 19      | 互动式证明/机器学习（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-080-great-ideas-in-theoretical-computer-science-spring-2008/lecture-notes/lec19.pdf)） |
| 20      | 大概正确（PAC）学习（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-080-great-ideas-in-theoretical-computer-science-spring-2008/lecture-notes/lec20.pdf)） |
| 21      | 学习，乔姆斯基，RSA，量子（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-080-great-ideas-in-theoretical-computer-science-spring-2008/lecture-notes/lec21.pdf)） |
| 22-23   | 量子计算（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-080-great-ideas-in-theoretical-computer-science-spring-2008/lecture-notes/lec22_23.pdf)） |
| 24      | 量子算法（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-080-great-ideas-in-theoretical-computer-science-spring-2008/lecture-notes/lec24.pdf)） |

# C内存管理和C ++面向对象编程简介

| SES编号 | 主题                                                         | 演讲笔记                                                     | 支持文件                                                     |
| :------ | :----------------------------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| 1个     | 使用C / C ++的动机；讨论C和C ++在抽象层次结构中的位置；编写我们的第一个C程序 | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-088-introduction-to-c-memory-management-and-c-object-oriented-programming-january-iap-2010/lecture-notes/MIT6_088IAP10_lec01.pdf)） |                                                              |
| 2       | C语言中内存操作的后勤（指针，结构）                          | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-088-introduction-to-c-memory-management-and-c-object-oriented-programming-january-iap-2010/lecture-notes/MIT6_088IAP10_lec02.pdf)） | （[ZIP](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-088-introduction-to-c-memory-management-and-c-object-oriented-programming-january-iap-2010/lecture-notes/lec02.zip)）（此ZIP文件包含：1个.c文件和1个.h文件。） |
| 3       | 用C语言进行更高级的内存操作。我们将显示双链表插入到位，使用双指针插入链表，使用内存的极端情况（当我们实际上需要堆分配时），等等。 | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-088-introduction-to-c-memory-management-and-c-object-oriented-programming-january-iap-2010/lecture-notes/MIT6_088IAP10_lec03.pdf)） |                                                              |
| 4       | C ++简介；封装：类，名称空间，构造函数和析构函数；C ++中的内存管理（新增，删除）；操作员重载和标准输入/输出 | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-088-introduction-to-c-memory-management-and-c-object-oriented-programming-january-iap-2010/lecture-notes/MIT6_088IAP10_lec04.pdf)） | （[ZIP](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-088-introduction-to-c-memory-management-and-c-object-oriented-programming-january-iap-2010/lecture-notes/lec04.zip)）（此Zip文件包含：3个.cc文件和2个.h文件。） |
| 5       | 继承和多态性；模板；标准库容器                               | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-088-introduction-to-c-memory-management-and-c-object-oriented-programming-january-iap-2010/lecture-notes/MIT6_088IAP10_lec05.pdf)） | （[ZIP](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-088-introduction-to-c-memory-management-and-c-object-oriented-programming-january-iap-2010/lecture-notes/lec05.zip)）（此ZIP文件包含：4个.cc文件和3个.h文件。） |
| 6       | 交易技巧。人们在访谈等中可能看到的东西。复习和讨论所涉及的主题，问答。 | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-088-introduction-to-c-memory-management-and-c-object-oriented-programming-january-iap-2010/lecture-notes/MIT6_088IAP10_lec06.pdf)） |                                                              |

# 軟件工程

| SES编号    | 主题                                | 演讲笔记                                                     |
| :--------- | :---------------------------------- | :----------------------------------------------------------- |
| **第一周** |                                     |                                                              |
| L1         | 介绍                                | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-170-laboratory-in-software-engineering-fall-2005/lecture-notes/lec1.pdf)） |
| L2         | 对象语义                            | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-170-laboratory-in-software-engineering-fall-2005/lecture-notes/lec2.pdf)） |
| **第二周** |                                     |                                                              |
| L3         | 子类化                              | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-170-laboratory-in-software-engineering-fall-2005/lecture-notes/lec3.pdf)） |
| L4         | 技术指标                            | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-170-laboratory-in-software-engineering-fall-2005/lecture-notes/lec4.pdf)） |
| L5         | 测验                                | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-170-laboratory-in-software-engineering-fall-2005/lecture-notes/lec5.pdf)） |
| **第三周** |                                     |                                                              |
| L6         | 对象模型符号代码摘要                | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-170-laboratory-in-software-engineering-fall-2005/lecture-notes/lec6.pdf)）（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-170-laboratory-in-software-engineering-fall-2005/lecture-notes/lec6_summary.pdf)） |
| L7         | ADT简介                             | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-170-laboratory-in-software-engineering-fall-2005/lecture-notes/lec7.pdf)） |
| **第四周** |                                     |                                                              |
| L8         | 表示不变式                          | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-170-laboratory-in-software-engineering-fall-2005/lecture-notes/lec8.pdf)） |
| L9         | 抽象功能                            | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-170-laboratory-in-software-engineering-fall-2005/lecture-notes/lec9.pdf)） |
| L10        | 依赖关系和去耦                      | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-170-laboratory-in-software-engineering-fall-2005/lecture-notes/lec10.pdf)） |
| **第五周** |                                     |                                                              |
| L11        | 例外情况                            | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-170-laboratory-in-software-engineering-fall-2005/lecture-notes/lec11.pdf)） |
| L12        | 平等                                | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-170-laboratory-in-software-engineering-fall-2005/lecture-notes/lec12.pdf)） |
| L13        | 多态性：Gilad Bracha的客座演讲      |                                                              |
| **第六周** |                                     |                                                              |
| L14        | 子类型和子类                        | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-170-laboratory-in-software-engineering-fall-2005/lecture-notes/lec14.pdf)） |
| **第七周** |                                     |                                                              |
| L15        | 类和接口                            | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-170-laboratory-in-software-engineering-fall-2005/lecture-notes/lec15.pdf)） |
| L16        | 可用性1                             | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-170-laboratory-in-software-engineering-fall-2005/lecture-notes/lec16.pdf)）（由Robert Miller教授提供。经许可使用。） |
| L17        | 可用性2                             | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-170-laboratory-in-software-engineering-fall-2005/lecture-notes/lec17.pdf)）（由Robert Miller教授提供。经许可使用。） |
| **第八周** |                                     |                                                              |
| L18        | 设计模式                            | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-170-laboratory-in-software-engineering-fall-2005/lecture-notes/lec18.pdf)） |
| L19        | 设计项目经验1                       | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-170-laboratory-in-software-engineering-fall-2005/lecture-notes/lec19.pdf)） |
| L20        | 设计项目经验2                       | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-170-laboratory-in-software-engineering-fall-2005/lecture-notes/lec20.pdf)） |
| **第十周** |                                     |                                                              |
| L21        | 管理小型软件团队                    | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-170-laboratory-in-software-engineering-fall-2005/lecture-notes/lec21.pdf)）（由Corey McCaffrey提供。经许可使用。） |
| **第11周** |                                     |                                                              |
| L22        | Joshua Bloch和Neal Gafter的客座演讲 |                                                              |

# 软件系统性能工程

| 主题 |                                                              |
| :--- | ------------------------------------------------------------ |
| 1个  | [简介和矩阵乘法（PDF-6.9MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-172-performance-engineering-of-software-systems-fall-2018/lecture-slides/MIT6_172F18_lec1.pdf) |
| 2    | [Bentley优化工作规则（PDF-3.5 MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-172-performance-engineering-of-software-systems-fall-2018/lecture-slides/MIT6_172F18_lec2.pdf) |
| 3    | [比特黑客（PDF-2.3MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-172-performance-engineering-of-software-systems-fall-2018/lecture-slides/MIT6_172F18_lec3.pdf) |
| 4    | [汇编语言和计算机体系结构（PDF-6.4MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-172-performance-engineering-of-software-systems-fall-2018/lecture-slides/MIT6_172F18_lec4.pdf) |
| 5    | [C到汇编（PDF-6.5MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-172-performance-engineering-of-software-systems-fall-2018/lecture-slides/MIT6_172F18_lec5.pdf) |
| 6    | [多核编程（PDF-4.4MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-172-performance-engineering-of-software-systems-fall-2018/lecture-slides/MIT6_172F18_lec6.pdf) |
| 7    | [种族与平行性（PDF-4.4MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-172-performance-engineering-of-software-systems-fall-2018/lecture-slides/MIT6_172F18_lec7.pdf) |
| 8    | [多线程算法分析（PDF-6.3MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-172-performance-engineering-of-software-systems-fall-2018/lecture-slides/MIT6_172F18_lec8.pdf) |
| 9    | [编译器可以做什么和不能做什么（PDF-7.4MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-172-performance-engineering-of-software-systems-fall-2018/lecture-slides/MIT6_172F18_lec9.pdf) |
| 10   | [测量和时序（PDF-1.6MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-172-performance-engineering-of-software-systems-fall-2018/lecture-slides/MIT6_172F18_lec10.pdf) |
| 11   | [储存空间分配（PDF-3.3MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-172-performance-engineering-of-software-systems-fall-2018/lecture-slides/MIT6_172F18_lec11.pdf) |
| 12   | [并行存储分配（PDF-2.5MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-172-performance-engineering-of-software-systems-fall-2018/lecture-slides/MIT6_172F18_lec12.pdf) |
| 13   | [民间运行系统（PDF-4.7MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-172-performance-engineering-of-software-systems-fall-2018/lecture-slides/MIT6_172F18_lec13.pdf) |
| 14   | [缓存和高效缓存算法（PDF-2.8MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-172-performance-engineering-of-software-systems-fall-2018/lecture-slides/MIT6_172F18_lec14.pdf) |
| 15   | [高速缓存无关的算法（PDF-3.2MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-172-performance-engineering-of-software-systems-fall-2018/lecture-slides/MIT6_172F18_lec15.pdf) |
| 16   | [非确定性并行编程（PDF-3.3MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-172-performance-engineering-of-software-systems-fall-2018/lecture-slides/MIT6_172F18_lec16.pdf) |
| 17   | [无锁同步（PDF-3.3MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-172-performance-engineering-of-software-systems-fall-2018/lecture-slides/MIT6_172F18_lec17.pdf) |
| 18岁 | [领域特定语言和自动调整（PDF-4.6MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-172-performance-engineering-of-software-systems-fall-2018/lecture-slides/MIT6_172F18_lec18.pdf) |
| 19   | [Leiserchess Codewalk（PDF-6.4MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-172-performance-engineering-of-software-systems-fall-2018/lecture-slides/MIT6_172F18_lec19.pdf) |
| 20   | [投机性平行与束缚（PDF-6.2MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-172-performance-engineering-of-software-systems-fall-2018/lecture-slides/MIT6_172F18_lec20.pdf) |
| 21   | [调整TSP算法（PDF-1.6MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-172-performance-engineering-of-software-systems-fall-2018/lecture-slides/MIT6_172F18_lec21.pdf) |
| 22   | [图形优化（PDF-2.9MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-172-performance-engineering-of-software-systems-fall-2018/lecture-slides/MIT6_172F18_lec22.pdf) |
| 23   | [动态语言的高性能（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-172-performance-engineering-of-software-systems-fall-2018/lecture-slides/MIT6_172F18_lec23.pdf) |

# 多核编程入门

- [视频讲座](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-189-multicore-programming-primer-january-iap-2007/lecture-notes-and-video)
- [字幕/笔录](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-189-multicore-programming-primer-january-iap-2007/lecture-notes-and-video/)
- [课堂比赛-视频](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-189-multicore-programming-primer-january-iap-2007/projects)
- [专题-视频](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-189-multicore-programming-primer-january-iap-2007/recitations)
- [选定的讲义](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-189-multicore-programming-primer-january-iap-2007/lecture-notes-and-video)
- [项目（无示例）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-189-multicore-programming-primer-january-iap-2007/projects)

# Dynamic Programming and Stochastic Control

| LEC编号                                                      | 主题                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| **有限期问题**                                               |                                                              |
| [讲座1（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-231-dynamic-programming-and-stochastic-control-fall-2015/lecture-notes/MIT6_231F15_Lec1.pdf) | 动态编程导论动态编程的例子反馈的意义                         |
| [讲座2（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-231-dynamic-programming-and-stochastic-control-fall-2015/lecture-notes/MIT6_231F15_Lec2.pdf) | 基本问题最优原则通用动态规划算法状态增强                     |
| [讲座3（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-231-dynamic-programming-and-stochastic-control-fall-2015/lecture-notes/MIT6_231F15_Lec3.pdf) | 确定性有限状态问题向后最短路径算法前向最短路径算法替代最短路径算法 |
| [讲座4（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-231-dynamic-programming-and-stochastic-control-fall-2015/lecture-notes/MIT6_231F15_Lec4.pdf) | 随机动态规划问题的例子线性二次问题库存控制                   |
| [讲座5（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-231-dynamic-programming-and-stochastic-control-fall-2015/lecture-notes/MIT6_231F15_Lec5.pdf) | 停止问题安排问题最小最大控制                                 |
| [讲座6（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-231-dynamic-programming-and-stochastic-control-fall-2015/lecture-notes/MIT6_231F15_Lec6.pdf) | 状态信息不完善的问题简化到完美状态信息Cas线性二次问题估计与控制分离 |
| [讲座7（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-231-dynamic-programming-and-stochastic-control-fall-2015/lecture-notes/MIT6_231F15_Lec7.pdf) | 状态信息不完善足够的统计有条件的状态分布作为充分的统计量有限状态分析 |
| [讲座8（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-231-dynamic-programming-and-stochastic-control-fall-2015/lecture-notes/MIT6_231F15_Lec8.pdf) | 次优控制成本估算方法：分类确定性等效控制有限的超前政策绩效界限问题近似法参数成本估算 |
| [讲座9（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-231-dynamic-programming-and-stochastic-control-fall-2015/lecture-notes/MIT6_231F15_Lec9.pdf) | 推出算法成本改善特性离散确定性问题推出算法的近似值模型预测控制（MPS）连续时间离散化连续空间的离散化其他次优方法 |
| **简单的无限地平线问题**                                     |                                                              |
| [讲座10（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-231-dynamic-programming-and-stochastic-control-fall-2015/lecture-notes/MIT6_231F15_Lec10.pdf) | 无限地平线问题随机最短路径（SSP）问题贝尔曼方程动态编程–值迭代贴现问题作为SSP的特例 |
| [讲座11（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-231-dynamic-programming-and-stochastic-control-fall-2015/lecture-notes/MIT6_231F15_Lec11.pdf) | 随机最短路径问题综述SSP的计算方法贴现问题的计算方法          |
| [讲座12（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-231-dynamic-programming-and-stochastic-control-fall-2015/lecture-notes/MIT6_231F15_Lec12.pdf) | 每阶段平均成本问题与随机最短路径问题的联系贝尔曼方程价值迭代，策略迭代 |
| [讲座13（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-231-dynamic-programming-and-stochastic-control-fall-2015/lecture-notes/MIT6_231F15_Lec13.pdf) | 连续时间马尔可夫链的控制：半马尔可夫问题问题表述：等价于离散问题折扣问题平均成本问题 |
| **高级无限视野问题**                                         |                                                              |
| [讲座14（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-231-dynamic-programming-and-stochastic-control-fall-2015/lecture-notes/MIT6_231F15_Lec14.pdf) | 高级无限视界动态规划和逼近方法简介                           |
| [讲座15（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-231-dynamic-programming-and-stochastic-control-fall-2015/lecture-notes/MIT6_231F15_Lec15.pdf) | 贴现问题基本理论述评收缩特性的单调性动态规划中的收缩映射折扣问题：具有无限成本的可数状态空间广义折扣动态规划抽象动态编程简介 |
| [讲座16（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-231-dynamic-programming-and-stochastic-control-fall-2015/lecture-notes/MIT6_231F15_Lec16.pdf) | 贴现问题计算理论的回顾值迭代（VI）策略迭代（PI）乐观的PI广义折扣动态规划的计算方法异步算法 |
| [讲座17（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-231-dynamic-programming-and-stochastic-control-fall-2015/lecture-notes/MIT6_231F15_Lec17.pdf) | 未打折的问题随机最短路径问题正确与不正确的政策SSP的分析与计算方法SSP的病理弱条件下的SSP |
| [讲座18（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-231-dynamic-programming-and-stochastic-control-fall-2015/lecture-notes/MIT6_231F15_Lec18.pdf) | 未折现的总成本问题正负成本问题确定性最优成本问题自适应（线性二次）动态编程仿射单论和风险敏感性问题 |
| [讲座19（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-231-dynamic-programming-and-stochastic-control-fall-2015/lecture-notes/MIT6_231F15_Lec19.pdf) | 近似动态编程简介政策空间中的近似价值空间中的逼近，基于部署/模拟的单策略迭代使用问题逼近在值空间中逼近 |
| [讲座20（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-231-dynamic-programming-and-stochastic-control-fall-2015/lecture-notes/MIT6_231F15_Lec20.pdf) | 折扣问题近似（拟合）VI近似PI投影方程收缩特性：误差范围投影方程的矩阵形式基于仿真的实现LSTD，LSPE和TD方法 |
| [讲座21（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-231-dynamic-programming-and-stochastic-control-fall-2015/lecture-notes/MIT6_231F15_Lec21.pdf) | 近似策略迭代的审查政策评估的投影方程法基于仿真的实现问题，多步投影方程法偏差-偏差权衡探索增强的实现，振荡 |
| [演讲22（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-231-dynamic-programming-and-stochastic-control-fall-2015/lecture-notes/MIT6_231F15_Lec22.pdf) | 聚合作为一种近似方法汇总问题基于模拟的聚合Q学习              |
| [讲座23（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-231-dynamic-programming-and-stochastic-control-fall-2015/lecture-notes/MIT6_231F15_Lec23.pdf) | 高级动态编程中的其他主题随机最短路径问题平均成本问题概论基本功能适应策略空间中基于梯度的近似概述 |



https://ocw.mit.edu/courses/mathematics/18-335j-introduction-to-numerical-methods-spring-2019/week-1/index.htm

https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-801-machine-vision-fall-2004/lecture-notes/

https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-831-user-interface-design-and-implementation-spring-2011/lecture-notes/

https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-823-computer-system-architecture-fall-2005/lecture-notes/

（A）：由Arvind教授讲授的课程
（J）：由Joel Emer博士讲授的课程

| SES编号   | 主题                                                         |
| :-------- | :----------------------------------------------------------- |
| **模块1** |                                                              |
| L1        | 计算和计算机体系结构的历史（A）（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-823-computer-system-architecture-fall-2005/lecture-notes/l01_earlydev.pdf)） |
| L2        | 技术和软件对指令集的影响：直到IBM 360（A）到来（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-823-computer-system-architecture-fall-2005/lecture-notes/l02_fifties.pdf)） |
| L3        | 六十年代复杂指令集的演进：堆栈和GPR架构（A）（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-823-computer-system-architecture-fall-2005/lecture-notes/l03_sixties.pdf)） |
| L4        | 微程序设计（A）（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-823-computer-system-architecture-fall-2005/lecture-notes/l04_microprog.pdf)） |
| L5        | 简单指令流水线（A）（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-823-computer-system-architecture-fall-2005/lecture-notes/l05_singlecycle.pdf)） |
| L6        | 管道危害（A）（![此资源可能无法在屏幕阅读器中正确呈现。](software%20design.assets/inacessible-1611070575714.gif)[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-823-computer-system-architecture-fall-2005/lecture-notes/l06_pipeline.pdf)） |
| **模块2** |                                                              |
| L7        | 多级内存-技术（J）（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-823-computer-system-architecture-fall-2005/lecture-notes/l07_caches.pdf)） |
| L8        | 缓存（内存）性能优化（J）（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-823-computer-system-architecture-fall-2005/lecture-notes/l08_caches_2.pdf)） |
| L9        | 虚拟内存基础知识（J）（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-823-computer-system-architecture-fall-2005/lecture-notes/l09_add_trans.pdf)） |
| L10       | 虚拟内存：半双工（A）（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-823-computer-system-architecture-fall-2005/lecture-notes/l10_vrtl_mem.pdf)） |
| **模块3** |                                                              |
| L11       | 复杂流水线（A）（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-823-computer-system-architecture-fall-2005/lecture-notes/l11_cmplx_pipes.pdf)） |
| L12       | 乱序执行和寄存器重命名（A）（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-823-computer-system-architecture-fall-2005/lecture-notes/l12_ooo_pipes.pdf)） |
| L13       | 分支预测和推测执行（A）（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-823-computer-system-architecture-fall-2005/lecture-notes/l13_brnchpred.pdf)） |
| L14       | 先进的超标量架构（J）（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-823-computer-system-architecture-fall-2005/lecture-notes/l14_superscalar.pdf)） |
| L15       | 微处理器演进：4004至Pentium 4（J）（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-823-computer-system-architecture-fall-2005/lecture-notes/l15_micro_evlutn.pdf)） |
| **模块4** |                                                              |
| L16       | 同步和顺序一致性（A）（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-823-computer-system-architecture-fall-2005/lecture-notes/l16_smps_sc.pdf)） |
| L17       | 缓存一致性（A）（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-823-computer-system-architecture-fall-2005/lecture-notes/l17_cc.pdf)） |
| L18       | 缓存一致性（实现）（A）（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-823-computer-system-architecture-fall-2005/lecture-notes/l18_ccprotocols.pdf)） |
| L19       | 史努比协议（A）（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-823-computer-system-architecture-fall-2005/lecture-notes/l19_snoopy_prot.pdf)） |
| L20       | 松弛记忆模型（A）（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-823-computer-system-architecture-fall-2005/lecture-notes/l20_relaxedmm.pdf)） |
| **模块5** |                                                              |
| L21       | VLIW / EPIC：静态调度的ILP（J）（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-823-computer-system-architecture-fall-2005/lecture-notes/l21_vliw.pdf)） |
| L22       | 向量计算机（J）（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-823-computer-system-architecture-fall-2005/lecture-notes/l22_vector.pdf)） |
| L23       | 多线程处理器（J）（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-823-computer-system-architecture-fall-2005/lecture-notes/l23_multithread.pdf)） |
| L24       | 可靠的架构（J）（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-823-computer-system-architecture-fall-2005/lecture-notes/l24_reliability.pdf)） |
| L25       | 虚拟机（J）（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-823-computer-system-architecture-fall-2005/lecture-notes/l25_vms.pdf)） |

# 分佈式系統

| EC编号 | 主题                                                         | 讲义                                                         |
| :----- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| 1个    | 简介和操作系统审查（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-824-distributed-computer-systems-engineering-spring-2006/lecture-notes/lec1.pdf)） | syscall.c（[C](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-824-distributed-computer-systems-engineering-spring-2006/lecture-notes/syscall.c)）webserver.c（[C](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-824-distributed-computer-systems-engineering-spring-2006/lecture-notes/webserver.c)） |
| 2      | I / O并发（[PDF 1](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-824-distributed-computer-systems-engineering-spring-2006/lecture-notes/lec2_concurrency.pdf)）事件驱动的编程（[PDF 2](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-824-distributed-computer-systems-engineering-spring-2006/lecture-notes/lec2_events.pdf)） | events.c（[C](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-824-distributed-computer-systems-engineering-spring-2006/lecture-notes/events.c)）webclient.c（[C](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-824-distributed-computer-systems-engineering-spring-2006/lecture-notes/webclient.c)）webclient_libasync.c（[C](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-824-distributed-computer-systems-engineering-spring-2006/lecture-notes/webclient_libasync.c)） |
| 3      | 事件驱动的编程（续）（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-824-distributed-computer-systems-engineering-spring-2006/lecture-notes/lec3_events.pdf)） | arpc.c（[C](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-824-distributed-computer-systems-engineering-spring-2006/lecture-notes/arpc.c)） |
| 4      | 网络文件系统（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-824-distributed-computer-systems-engineering-spring-2006/lecture-notes/lec4_nfs.pdf)） |                                                              |
| 5      | RPC透明度（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-824-distributed-computer-systems-engineering-spring-2006/lecture-notes/lec5_rpc.pdf)） |                                                              |
| 6      | 崩溃恢复（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-824-distributed-computer-systems-engineering-spring-2006/lecture-notes/lec6_crash.pdf)） |                                                              |
| 7      | 记录（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-824-distributed-computer-systems-engineering-spring-2006/lecture-notes/lec7_logging.pdf)） |                                                              |
| 8      | 缓存一致性和锁定（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-824-distributed-computer-systems-engineering-spring-2006/lecture-notes/lec8_cache.pdf)） |                                                              |
| 9      | 内存一致性（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-824-distributed-computer-systems-engineering-spring-2006/lecture-notes/lec9_memory.pdf)） |                                                              |
| 10     | 第一次项目会议                                               |                                                              |
| 11     | 内存一致性（续）（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-824-distributed-computer-systems-engineering-spring-2006/lecture-notes/lec11_memory.pdf)） |                                                              |
| 12     | 矢量时间戳和版本矢量（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-824-distributed-computer-systems-engineering-spring-2006/lecture-notes/lec12_vector.pdf)） |                                                              |
| 13     | 两阶段提交（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-824-distributed-computer-systems-engineering-spring-2006/lecture-notes/lec13_twophase.pdf)） |                                                              |
| 14     | Paxos（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-824-distributed-computer-systems-engineering-spring-2006/lecture-notes/lec14_paxos.pdf)） |                                                              |
| 15     | 带时间戳的复制（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-824-distributed-computer-systems-engineering-spring-2006/lecture-notes/lec15_viewstamp.pdf)） |                                                              |
| 16     | 竖琴（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-824-distributed-computer-systems-engineering-spring-2006/lecture-notes/lec16_harp.pdf)） |                                                              |
| 17     | 第二次项目会议                                               |                                                              |
| 18岁   | 素馨花（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-824-distributed-computer-systems-engineering-spring-2006/lecture-notes/lec18_frangipani.pdf)） |                                                              |
| 19     | 可扩展查找（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-824-distributed-computer-systems-engineering-spring-2006/lecture-notes/lec19_scalable.pdf)） |                                                              |
| 20     | 广域存储                                                     |                                                              |
| 21     | 骇客日（无课）                                               |                                                              |
| 22     | 项目示范                                                     |                                                              |
| 23     | 内容分配                                                     |                                                              |
| 24     | 分布式计算                                                   |                                                              |

# 并行計算

| LEC编号 | 主题                                           | 档案                                                         |
| :------ | :--------------------------------------------- | :----------------------------------------------------------- |
| 1个     | 表达并行计算                                   | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-827-multithreaded-parallelism-languages-and-compilers-fall-2002/lecture-notes/L01Introduction.pdf)） |
| 2       | pH中的隐式并行编程：函数和类型                 | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-827-multithreaded-parallelism-languages-and-compilers-fall-2002/lecture-notes/L02pH_FunctionalPrint.pdf)） |
| 3       | ג-微积分：功能语言的基础                       | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-827-multithreaded-parallelism-languages-and-compilers-fall-2002/lecture-notes/L03LambdaCalculusPrint.pdf)） |
| 4       | 带有常数和Let-块的A-微积分                     | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-827-multithreaded-parallelism-languages-and-compilers-fall-2002/lecture-notes/L04LambdaLetPrint.pdf)） |
| 5       | 带Let块的ג-微积分（续）                        | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-827-multithreaded-parallelism-languages-and-compilers-fall-2002/lecture-notes/L05LambdaLet2Print.pdf)） |
| 6       | Hindley-Milner类型系统                         | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-827-multithreaded-parallelism-languages-and-compilers-fall-2002/lecture-notes/L06HindleyMilnerPrint.pdf)） |
| 7       | Hindley-Milner类型系统（续）                   | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-827-multithreaded-parallelism-languages-and-compilers-fall-2002/lecture-notes/L07HindleyMilner2Print.pdf)） |
| 8       | 列表和代数类型                                 | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-827-multithreaded-parallelism-languages-and-compilers-fall-2002/lecture-notes/L08ListsPrint.pdf)） |
| 9       | 脱糖列表理解和模式匹配                         | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-827-multithreaded-parallelism-languages-and-compilers-fall-2002/lecture-notes/L09Lists2Print.pdf)） |
| 10      | 数组编程                                       | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-827-multithreaded-parallelism-languages-and-compilers-fall-2002/lecture-notes/L10pH_ArraysPrint.pdf)） |
| 11      | I-结构和开放列表                               | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-827-multithreaded-parallelism-languages-and-compilers-fall-2002/lecture-notes/L11IstructuresPrint.pdf)） |
| 12      | M结构：使用状态和不确定性进行编程              | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-827-multithreaded-parallelism-languages-and-compilers-fall-2002/lecture-notes/L11IstructuresPrint.pdf)） |
| 13      | M结构续                                        | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-827-multithreaded-parallelism-languages-and-compilers-fall-2002/lecture-notes/L13Mstructures2Print.pdf)） |
| 14      | λS：具有副作用的Lambda微积分                   | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-827-multithreaded-parallelism-languages-and-compilers-fall-2002/lecture-notes/L14LambdaSide.pdf)） |
| 15      | 使用Monad输入和输出                            | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-827-multithreaded-parallelism-languages-and-compilers-fall-2002/lecture-notes/L15MonadsIO.pdf)） |
| 16      | 使用Monad进行结构计算                          | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-827-multithreaded-parallelism-languages-and-compilers-fall-2002/lecture-notes/L16MonadComputation.pdf)） |
| 17      | Bluespec-1：一种用于硬件设计，仿真和综合的语言 | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-827-multithreaded-parallelism-languages-and-compilers-fall-2002/lecture-notes/L17Bluespec1Print.pdf)） |
| 18岁    | Bluespec-2：Bluespec编译模型和编程简介         | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-827-multithreaded-parallelism-languages-and-compilers-fall-2002/lecture-notes/L18Bluespec2.pdf)） |
| 19      | Bluespec-3：IP查找问题                         | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-827-multithreaded-parallelism-languages-and-compilers-fall-2002/lecture-notes/L19Bluespec3.pdf)） |
| 20      | Bluespec-4：模块和类型类                       | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-827-multithreaded-parallelism-languages-and-compilers-fall-2002/lecture-notes/L20Bluespec4.pdf)） |
| 21      | Bluespec-5：编程示例                           | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-827-multithreaded-parallelism-languages-and-compilers-fall-2002/lecture-notes/L21Bluespec5Print.pdf)） |
| 22      | 术语重写系统                                   | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-827-multithreaded-parallelism-languages-and-compilers-fall-2002/lecture-notes/L22TRSPrint.pdf)） |
| 23      | ג-微积分的合流                                 | （[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-827-multithreaded-parallelism-languages-and-compilers-fall-2002/lecture-notes/L23ConfluencePrint.pdf)） |

# OS

| LEC编号 | 演讲主题和笔记                                               | 阅读和讲义                                                   |
| :------ | :----------------------------------------------------------- | :----------------------------------------------------------- |
| 1个     | [操作系统（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-828-operating-system-engineering-fall-2012/lecture-notes-and-readings/MIT6_828F12_lec1_notes.pdf) | xv6书的“第0章：操作系统接口”                                 |
| 2       | [PC硬件和x86编程（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-828-operating-system-engineering-fall-2012/lecture-notes-and-readings/MIT6_828F12_lec2_notes.pdf) | xv6书的“附录A：PC硬件”和“附录B：引导加载程序”，以及相关的xv6源文件 |
| 3       | [主要内部组件概述，系统调用界面（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-828-operating-system-engineering-fall-2012/lecture-notes-and-readings/MIT6_828F12_lec3_notes.pdf) | “第1章：第一个过程”和相关的xv6源文件                         |
| 4       | [虚拟内存（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-828-operating-system-engineering-fall-2012/lecture-notes-and-readings/MIT6_828F12_lec4_notes.pdf) | “第二章：页表”[页表翻译和寄存器（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-828-operating-system-engineering-fall-2012/lecture-notes-and-readings/MIT6_828F12_lec4_handout.pdf) |
| 5       | [中断，异常（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-828-operating-system-engineering-fall-2012/lecture-notes-and-readings/MIT6_828F12_lec5_notes.pdf) | “第3章：陷阱，中断和驱动程序”以及相关的xv6源文件[IDT（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-828-operating-system-engineering-fall-2012/lecture-notes-and-readings/MIT6_828F12_lec5_handout.pdf) |
| 6       | [多处理器和锁定（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-828-operating-system-engineering-fall-2012/lecture-notes-and-readings/MIT6_828F12_lec6_notes.pdf) | 使用spinlock.c和mp.c浏览“第4章：锁定”                        |
| 7       | [流程和转换（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-828-operating-system-engineering-fall-2012/lecture-notes-and-readings/MIT6_828F12_lec7_notes.pdf) | 使用proc.c，setjmp.S和sys_fork（在sysproc.c中）进行“第5章：计划”直至“睡眠和唤醒” |
| 8       | [睡眠与唤醒（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-828-operating-system-engineering-fall-2012/lecture-notes-and-readings/MIT6_828F12_lec8_notes.pdf) | 阅读“第5章：计划”的其余部分；读取proc.c和sys_wait，sys_exit，sys_kill的其余部分 |
| 9       | [文件系统（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-828-operating-system-engineering-fall-2012/lecture-notes-and-readings/MIT6_828F12_lec9_notes.pdf) | “第6章：文件系统”和bio.c，fs.c，sysfile.c，file.c（记录部分除外） |
| 10      | [崩溃恢复（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-828-operating-system-engineering-fall-2012/lecture-notes-and-readings/MIT6_828F12_lec10_notes.pdf) | 阅读log.c和“第6章：文件系统”的日志记录部分                   |
| 11      | [文件系统性能和快速崩溃恢复（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-828-operating-system-engineering-fall-2012/lecture-notes-and-readings/MIT6_828F12_lec11_notes.pdf) | Tweedie，[StephenC](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.307.9137)。“记录[Linux ext2fs文件系统”](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.307.9137)。[在LinuxExpo 1998上发表的论文]。 |
| 12      | 项目介绍与讨论                                               |                                                              |
| 13      | [操作系统组织（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-828-operating-system-engineering-fall-2012/lecture-notes-and-readings/MIT6_828F12_lec13_notes.pdf) | Engler，Dawson R.，M。Frans Kaashoek和James O'Toole Jr.“ [Exokernel：用于应用程序级资源管理的操作系统体系结构](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.52.2893)。” |
| 14      | 课堂骇客课程                                                 |                                                              |
| 15      | 项目会议                                                     |                                                              |
| 16      | 项目会议（续）                                               |                                                              |
| 17      | [语言/操作系统协同设计（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-828-operating-system-engineering-fall-2012/lecture-notes-and-readings/MIT6_828F12_lec17_notes.pdf) | Hunt，Galen C.和James R. Larus。“[奇点：重新思考软件堆栈](http://dx.doi.org/10.1145/1243418.1243424)。” *Microsoft Research Redmond* 41，没有。2（2007）：37-49。 |
| 测验    | 测验（打开的书和笔记）                                       |                                                              |
| 18岁    | [可伸缩锁（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-828-operating-system-engineering-fall-2012/lecture-notes-and-readings/MIT6_828F12_lec18_notes.pdf) | Boyd-Wickizer，Silas，M.Frans Kaashoek等。“[不可伸缩的锁很危险](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.261.196)。” |
| 19      | 项目会议                                                     |                                                              |
| 20      | 项目会议（续）                                               | Boyd-Wickizer，Silas，Austin T.Clements等。“ [Linux对许多核心的可伸缩性分析](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.174.5191)。” |
| 21      | [无锁协调（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-828-operating-system-engineering-fall-2012/lecture-notes-and-readings/MIT6_828F12_lec21_notes.pdf) |                                                              |
| 22      | [虚拟机（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-828-operating-system-engineering-fall-2012/lecture-notes-and-readings/MIT6_828F12_lec22_notes.pdf) | 亚当斯，基思和奥莱·艾格森。“ [x86虚拟化的软件和硬件技术比较](http://dx.doi.org/10.1145/1168857.1168860)。” *ACM数字图书馆*34，没有。5（2006）：2-13。 |
| 23      | 没有讲座；完成最终项目                                       |                                                              |
| 24      | 课堂演示                                                     |                                                              |
| 25      | 课堂上的演示（续）                                           |                                                              |

# CG

| LEC编号 | 主题                                                         |
| :------ | :----------------------------------------------------------- |
| 00      | [简介和课程概述（PDF-2.5MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-837-computer-graphics-fall-2012/lecture-notes/MIT6_837F12_Lec00.pdf) |
| 01      | [贝塞尔曲线和样条曲线（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-837-computer-graphics-fall-2012/lecture-notes/MIT6_837F12_Lec01.pdf) |
| 02      | [曲线特性和转换，表面表示（PDF-1.7MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-837-computer-graphics-fall-2012/lecture-notes/MIT6_837F12_Lec02.pdf) |
| 03      | [坐标与变换（PDF-1.5MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-837-computer-graphics-fall-2012/lecture-notes/MIT6_837F12_Lec03.pdf) |
| 04      | [分层建模（PDF-2.1MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-837-computer-graphics-fall-2012/lecture-notes/MIT6_837F12_Lec04.pdf) |
| 05      | [彩色（PDF-3.5MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-837-computer-graphics-fall-2012/lecture-notes/MIT6_837F12_Lec05.pdf) |
| 06      | [计算机动画的基础-蒙皮/封装（PDF-2.4MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-837-computer-graphics-fall-2012/lecture-notes/MIT6_837F12_Lec06.pdf) |
| 07      | [粒子系统和ODE（PDF-1.8MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-837-computer-graphics-fall-2012/lecture-notes/MIT6_837F12_Lec07.pdf) |
| 08      | [粒子系统和ODE解算器II，质量弹簧建模（PDF-1.4MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-837-computer-graphics-fall-2012/lecture-notes/MIT6_837F12_Lec08.pdf) |
| 09      | [隐式集成，碰撞检测（PDF-1.7MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-837-computer-graphics-fall-2012/lecture-notes/MIT6_837F12_Lec09.pdf) |
| 10      | [碰撞检测和响应（PDF-1.2MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-837-computer-graphics-fall-2012/lecture-notes/MIT6_837F12_Lec10.pdf) |
| 11      | [射线投射和渲染（PDF-3.2MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-837-computer-graphics-fall-2012/lecture-notes/MIT6_837F12_Lec11.pdf) |
| 12      | [射线铸造II（PDF-2.0MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-837-computer-graphics-fall-2012/lecture-notes/MIT6_837F12_Lec12.pdf) |
| 13      | [射线追踪（PDF-2.9MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-837-computer-graphics-fall-2012/lecture-notes/MIT6_837F12_Lec13.pdf) |
| 14      | [射线投射的加速结构（PDF）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-837-computer-graphics-fall-2012/lecture-notes/MIT6_837F12_Lec14.pdf) |
| 15      | [阴影和材质外观（PDF-1.8MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-837-computer-graphics-fall-2012/lecture-notes/MIT6_837F12_Lec15.pdf) |
| 16      | [纹理贴图和明暗器（PDF-2.2MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-837-computer-graphics-fall-2012/lecture-notes/MIT6_837F12_Lec16.pdf) |
| 17      | [采样，别名和Mipmap（PDF-1.6MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-837-computer-graphics-fall-2012/lecture-notes/MIT6_837F12_Lec17.pdf) |
| 18岁    | [全球照明和蒙特卡洛（PDF-2.7MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-837-computer-graphics-fall-2012/lecture-notes/MIT6_837F12_Lec18.pdf) |
| 19      | 基于图像的渲染和照明（本讲义不可用）                         |
| 20      | 输出设备（不提供讲义）                                       |
| 21      | [图形管道和栅格化（PDF-2.4MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-837-computer-graphics-fall-2012/lecture-notes/MIT6_837F12_Lec21.pdf) |
| 22      | [图形管线和栅格化II（PDF-2.2MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-837-computer-graphics-fall-2012/lecture-notes/MIT6_837F12_Lec22.pdf) |
| 23      | [实时阴影（PDF-2.8MB）](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-837-computer-graphics-fall-2012/lecture-notes/MIT6_837F12_Lec23.pdf) |
| 24      | 图形硬件和计算机游戏（不提供讲义）                           |

# 并行

| LEC编号      | 主题                                                         |
| :----------- | :----------------------------------------------------------- |
| **第一周**   |                                                              |
| 1个          | 动态多线程（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-895-theory-of-parallel-systems-sma-5509-fall-2003/lecture-notes/lecture1.pdf)）（由Ben Adida和Abhi Shelat提供。经许可使用。） |
| **第二周**   |                                                              |
| 2            | 民间，矩阵乘法和排序（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-895-theory-of-parallel-systems-sma-5509-fall-2003/lecture-notes/lecture2.pdf)） |
| 3            | 串行性能和缓存（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-895-theory-of-parallel-systems-sma-5509-fall-2003/lecture-notes/lecture3.pdf)）（由Kenneth Barr和Zardosht Kasheff提供。经许可使用。） |
| **第三周**   |                                                              |
| 4            | 确定性检测和种族检测（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-895-theory-of-parallel-systems-sma-5509-fall-2003/lecture-notes/lecture4.pdf)）（由Siddhartha Sen和Jim Sukha提供。经许可使用。） |
| 5            | 内存子系统的一致性                                           |
| **第四周**   |                                                              |
| 6            | 分析空间界限（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-895-theory-of-parallel-systems-sma-5509-fall-2003/lecture-notes/lecture6.pdf)）（由Jeremy Fineman和Siddhartha Sen提供。经许可使用。） |
| **第五周**   |                                                              |
| 7            | 内存争用（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-895-theory-of-parallel-systems-sma-5509-fall-2003/lecture-notes/lecture7.pdf)）（由Barbara Mack和C.Scott Ananian提供。经许可使用。） |
| 8            | Cilk Scheduler（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-895-theory-of-parallel-systems-sma-5509-fall-2003/lecture-notes/lecture8.pdf)）（由Barbara Mack和Kevin Matulef提供。经许可使用。） |
| **第六周**   |                                                              |
| 9            | 民间调度程序分析（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-895-theory-of-parallel-systems-sma-5509-fall-2003/lecture-notes/lecture9.pdf)）（由Alexandru Caracas和C.Scott Ananian提供。经许可使用。） |
| 10           | 民间实施（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-895-theory-of-parallel-systems-sma-5509-fall-2003/lecture-notes/lecture10.pdf)） |
| **第七周**   |                                                              |
| 11           | [项目介绍1](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-895-theory-of-parallel-systems-sma-5509-fall-2003/projects) |
| **第八周**   |                                                              |
| 12           | [项目介绍2](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-895-theory-of-parallel-systems-sma-5509-fall-2003/projects) |
| 13           | 内存一致性的实现（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-895-theory-of-parallel-systems-sma-5509-fall-2003/lecture-notes/lecture13.pdf)）（由塞思·吉尔伯特（Seth Gilbert）和谢勇提供。经许可使用。） |
| **第9周**    |                                                              |
| 14           | 竞争性Snoopy缓存                                             |
| 15           | 史努比缓存和自旋阻塞问题 手写笔记（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-895-theory-of-parallel-systems-sma-5509-fall-2003/lecture-notes/lecture15_notes.pdf)） |
| **第十周**   |                                                              |
| 16           | 超三次网络1 幻灯片（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-895-theory-of-parallel-systems-sma-5509-fall-2003/lecture-notes/lecture16_slides.pdf)） 手写笔记（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-895-theory-of-parallel-systems-sma-5509-fall-2003/lecture-notes/lecture16_notes.pdf)） |
| 17           | 超三次网络2（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-895-theory-of-parallel-systems-sma-5509-fall-2003/lecture-notes/lecture17.pdf)） |
| **第11周**   |                                                              |
| 18岁         | 超立方网络3（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-895-theory-of-parallel-systems-sma-5509-fall-2003/lecture-notes/lecture18.pdf)）（由Sriram Saroop和Wang Junqing提供。经许可使用。） 演讲幻灯片（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-895-theory-of-parallel-systems-sma-5509-fall-2003/lecture-notes/lecture18_slide.pdf)） |
| **第十二周** |                                                              |
| 19           | 压缩路由                                                     |
| 20           | 在并行磁盘上置换数据 手写说明（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-895-theory-of-parallel-systems-sma-5509-fall-2003/lecture-notes/lecture20_notes.pdf)） |
| **第13周**   |                                                              |
| 21           | 排序和排列 手写笔记（[PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-895-theory-of-parallel-systems-sma-5509-fall-2003/lecture-notes/lecture21_notes.pdf)） |
| 22           | 选择优胜者                                                   |
| **第14周**   |                                                              |
| 23           | [最终项目介绍](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-895-theory-of-parallel-systems-sma-5509-fall-2003/projects) |
| 24           | [最终项目介绍](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-895-theory-of-parallel-systems-sma-5509-fall-2003/projects) （续） |
| **第15周**   |                                                              |
| 25           | [最终项目介绍](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-895-theory-of-parallel-systems-sma-5509-fall-2003/projects) （续） |
| 26           | [最终项目介绍](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-895-theory-of-parallel-systems-sma-5509-fall-2003/projects) （续） [最终论文](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-895-theory-of-parallel-systems-sma-5509-fall-2003/projects) |