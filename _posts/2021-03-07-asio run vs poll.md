# asio run vs poll

## discussions

Using `io_service::poll` instead of `io_service::run` is perfectly acceptable. The difference is explained in the [documentation](http://www.boost.org/doc/libs/release/doc/html/boost_asio/reference.html#boost_asio.reference.io_service.run_one.overload1)

> The poll() function may also be used to dispatch ready handlers, but without blocking.

Note that `io_service::run` will block if there's any [`work`](http://www.boost.org/doc/libs/release/doc/html/boost_asio/reference.html#boost_asio.reference.io_service__work) left in the queue

> The work class is used to inform the io_service when work starts and finishes. This ensures that the io_service object's run() function will not exit while work is underway, and that it does exit when there is no unfinished work remaining.

whereas `io_service::poll` does not exhibit this behavior, it just invokes ready handlers. Also note that you will need to invoke [io_service::reset](http://www.boost.org/doc/libs/release/doc/html/boost_asio/reference.html#boost_asio.reference.io_service.reset) on any subsequent invocation to `io_service:run` or `io_service::poll`.

## summary

1. run: will block if there's any [`work`](http://www.boost.org/doc/libs/release/doc/html/boost_asio/reference.html#boost_asio.reference.io_service__work) left in the queue

2. poll: dispatch ready handlers, but without blocking

3. blocking vs non-blocking

   1. 所谓的blocking：除了invoke ready handlers,还会等待这些handler结束，以及继续执行ready queue里面的task
   2. 所谓的nonblocking：只是执行ready queue里面的task，但不会继续等待这些handler结束

# 如何集成到GraphApi中去

idea1： 一个graph配一个io_service. 用io_service的run()驱动graph执行

Pros:简单，容易debug。应用层是同步处理，用法简单

Cons:io_service创建的effort大不大？

~~idead2：所有graph使用同一个io_service。io_service在一个单独的线程执行。graph方面不提供同步的run函数。~~

~~Pros:~~

~~Cons:复杂，可能不好debug。由于应用层会是全异步，Mat生命周期管理会复杂一些~~


# Ref

https://stackoverflow.com/questions/4705411/boostasio-io-service-run-vs-poll-or-how-do-i-integrate-boostasio-in-ma