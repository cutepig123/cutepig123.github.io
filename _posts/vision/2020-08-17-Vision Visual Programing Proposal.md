---
categories: vision
---
Vision Visual Programing Proposal

# 目标

实现一个类似于外面的vvp软件的可视化编程环境，加快项目研发速度

系统要分层，

- 框架层（UI层，引擎），
- 模块层（框架接口，模块UI，模块功能）

支持多种语言编写模块，比如python，lua，c

# Proposal

UI：C++ Qt， pyQt, luaQt?

Flow File： Json

Module： 保存设置为json，保存record也为json

# 框架层（UI层，引擎）

- UI层：  --》pyQt
  - Flow: List Control --> pyQt
  - Module: Per module defined dialog --> pyQt
- Flow Engine --> pyQt
  - Flow File： Json
  - Module： 保存设置为json，保存record也为json
  - Flow execution: Python

![image-20200816110006543](Vision%20Visual%20Programing%20Proposal.assets/image-20200816110006543.png)

# 模块层（框架接口，模块UI，模块功能）

框架接口：

- 声明依赖	--》输入输出都model为一个全局表里面的数据，所以可以先不管这个
- Execute(输入，输出) --》输入输出都model为一个全局表里面的数据，所以可以先不管输入输出

```python
class AlignModule:
    def UI(cfg):pass
    def Execute(): pass
```

# QA

Q：谁负责保存这个flow？

A:框架负责，但是框架也会调用module，保存module相关的flow



Q：如何做到增加模块不需要改框架层

A：模块放到一个单独的目录，这样框架可以扫描目录获取模块列表

定义好模块接口