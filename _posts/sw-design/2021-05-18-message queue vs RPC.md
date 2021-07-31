---
categories: sw-design
---
message queue。消息队列。一般提供放东西，拿东西之类的功能 。

RPC。用户只需要声明message，和对应的处理函数。框架就自动能生成客户端代码和服务器

感觉RPC比MQ更高级一些，他的实现可以基于MQ

如何实现RPC呢，支持多线程客户端和多线程服务端的RPC？

需要什么

- command mq
- reply mq
- 客户端的一个消息接收线程
- 服务端的一个消息接收线程
- 服务端的一个或者多个消息处理线程

流程

```sequence
Client -> Client : Put id to obj-pool
Client -> Client : Put Msg+id to MQ
Client --> Server : MQ sends Msg to server
Server -> Server ThreadPool : Processing Msg
Server ThreadPool -> Server ThreadPool: Put Reply+id to MQ
Server ThreadPool --> ClientRevThd: MQ sends reply to client
ClientRevThd -> ClientRevThd: Copy the reply to obj-pool[id]. \nand set a event[id] so that client is notified
ClientRevThd -> Client: nodify client
```





