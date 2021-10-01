---
categories: tools
---
[TOC]

jaeger tracing

# architecture

https://www.jaegertracing.io/docs/1.21/architecture/

![Architecture](jaeger%20tracing.assets/architecture-v1.png)

![img](jaeger%20tracing.assets/v2-f671cb89ab5946b181443c53962cfa2f_720w.jpg)

如上图所示，Jaeger 主要由以下几部分组成。

- Jaeger Client - 为不同语言实现了符合 OpenTracing 标准的 SDK。应用程序通过 API 写入数据，client library 把 trace 信息按照应用程序指定的采样策略传递给 jaeger-agent。
- Agent - 它是一个监听在 UDP 端口上接收 span 数据的网络守护进程，它会将数据批量发送给 collector。它被设计成一个基础组件，部署到所有的宿主机上。Agent 将 client library 和 collector 解耦，为 client library 屏蔽了路由和发现 collector 的细节。
- Collector - 接收 jaeger-agent 发送来的数据，然后将数据写入后端存储。Collector 被设计成无状态的组件，因此您可以同时运行任意数量的 jaeger-collector。
- Data Store - 后端存储被设计成一个可插拔的组件，支持将数据写入 cassandra、elastic search。
- Query - 接收查询请求，然后从后端存储系统中检索 trace 并通过 UI 进行展示。Query 是无状态的，您可以启动多个实例，把它们部署在 nginx 这样的负载均衡器后面。

https://www.jaegertracing.io/docs/1.21/getting-started/

