---
categories: rust
---
# [不用再担心阻塞了：受Go启发的新async-std运行时](https://async.rs/blog/stop-worrying-about-blocking-the-new-async-std-runtime/)

[斯捷潘·格拉维纳](https://twitter.com/stjepang)（[Stjepan Glavina）](https://twitter.com/stjepang)发表于2019年12月16日在

- [释放](https://async.rs/blog/tags/release)
- [公告](https://async.rs/blog/tags/announcement)
- [圣诞](https://async.rs/blog/tags/christmas)

`async-std`是Rust标准库向`async/await`新世界发展的成熟和稳定的端口，旨在使异步编程变得简单，高效，无忧且无错误。

我们在8月16日（也就是4个月前）宣布了[async-std](https://async.rs/)。我们最初发布的重点是为用户提供稳定可靠的API，以基于Rust标准库为模型构建异步应用程序。它带有许多创新的实现：`JoinHandle`基于任务的API和单一分配任务的第一个实现。

今天，我们将介绍新的[async-std](https://async.rs/)运行时。它具有许多改进，但主要新闻是它消除了并发程序中的错误和性能问题的主要来源：意外阻塞。

综上所述：

- 新的运行时**确实非常快，**并且性能优于旧的。
- 从某种意义上说，新的运行时是**通用**的，它可以自动适应不同的工作负载，并按需成为单线程或多线程。如果一个线程可以处理所有工作，那么我们就不必为窃取工作付出任何代价。
- 通过消除非阻塞线程池和阻塞线程池之间的分隔，新的运行时在**概念上更加简单**。
- 新的运行时**会**自动**检测到阻塞**。我们不再需要[`spawn_blocking`](https://docs.rs/async-std/1.2.0/async_std/task/fn.spawn_blocking.html)，可以简单地弃用它。
- 新的运行时使**阻塞有效**。除了只支付工作的费用`spawn_blocking`，我们仅在工作确实阻塞的情况下才将阻塞的工作转移到单独的线程中。

新的任务调度算法和阻止策略是Go运行时对Rust使用的思想的改编。

## 阻塞的问题

直到今天，在Rust中编写异步程序时，经常遇到挫折的可能是在运行任务时*意外* *阻塞*执行程序线程。为避免该问题，`async-std`用于提供不稳定的`spawn_blocking`功能，该功能将潜在的阻塞工作移至特殊的线程池上，以便执行程序线程可以保持进度。

但是，`spawn_blocking`这不是防弹解决方案，因为我们必须记住每次希望阻止时都要手动调用它。但是，甚至很难可靠地预测*可以*阻止哪种代码。程序员必须仔细分离异步代码和阻塞代码，这是一个臭名昭著的问题，在博客文章“ [*什么颜色是您的功能*](https://journal.stuffwithstuff.com/2015/02/01/what-color-is-your-function/) ”中进行了讨论。

当您考虑可能会阻塞*当前执行程序线程的操作*包括普通的昂贵计算（例如，转换图像或对大量数据进行排序）时，代码分离会变得更加困难。相反，有时我们会悲观地假设一些代码块，而实际上这可能会很快，这意味着`spawn_blocking`即使没有必要，我们也会付出代价。

使用新的`async-std`运行时，这样的困难已成为过去：如果任务执行时间过长，运行时将通过产生新的执行程序线程来接管当前线程的工作，从而自动做出反应。这种策略消除了分离异步代码和阻塞代码的需要。

## 一个具体的例子

为了说明所有这些在实践中的含义，让我们`std::fs::read_to_string`以阻塞操作为例。该[异步版本](https://docs.rs/async-std/1.3.0/async_std/fs/fn.read_to_string.html)的它用来实现如下：

```
async fn read_to_string<P: AsRef<Path>>(path: P) -> io::Result<String> {
    let path = path.as_ref().to_owned();
    spawn_blocking(move || std::fs::read_to_string(path)).await
}
```

请注意两个关键事项：

- 我们呼吁`spawn_blocking`隔离阻塞操作。
- 我们始终会克隆路径并在单独的线程池上执行阻塞操作，即使该文件已缓存并可以立即读取。

新的运行时减轻了您的这些麻烦，并允许您直接在async函数内部执行阻塞操作：

```
async fn read_to_string(path: impl AsRef<Path>) -> io::Result<String> {
    std::fs::read_to_string(path)
}
```

运行时将测量执行阻塞操作所需的时间，如果需要一段时间，则会自动生成一个新线程并替换旧的执行程序线程。这样，仅当前任务在操作上被阻止，而不是整个执行程序线程或整个运行时被阻止。如果阻塞操作很快，我们就不会产生新的线程，因此不会造成任何额外的开销。

如果您*仍要*确保操作在后台运行并且也不阻塞当前任务，则可以简单地生成一个常规任务并在其中执行阻塞工作：

```
async fn read_to_string(path: impl AsRef<Path>) -> io::Result<String> {
    let path = path.as_ref().to_owned();
    spawn(async move { std::fs::read_to_string(path) }).await
}
```

请注意使用`spawn`代替`spawn_blocking`。

Web框架通常需要异步I / O，同时每个请求都要执行大量工作。新的运行时，您可以使用无畏同步库像`diesel`或`rayon`在任何`async-std`应用程序。

## 基准测试

在我们的初始测试中，新的调度程序比旧的调度程序性能更好，同时仍保持较小且易于理解。

以下基准测试在两个EC2实例上运行。一个[minihttp](https://github.com/stjepang/minihttp)基于旧的运行时（服务器`master`分支）和新的运行时（`new-scheduler`分支）上m5a.8xlarge实例上运行，而[WRK](https://github.com/wg/wrk)（一个基准测试工具）上的单独m5a.16xlarge实例中运行。

该基准测试具有三种不同的方案，并向wrk传递了不同的参数。Option `-t`配置线程数，`-c`配置TCP连接数，并`-d`配置基准测试的持续时间（以秒为单位）。有关如何运行基准测试的更多详细信息，请参见[自述文件](https://github.com/stjepang/minihttp/blob/master/README.md)。

![不同基准的图表。 wrk -t1 -c50 -d10：新的调度程序快2倍。 wrk -t10 -c50 -d10：新的调度程序快5倍。 wrk -t1 -c500 -d10：新的调度程序快15倍](https://async.rs/images/async-std-http-benchmark-new-vs-old-scheduler.svg)

一般而言，新的运行时更快，并且可以更好地扩展以利用可用资源。

## 小而有据可查的

新的运行时很小，不使用`unsafe`并且已记录在案。请查看[源](https://github.com/stjepang/async-std/tree/new-scheduler/src/rt)以了解其工作原理。随意在[拉动要求](https://github.com/async-rs/async-std/pull/631)上提问！仍有许多优化机会，我们将继续在博客中介绍这些细节！

## 尝试一下

要在发布前试用新的调度程序，请按`Cargo.toml`以下方式进行修改：

```
async-std = { git = 'https://github.com/stjepang/async-std', branch = 'new-scheduler' }
```

请报告您的经验-并报告潜在的错误！

## 摘要

新的`async-std`运行时减轻了程序员将阻塞代码与异步代码隔离的负担。您完全不必再为此担心。

当多线程没有带来任何好处时，新运行时的自适应特性使其可以使用*更少的*资源。这样可以提高CLI工具的性能，并降低Web服务器的延迟。同时，运行时将扩展以在繁重的工作负载中使用所有可用资源。

所有这些更改使编写异步程序变得更加容易，同时*也*使它们更高效，更可靠！

我们要感谢[*async-std的所有贡献者，无论*](https://github.com/async-rs/async-std/graphs/contributors)大小，新的和长期的，以及所有库作者为Rust异步生态系统构建了出色的东西！