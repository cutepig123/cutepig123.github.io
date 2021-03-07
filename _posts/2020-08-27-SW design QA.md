SW design QA



Q: 当一个系统一层一层build起来的时候，有可能需要用户输入底层的参数，那么就要一层一层传递这个参数，这样导致高层的参数越来越多。如何解决这个问题？

A: 上层不应该暴露太多底层参数，否则多层的系统根本达不到封装隐藏具体实现的目的



Q: 为什么GAA Grab的API这么复杂？

A：因为他一个函数支持最复杂的用法，又有Partition抓图，partition stitching，又有Optics High level grabset转low level grabset，又有IST，又有grabsequence，又有各种post processing，又有各种优化，又有既可以grab的时候做一部分post processing，又可以packview的时候做一部分post processing

可能用build pattern处理这么复杂的东西？