run the `jaeger-all-in-one(.exe)` executable from the [binary distribution archives](https://www.jaegertracing.io/download/):

Copy

```bash
$ jaeger-all-in-one --collector.zipkin.http-port=9411
```

You can then navigate to `http://localhost:16686` to access the Jaeger UI.

The container exposes the following ports:

| Port  | Protocol | Component | Function                                                     |
| :---- | :------- | :-------- | :----------------------------------------------------------- |
| 5775  | UDP      | agent     | accept `zipkin.thrift` over compact thrift protocol (deprecated, used by legacy clients only) |
| 6831  | UDP      | agent     | accept `jaeger.thrift` over compact thrift protocol          |
| 6832  | UDP      | agent     | accept `jaeger.thrift` over binary thrift protocol           |
| 5778  | HTTP     | agent     | serve configs                                                |
| 16686 | HTTP     | query     | serve frontend                                               |
| 14268 | HTTP     | collector | accept `jaeger.thrift` directly from clients                 |
| 14250 | HTTP     | collector | accept `model.proto`                                         |
| 9411  | HTTP     | collector | Zipkin compatible endpoint (optional)                        |

# Basic setup

下載jaeger-all-in-one

下載https://github.com/jaegertracing/jaeger-client-cpp

用cmake編譯

To build:

```bash
    mkdir build
    cd build
    cmake ..
    make
```

運行jaeger-all-in-one

由於hunter下載一些依賴到c:\.hunter目錄，需要人手拷貝幾個dll到app.exe所在路徑

After building, the [example](./examples/App.cpp) program can be run
with:

```bash
    ./app ../examples/config.yml
```

效果

![image-20210127154723734](jaeger%20tracing.assets/image-20210127154723734.png)

以上直接打印trace信息，也可以設置鏈接到agent

```yml
disabled: false
reporter:
    localAgentHostPort: localhost:6831
    logSpans: true
sampler:
  type: const
  param: 1

```

這樣效果如下

![image-20210127155945240](jaeger%20tracing.assets/image-20210127155945240.png)

也可以直接連接collector

```
disabled: false
reporter:
    endpoint: http://localhost:14268/api/traces
    logSpans: true
sampler:
  type: const
  param: 1
```



# QA

## client lib和agent之間的數據協議是怎樣的（w/ ans）

`jaeger.thrift` over binary thrift protocol

https://github.com/yangwenmai/jaeger-opentracing-examples/blob/master/vendor/github.com/apache/thrift/doc/specs/thrift-binary-protocol.md

## agent是必須的嘛？（w/ ans）

不是必須

https://medium.com/swlh/learn-how-to-use-and-deploy-jaeger-components-in-production-fddb9947b2b2

> [Jaeger客户端库希望**jaeger-agent**进程在每个主机上本地运行。](https://www.jaegertracing.io/docs/1.21/deployment/#agent)

明确声明代理应该安装在主机中，或者如果愿意，<u>可以直接将跟踪指标直接发送到Jaeger收集器中</u>。Jaeger的创建者Yuri Shkuro在此回复中也提出了这一建议：

> Jaeger代理应始终与Sidecar或主机代理一起在与应用程序相同的主机上运行。或者，可以将Jaeger客户端配置为直接将范围发送到收集器，然后收集器可以在任何地方运行。
> -**尤里Shkuro**

Jaeger代理充当您的应用程序与Jaeger收集器之间的中间缓冲区。与您的应用程序保持紧密联系将对您的性能有所帮助，因为您的应用程序将使用UDP协议（通常为端口6831）发送数据，然后使用gRPC（通常为Jaeger收集器中的端口14250）将其缓冲到Jaeger收集器。由于UDP是无状态协议，因此有意义的是，在同一主机中安装将减少发送度量标准时数据丢失的风险。



https://stackoverflow.com/questions/59153293/advantages-of-using-jaeger-agent



## agent和collector 之間的數據協議是怎樣的（w/ ans）

14268  HTTP  collector  accept `jaeger.thrift` directly from clients  14250  HTTP  collector  accept `model.proto`  9411  HTTP  collector  Zipkin compatible endpoint (optional)

## jaeger-all-in-one使用的是什麽DB？（w/ ans）

他好像衹是把數據存在内存裏面 https://github.com/jaegertracing/jaeger/issues/551

看文檔也可以配置為別的方式

Jaeger all-in-one distribution with agent, collector and query. Use with caution this version by default uses only in-memory database.

jaeger-all-in-one can be used with these storage backends:

- [jaeger-all-in-one with `cassandra`](https://www.jaegertracing.io/docs/1.21/cli/#jaeger-all-in-one-cassandra)
- [jaeger-all-in-one with `elasticsearch`](https://www.jaegertracing.io/docs/1.21/cli/#jaeger-all-in-one-elasticsearch)
- [jaeger-all-in-one with `memory`](https://www.jaegertracing.io/docs/1.21/cli/#jaeger-all-in-one-memory)
- [jaeger-all-in-one with `badger`](https://www.jaegertracing.io/docs/1.21/cli/#jaeger-all-in-one-badger)
- [jaeger-all-in-one with `grpc-plugin`](https://www.jaegertracing.io/docs/1.21/cli/#jaeger-all-in-one-grpc-plugin)

### **存储后端**

Collectors需要持久的存储后端.Cassandra和Elasticsearch是主要支持的存储后端。 其他后端在[此处讨论](https://github.com/jaegertracing/jaeger/issues/638)。

可以通过SPAN_STORAGE_TYPE环境变量来传递存储类型。 有效值为cassandra,elasticsearch,kafka(仅作为缓冲区),grpc-plugin,badger(仅适用于all-in-one)和memory(仅适用于all-in-one)。

从1.6.0版开始,可以通过向SPAN_STORAGE_TYPE环境变量提供一个以逗号分隔的有效类型列表来同时使用多种存储类型。 重要的是要注意,所有列出的存储类型都用于写入,但是列表中仅第一个类型将用于读取和归档。

### **内存**

内存中存储不适用于生产工作负载。它旨在作为一种快速入门的简单解决方案, 该过程结束后,数据将丢失。

默认情况下,存储在内存中的跟踪数量没有限制,但是可以通过`--memory.max-traces`传递一个整型来建立限制。

### **Badger-本地存储**

自Jaeger 1.9起进行实验

[Badger](https://github.com/dgraph-io/badger)是嵌入式本地存储,仅可用 具有`all-in-one`分布。默认情况下,它用作使用临时文件系统的临时存储。 这可以通过使用`--badger.ephemeral = false`选项来覆盖。



```
docker run \
  -e SPAN_STORAGE_TYPE=badger \
  -e BADGER_EPHEMERAL=false \
  -e BADGER_DIRECTORY_VALUE=/badger/data \
  -e BADGER_DIRECTORY_KEY=/badger/key \
  -v <storage_dir_on_host>:/badger \
  -p 16686:16686 \
  jaegertracing/all-in-one:1.14
```

## windows下如何編譯jaeger-all-in-one

## 如何打開jaeger-all-in-one的metrics以便Prometheus可以訪問他（w/ ans）

默認情況下metrcis已經打開了，端口如下

https://www.jaegertracing.io/docs/1.21/monitoring/

Each Jaeger component exposes the metrics scraping endpoint on the admin port:

| Component            | Port  |
| :------------------- | :---- |
| **jaeger-agent**     | 14271 |
| **jaeger-collector** | 14269 |
| **jaeger-query**     | 16687 |
| **jaeger-ingester**  | 14270 |
| **all-in-one**       | 14269 |

設置proomethus訪問jaeger的tracing

```yml

scrape_configs:
  

  - job_name: 'jaeger'

    # metrics_path defaults to '/metrics'
    # scheme defaults to 'http'.

    static_configs:
    - targets: ['localhost:14269']
```

效果如下

![image-20210127161005251](jaeger%20tracing.assets/image-20210127161005251.png)

![image-20210127161338498](jaeger%20tracing.assets/image-20210127161338498.png)

## jaeger-all-in-one的metrics的實現代碼是怎樣的？



## jaeger-all-in-one能否用在生產環境？

## 什麽是docker compose文件

## 什麽是badger（w/ ans）

https://github.com/dgraph-io/badger

BadgerDB是用纯Go编写的可嵌入，持久和快速键值（KV）数据库。它是[Dgraph](https://dgraph.io/)（快速，分布式图形数据库）的基础数据库。它旨在成为RocksDB等非基于Go的键值存储的高性能替代品。

## Sender是base class，他的具體實現代碼在哪裏（w/ ans）

好像是ThriftSender.cpp

## ThriftSender用什麽庫來發送tcp數據，他是同步還是異步？

好像是ThriftSender::flush()調用_transporter->emitBatch(batch)發送數據
看ThriftSender代碼，他要求單綫程使用，不支持多綫程
看G:\_codes\jaeger-client-cpp\src\jaegertracing\reporters\Config.cpp，ThriftSender的ctor參數為UDPTransporter或者HTTPTransporter。
UDPTransporter代碼在G:\_codes\jaeger-client-cpp\src\jaegertracing\utils\UDPTransporter.h，其emitBatch（）函數調用了_client->emitBatch（），而client初始化為agent::thrift::AgentClient類型

所以其實際上使用的是thrift庫

```cpp
void AgentClient::send_emitBatch(const  ::jaegertracing::thrift::Batch& batch)
{
  int32_t cseqid = 0;
  oprot_->writeMessageBegin("emitBatch", ::apache::thrift::protocol::T_ONEWAY, cseqid);

  Agent_emitBatch_pargs args;
  args.batch = &batch;
  args.write(oprot_);

  oprot_->writeMessageEnd();
  oprot_->getTransport()->writeEnd();
  oprot_->getTransport()->flush();
}
```

thrift是一個rpc框架

https://thrift.apache.org/

## 能不能畫一個典型的sequence diagram描述client lib如何與agent交互？

```sequence
app -> client_lib: x
```

## 閲讀他的測試代碼有啥感受（w/ ans）

使用了不少mock技術，這個同時也要求他的代碼大量使用接口

比如在ThriftSender，其基類為 接口Sender，其構造函數參數為transporter，兩者都是接口類

在測試中，MockThriftSender的構造函數參數為MockUDPSender，而MockUDPSender爲一個mock的transporter實現

## 什麽是.hunter（w/ ans）

https://github.com/ruslo/hunter/tree/v0.23.115

CMake driven cross-platform package manager for C/C++. Linux, Windows, macOS, iOS, Android, Raspberry Pi,

## 把自己的trace格式發送給jaeger ui的最簡方式是什麽？（w/ ans）

1. `寫一個client發送jaeger.thrift` over compact thrift protocol協議數據給agant
2. 寫一個client發送accept `jaeger.thrift` directly from clients給collector
3. 寫一個serve frontend，**jaeger-query** server。 協議為？？

參考資料如下1，2

### Thrift over UDP (stable)

The Agent can only receive spans over UDP in Thrift format. The primary API is a UDP packet that contains a Thrift-encoded `Batch` struct defined in [jaeger.thrift](https://github.com/jaegertracing/jaeger-idl/blob/master/thrift/jaeger.thrift) IDL file, located in the [jaeger-idl](https://github.com/jaegertracing/jaeger-idl/) repository. Most Jaeger Clients use Thrift’s `compact` encoding, however some client libraries do not support it (notably, Node.js) and use Thrift’s `binary` encoding (sent to a different UDP port). The Agent’s API is defined by [agent.thrift](https://github.com/jaegertracing/jaeger-idl/blob/master/thrift/agent.thrift) IDL file.

For legacy reasons, the Agent also accepts spans in Zipkin format, however, only very old versions of Jaeger clients can send data in that format and it is officially deprecated.

### Protobuf via gRPC (stable)

In a typical Jaeger deployment, Agents receive spans from Clients and forward them to Collectors. Since Jaeger version 1.11 the official and recommended protocol between Agents and Collectors is gRPC with Protobuf as defined in [collector.proto](https://github.com/jaegertracing/jaeger-idl/blob/master/proto/api_v2/collector.proto) IDL file.

### Thrift over HTTP (stable)

In some cases it is not feasible to deploy Jaeger Agent next to the application, for example, when the application code is running as AWS Lambda function. In these scenarios the Jaeger Clients can be configured to submit spans directly to the Collectors over HTTP/HTTPS.

The same [jaeger.thrift](https://github.com/jaegertracing/jaeger-idl/blob/master/thrift/jaeger.thrift) payload can be submitted in HTTP POST request to `/api/traces` endpoint, for example, `https://jaeger-collector:14268/api/traces`. The `Batch` struct needs to be encoded using Thrift’s `binary` encoding, and the HTTP request should specify the content type header:

Copy

```
Content-Type: application/vnd.apache.thrift.binary
```

3，

### gRPC/Protobuf (stable)

The recommended way for programmatically retrieving traces and other data is via gRPC endpoint defined in [query.proto](https://github.com/jaegertracing/jaeger-idl/blob/master/proto/api_v2/query.proto) IDL file.