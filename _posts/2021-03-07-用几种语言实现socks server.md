用几种语言实现socks server

# 总结

- socks协议本身比较简单，编写难度不大
- 首先要会用工具解析封包，这样一是了解协议，二是方便调试代码的问题
- c++的主要难点在与
  - boost，cmake工具链
  - 要留意变量生命周期，需要的时候用share_ptr
- rust
  - ？？
- python
  - ??

# rust

参考实现 https://github.com/WANG-lp/socks5-rs

# c++

## 同步

使用boost asio

代码包含两部分，协议分析层，和网络层

- 协议分析层
  - verify1: 握手
  - Cmd：链接目标
- 网络层
  - read
  - write
  - connect
  - thread：数据转发

```cpp
#include <ctime>
#include <iostream>
#include <string>
#include <boost/asio.hpp>
#include <boost/array.hpp>
#include <boost/thread.hpp>
#include <vector>
#include <assert.h>

using boost::asio::ip::tcp;

std::string make_daytime_string()
{
    using namespace std; // For time_t, time and ctime;
    time_t now = time(0);
    return ctime(&now);
}

class verify1
{
    int ver;
    
    enum class Method
    {
        NA = 0,
        GSSAPI = 1,
        USERNAMEPASSWORD=2,
        IANA=3,
        RESERVED=0x80,
        NO=0xff
    };
    std::vector<Method> methods;

public:
    template <class F>
    void read_req(F read)
    {
        ver = read(1);
        assert(ver == 5);
        size_t NMETHODS = read(1);
        methods.reserve(NMETHODS);
        assert(NMETHODS > 0 && NMETHODS < 10);
        for (size_t i = 0; i < NMETHODS; i++)
        {
            int method = read(1);
            methods.push_back(Method(method));
        }
    }

    template <class F>
    void send_rpy(F write)
    {
        write({ 5 });
        assert(std::find(methods.begin(), methods.end(), Method::NA) != methods.end());
        write({ 0 });
    }
};

enum class CMDType
{
    CONNECT=1,
    BIND=2,
    UDP=3,
};

enum class ATYPType
{
    IPv4=0x01,
    Domain=0x03,
    IPv6=0x04,
};

class Cmd
{
    int VER;
    CMDType CMD;
    int RSV;
    ATYPType ATYP;
    
    union DSTADDR {
        unsigned char ipv4[4];
        char domain[100];
        char ipv6[16];
    }dstAddr;

    int dstPort;

public:
    template <class F, class F2>
    void read_req(F read, F2 connect)
    {
        VER = read(1);
        assert(VER == 5);
        CMD = CMDType(read(1));
        RSV = read(1);
        ATYP = ATYPType(read(1));
        switch (ATYP)
        {
        case ATYPType::IPv4:
            for (size_t i = 0; i < 4; i++)
            {
                dstAddr.ipv4[i] = read(1);
            }
            printf("dest ip: %d,%d,%d,%d\n", dstAddr.ipv4[0], dstAddr.ipv4[1], dstAddr.ipv4[2], dstAddr.ipv4[3]);
            sprintf(dstAddr.domain, "%d.%d.%d.%d", dstAddr.ipv4[0], dstAddr.ipv4[1], dstAddr.ipv4[2], dstAddr.ipv4[3]);
            break;
        case ATYPType::Domain:
        {
            size_t n = read(1);
            assert(n < 100);
            for (size_t i = 0; i < n; i++)
            {
                dstAddr.domain[i] = read(1);
            }
            dstAddr.domain[n] = 0;
            printf("dest domain: %s\n", dstAddr.domain);
        }
            break;
        case ATYPType::IPv6:
            assert(0);
            break;
        default:
            break;
        }

        dstPort = read(2);
        printf("dest port: %d\n", dstPort);
        char sport[100];
        sprintf(sport, "%d", dstPort);

        connect(dstAddr.domain, sport);
    }

    template <class F>
    void send_rpy(F write)
    {
        write({5 });    // Version: 5
        write({ 0 });    // Results(V5): Succeeded (0)
        write({ 0 });    // Reserved: 0
        write({ 1 });    // Address Type: IPv4 (1)
        write({ 127, 0, 0, 1 }); // Remote Address : 10.0.120.14
        write({ 1,0 });    // Port: 55593
    }
};

int main()
{
    try
    {
        boost::asio::io_context io_context;
        tcp::acceptor acceptor(io_context, tcp::endpoint(tcp::v4(), 10800));
        for (;;)
        {
            tcp::socket socket(io_context);
            acceptor.accept(socket);
            
            auto read =
                [&socket](int n) ->int {
                boost::array<char, 1> buf;
                
                char ret[4] = { 0 };
                for (size_t i = 0; i < n; i++)
                {
                    size_t len = socket.read_some(boost::asio::buffer(buf));
                    ret[i] = buf[0];
                }
                int t = *(int*)ret;
                if (n==1)
                {
                    return t;
                }
                if (n == 2)
                {
                    return ntohs(t);
                }
                if (n == 4)
                {
                    return ntohl(t);
                }
                assert(0);
            };
            char write_data[100];
            int write_len = 0;
            auto write_begin = [&write_len]() {write_len = 0; };
            auto write = [&write_len, &write_data](std::initializer_list<char> args)  {
                for (char i: args)
                {
                    write_data[write_len++] = i;
                }
            };
            auto write_end = [&socket, &write_len, &write_data]() {
                printf("write %d bytes\n", write_len);
                for (size_t i = 0; i < write_len; i++)
                {
                    printf("%x", write_data[i]);
                }
                printf("\n");
                socket.write_some(boost::asio::buffer(write_data, write_len));
            };

            verify1 v1;
            v1.read_req(read);
            write_begin();
            v1.send_rpy(write);
            write_end();

            tcp::resolver::results_type endpoints;
            auto connect = [&io_context, &endpoints](const char *name, const char* port) {
                tcp::resolver resolver(io_context);
                endpoints =
                    resolver.resolve(tcp::v4(), name, port);
            };

            Cmd cmd;
            cmd.read_req(read, connect);
            write_begin();
            cmd.send_rpy(write);
            write_end();

            tcp::socket sock_remote(io_context);
            boost::asio::connect(sock_remote, endpoints);

            boost::thread th1([&sock_remote, &socket] {
                boost::system::error_code ec;
                while (!ec)
                {
                    uint8_t data[512];

                    size_t len = sock_remote.read_some(boost::asio::buffer(data), ec);

                    if (len > 0)
                    {
                        std::cout << "received " << len << " bytes\n";
                        boost::asio::write(socket, boost::asio::buffer(data, len));
                    }
                }
            });
            
            boost::system::error_code ec;
            while (!ec)
            {
                uint8_t data[512];

                size_t len = socket.read_some(boost::asio::buffer(data), ec);

                if (len > 0)
                {
                    std::cout << "received " << len << " bytes\n";
                    boost::asio::write(sock_remote, boost::asio::buffer(data, len));
                }
            }

            th1.join();
        }
    }
    catch (std::exception& e)
    {
        std::cerr << e.what() << std::endl;
    }

    return 0;
}

```



## 异步

使用boost asio coroutine

基本思路是把网络层重新实现了一下，协议分析层代码完全一样

- 协议分析层

  - verify1: 握手. 和同步实现的代码完全一样
  - Cmd：链接目标. 和同步实现的代码完全一样

- 网络层。用coroutine重新实现

  - read
  - write
  - connect
  - thread：数据转发

  为了便于实现，写了一个session类封装每次链接相关的数据

  

```cpp
#include <ctime>
#include <iostream>
#include <string>
#include <boost/asio.hpp>
#include <boost/array.hpp>
#include <boost/thread.hpp>
#include <boost/asio/spawn.hpp>
#include <vector>
#include <assert.h>

using boost::asio::ip::tcp;

std::string make_daytime_string()
{
    using namespace std; // For time_t, time and ctime;
    time_t now = time(0);
    return ctime(&now);
}

class verify1
{
    int ver;
    
    enum class Method
    {
        NA = 0,
        GSSAPI = 1,
        USERNAMEPASSWORD=2,
        IANA=3,
        RESERVED=0x80,
        NO=0xff
    };
    std::vector<Method> methods;

public:
    template <class F>
    void read_req(F read)
    {
        ver = read(1);
        assert(ver == 5);
        size_t NMETHODS = read(1);
        methods.reserve(NMETHODS);
        assert(NMETHODS > 0 && NMETHODS < 10);
        for (size_t i = 0; i < NMETHODS; i++)
        {
            int method = read(1);
            methods.push_back(Method(method));
        }
    }

    template <class F>
    void send_rpy(F write)
    {
        write({ 5 });
        assert(std::find(methods.begin(), methods.end(), Method::NA) != methods.end());
        write({ 0 });
    }
};

enum class CMDType
{
    CONNECT=1,
    BIND=2,
    UDP=3,
};

enum class ATYPType
{
    IPv4=0x01,
    Domain=0x03,
    IPv6=0x04,
};

class Cmd
{
    int VER;
    CMDType CMD;
    int RSV;
    ATYPType ATYP;
    
    union DSTADDR {
        unsigned char ipv4[4];
        char domain[100];
        char ipv6[16];
    }dstAddr;

    int dstPort;

public:
    template <class F, class F2>
    void read_req(F read, F2 connect)
    {
        VER = read(1);
        assert(VER == 5);
        CMD = CMDType(read(1));
        RSV = read(1);
        ATYP = ATYPType(read(1));
        switch (ATYP)
        {
        case ATYPType::IPv4:
            for (size_t i = 0; i < 4; i++)
            {
                dstAddr.ipv4[i] = read(1);
            }
            printf("dest ip: %d,%d,%d,%d\n", dstAddr.ipv4[0], dstAddr.ipv4[1], dstAddr.ipv4[2], dstAddr.ipv4[3]);
            sprintf(dstAddr.domain, "%d.%d.%d.%d", dstAddr.ipv4[0], dstAddr.ipv4[1], dstAddr.ipv4[2], dstAddr.ipv4[3]);
            break;
        case ATYPType::Domain:
        {
            size_t n = read(1);
            assert(n < 100);
            for (size_t i = 0; i < n; i++)
            {
                dstAddr.domain[i] = read(1);
            }
            dstAddr.domain[n] = 0;
            printf("dest domain: %s\n", dstAddr.domain);
        }
            break;
        case ATYPType::IPv6:
            assert(0);
            break;
        default:
            break;
        }

        dstPort = read(2);
        printf("dest port: %d\n", dstPort);
        char sport[100];
        sprintf(sport, "%d", dstPort);

        connect(dstAddr.domain, sport);
    }

    template <class F>
    void send_rpy(F write)
    {
        write({5 });    // Version: 5
        write({ 0 });    // Results(V5): Succeeded (0)
        write({ 0 });    // Reserved: 0
        write({ 1 });    // Address Type: IPv4 (1)
        write({ 127, 0, 0, 1 }); // Remote Address : 10.0.120.14
        write({ 1,0 });    // Port: 55593
    }
};


// ref: https://www.boost.org/doc/libs/1_74_0/doc/html/boost_asio/example/cpp03/spawn/echo_server.cpp

class session : public boost::enable_shared_from_this<session>
{
public:
    explicit session(boost::asio::io_context& io_context)
        : io_context_(io_context),
        strand_(boost::asio::make_strand(io_context)),
        socket_(io_context),
        sock_remote_(io_context_)
    {
    }

    tcp::socket& socket()
    {
        return socket_;
    }

    void go()
    {
        boost::asio::spawn(strand_,
            boost::bind(&session::echo,
                shared_from_this(), boost::placeholders::_1));
    }

private:
    void echo(boost::asio::yield_context yield)
    {
        auto read =
            [this, &yield](int n) ->int {
            boost::array<char, 1> buf;

            char ret[4] = { 0 };
            for (size_t i = 0; i < n; i++)
            {
                size_t len = socket_.async_read_some(boost::asio::buffer(buf), yield);
                ret[i] = buf[0];
            }
            int t = *(int*)ret;
            if (n == 1)
            {
                return t;
            }
            if (n == 2)
            {
                return ntohs(t);
            }
            if (n == 4)
            {
                return ntohl(t);
            }
            assert(0);
        };
        char write_data[100];
        int write_len = 0;
        auto write_begin = [&write_len]() {write_len = 0; };
        auto write = [&write_len, &write_data](std::initializer_list<char> args) {
            for (char i : args)
            {
                write_data[write_len++] = i;
            }
        };
        auto write_end = [this, &write_len, &write_data, &yield]() {
            printf("write %d bytes\n", write_len);
            for (size_t i = 0; i < write_len; i++)
            {
                printf("%x", write_data[i]);
            }
            printf("\n");
            boost::asio::async_write(socket_, boost::asio::buffer(write_data, write_len), yield);
        };

        verify1 v1;
        v1.read_req(read);
        write_begin();
        v1.send_rpy(write);
        write_end();

        tcp::resolver::results_type endpoints;
        boost::system::error_code ec;
        auto connect = [this, &endpoints, &yield, &ec](const char* name, const char* port) {
            tcp::resolver resolver(io_context_);
            endpoints =
                resolver.async_resolve(tcp::v4(), name, port, yield[ec]);
        };

        Cmd cmd;
        cmd.read_req(read, connect);
        if (ec) return;
        write_begin();
        cmd.send_rpy(write);
        write_end();

        boost::asio::async_connect(sock_remote_, endpoints, yield[ec]);
        if (ec) return;

        boost::asio::spawn(strand_,
            boost::bind(&session::copy_sock_1, shared_from_this(), boost::placeholders::_1));

        boost::asio::spawn(strand_,
            boost::bind(&session::copy_sock_2, shared_from_this(), boost::placeholders::_1));
    }

    void copy_sock_1(boost::asio::yield_context yield)
    {
        tcp::socket& a = socket_;
        tcp::socket& b = sock_remote_;
        copy_sock(a, b, yield);
    }

    void copy_sock_2(boost::asio::yield_context yield)
    {
        tcp::socket& b = socket_;
        tcp::socket& a = sock_remote_;
        copy_sock(a, b, yield);
    }

    static void copy_sock(tcp::socket& a, tcp::socket& b, boost::asio::yield_context yield)
    {
        std::cout << "copy_sock \n";
        boost::system::error_code ec;
        while (!ec)
        {
            uint8_t data[512];

            size_t len = a.async_read_some(boost::asio::buffer(data), yield[ec]);

            std::cout << "received " << len << " bytes\n";
            if (len > 0)
            {
                b.async_write_some(boost::asio::buffer(data, len), yield[ec]);
            }
        }
    }
    boost::asio::io_context& io_context_;
    boost::asio::strand<boost::asio::io_context::executor_type> strand_;
    tcp::socket socket_;
    tcp::socket sock_remote_;
};

void do_accept(boost::asio::io_context &io_context, boost::asio::yield_context yield)
{
    tcp::acceptor acceptor(io_context, tcp::endpoint(tcp::v4(), 10800));

    for (;;)
    {
        tcp::socket socket(io_context);
        boost::shared_ptr<session> new_session(new session(io_context));
        acceptor.async_accept(new_session->socket(), yield);
        new_session->go();
    }
}
int main()
{
    try
    {
        boost::asio::io_context io_context;
        
        boost::asio::spawn(io_context,
            [&io_context](boost::asio::yield_context yield) {
            do_accept(io_context, yield);
        });

        io_context.run();
    }
    catch (std::exception& e)
    {
        std::cerr << e.what() << std::endl;
    }

    return 0;
}

```



## 如何编译boost

## [5.1  Simplified Build From Source](https://www.boost.org/doc/libs/1_74_0/more/getting_started/windows.html#id36)

If you wish to build from source with Visual C++, you can use a simple build procedure described in this section. Open the command prompt and change your current directory to the Boost root directory. Then, type the following commands:

```
bootstrap
.\b2
```

The first command prepares the Boost.Build system for use. The second command invokes Boost.Build to build the separately-compiled Boost libraries. Please consult the [Boost.Build documentation](https://www.boost.org/build/doc/html/bbv2/overview/invocation.html) for a list of allowed options.

## 如何cmake引用boost

```cmake
set(BOOST_ROOT "G:/_codes/boost_1_74_0_rc2/boost_1_74_0")
set(Boost_USE_STATIC_LIBS ON)
find_package(Boost REQUIRED)

include_directories(${Boost_INCLUDE_DIR})
link_directories(${Boost_LIBRARY_DIR_DEBUG})

```



## error LNK2026: module unsafe for SAFESEH image.

[ref](https://stackoverflow.com/questions/14710577/error-lnk2026-module-unsafe-for-safeseh-image)

在Visual Studio 2012 Express Edition中：

```cpp
Right-click on your project ->
Properties -> 
Configuration Properties ->
Linker ->
Advanced and changed "Image Has Safe Exception Handlers" to "No (/SAFESEH:NO)"
```

# python

# 如何截获网络封包

工具 wireshark

## [wireshark如何抓取本机包](https://www.cnblogs.com/lvdongjie/p/6110183.html)

###  

​    在进行通信开发的过程中，我们往往会把本机既作为客户端又作为服务器端来调试代码，使得本机自己和自己通信。但是wireshark此时是无法抓取到数据包的，需要通过简单的设置才可以。 

​    具体方法如下：

**方法一：**

​    1.以管理员身份运行cmd

​    2.route add 本机ip mask 255.255.255.255 网关ip

`route add 192.168.1.118 mask 255.255.255.255 192.168.1.1`

​    如：route add 172.16.51.115 mask 255.255.255.255 172.16.1.1

​    使用完毕后用route delete 172.16.51.115 mask 255.255.255.255 172.16.1.1删除，否则所有本机报文都经过网卡出去走一圈回来很耗性能。

​    此时再利用wireshark进行抓包便可以抓到本机自己同自己的通信包，这样配置的原因是将发往本机的包发送到网关，而此时wireshark可以捕获到网卡驱动的报文实现抓包。

​    但这样有一个缺点，那就是本地请求的URL的IP只能写本地的IP地址，不能写localhost或127.0.0.1，写localhost或127.0.0.1还是抓不到包。

 

**方法二：**

​    windows系统没有提供本地回环网络的接口，用wireshark监控网络的话只能看到经过网卡的流量，看不到访问localhost的流量，因为wireshark在windows系统上默认使用的是WinPcap来抓包的，现在可以用Npcap来替换掉WinPcap，Npcap是基于WinPcap 4.1.3开发的，api兼容WinPcap。

1.下载安装包

​    [Npcap项目主页](https://github.com/nmap/npcap)，它采用的是MIT开源协议，[Npcap下载](https://github.com/nmap/npcap/releases)

2.安装

​    安装时要勾选 Use DLT_NULL protocol sa Loopback ... 和 install npcap in winpcap api-compat mode，如下所示。

![img](../images/%E7%94%A8%E5%87%A0%E7%A7%8D%E8%AF%AD%E8%A8%80%E5%AE%9E%E7%8E%B0socks%20server.assets/dfccc991-ba44-3674-b01a-8a72364cf22f.png)
    如果你已经安装了wireshark, 安装前请先卸载WinPcap。

![img](../images/%E7%94%A8%E5%87%A0%E7%A7%8D%E8%AF%AD%E8%A8%80%E5%AE%9E%E7%8E%B0socks%20server.assets/ccf6f9c1-92bf-33b8-855b-3924553dd9dd.png)
    如果还提示WinPcap has been detected之类的，那就将C:\Windows\SysWOW64下的wpcap.dll修改为wpcap.dll.old，packet.dll修改为packet.dll.old，也可参考：https://nicolask.wordpress.com/2012/09/23/solved-winpcap-4-12-install-error/。

​    当然，如果还没有安装wireshark安装，安装wireshark不要安装WinPcap了。

​    安装完成启动wireshark, 可以看到在网络接口列表中，多了一项Npcap Loopback adapter，这个就是来抓本地回环包的网络接口了，打开后如下图：

![img](../images/%E7%94%A8%E5%87%A0%E7%A7%8D%E8%AF%AD%E8%A8%80%E5%AE%9E%E7%8E%B0socks%20server.assets/9404c547-9388-3ca3-aac5-de320fa22ae4.png)
    它不仅可以抓URL是localhost的，也可以是127.0.0.1。

![点击查看原始大小图片](../images/%E7%94%A8%E5%87%A0%E7%A7%8D%E8%AF%AD%E8%A8%80%E5%AE%9E%E7%8E%B0socks%20server.assets/d8a9fa26-7e55-369c-9565-7e35084aaabd.png)
    当然，抓本机IP也是完全可以的。

## 为啥我死活抓不到socks包？

你忘记设置端口了

![image-20201002224951835](../images/%E7%94%A8%E5%87%A0%E7%A7%8D%E8%AF%AD%E8%A8%80%E5%AE%9E%E7%8E%B0socks%20server.assets/image-20201002224951835.png)



# socks5协议

[https://guiyongdong.github.io/2017/12/09/Socks5%E4%BB%A3%E7%90%86%E5%88%86%E6%9E%90/](https://guiyongdong.github.io/2017/12/09/Socks5代理分析/)

### 认证

通常，socks5代理服务器都会配置在1080端口，他是基于TCP的，客户端要连接到代理服务器，首先要经过三次握手，之后需要和服务器进行认证，格式如下：

```
+----+----------+----------+
|VER | NMETHODS | METHODS  |
+----+----------+----------+
| 1  |    1     | 1 to 255 |
+----+----------+----------+
```

- VER 字段是当前协议的版本号，也就是5
- NMETHODS 字段是代表客户端支持的认证方式的个数
- METHODS 字段代表客户端支持的认证方式，每一位字节表示一种认证方式。

服务器在客户端发送的认证方式中选择一种进行匹配，返回数据如下：

```
+----+----------+
|VER |  METHODS |
+----+----------+
| 1  |    1     |
+----+----------+
```

- METHOD 即为服务器端匹配的结果，如果服务器返回的是OxFF，则表明客户端所支持的认证方式，服务器端都不支持。那么认证失败。

认证方式有如下几种：

```
0x00: 无验证需求
0x01: 通用安全服务应用程序接口(GSSAPI)
0x02: 用户名/密码(USERNAME/PASSWORD)
0x03: 至 0x7F IANA 分配(IANA ASSIGNED)
0x80: 至 0xFE 私人方法保留(RESERVED FOR PRIVATE METHODS)
0xFF: 无可接受方法(NO ACCEPTABLE METHODS)
```

下面通过WireShark分析socks5认证过程：

![img](../images/%E7%94%A8%E5%87%A0%E7%A7%8D%E8%AF%AD%E8%A8%80%E5%AE%9E%E7%8E%B0socks%20server.assets/socks5_1.png)

首先，客户端和服务器的三次握手建立连接，之后，客户端发送认证请求，我们可以看到，客户端发送的数据为：

- VER:05 即版本为5
- NMETHODS:02 即支持两种认证方式
- METHODS: 00 02 两种认证方式分别为 无须认证和用户名密码认证

![img](../images/%E7%94%A8%E5%87%A0%E7%A7%8D%E8%AF%AD%E8%A8%80%E5%AE%9E%E7%8E%B0socks%20server.assets/socks5_2.png)

服务器回的数据为：

- VER:05 即版本为5
- METHODS:00 即和客户端商议使用无须认证方式

当然，这里我配置的代理服务器没有使用用户名密码认证方式，假如需要此种方式的认证，客户端还需要发送用户名密码进行认证，有兴趣的同学可以试试。

### 连接

认证通过以后，客户端就需要告诉代理，需要它做什么，即需要给代理发命令，具体的格式如下：

```
+----+-----+-------+------+----------+----------+
|VER | CMD |  RSV  | ATYP | DST.ADDR | DST.PORT |
+----+-----+-------+------+----------+----------+
| 1  |  1  |   1   |  1   | Variable |    2     |
+----+-----+-------+------+----------+----------+
```

- VER: 协议版本
- CMD: 命令，有三种命令：

```
0x01：CONNECT 建立 TCP 连接 
0x02: BIND 上报反向连接地址
0x03：关联 UDP 请求
```

- RSV: 保留字段，值为 0x00
- ATYP: 地址类型，取值为：

```
0x01：IPv4
0x03: 域名
0x04：IPv6
```

- DST.ADDR 目的地，取值随ATYP的类型不同而不同，如下：

```
ATYP == 0x01：4 个字节的 IPv4 地址
ATYP == 0x03：1 个字节表示域名长度，紧随其后的是对应的域名
ATYP == 0x04：16 个字节的 IPv6 地址
```

- DST.PORT 目的地端口

服务器返回的数据如下：

```
+----+-----+-------+------+----------+----------+
|VER | REP |  RSV  | ATYP | BND.ADDR | BND.PORT |
+----+-----+-------+------+----------+----------+
| 1  |  1  |   1   |  1   | Variable |    2     |
+----+-----+-------+------+----------+----------+
```

- VER: 版本号
- REP: 服务器返回的结果

```
* X'00' succeeded
* X'01' general SOCKS server failure
* X'02' connection not allowed by ruleset
* X'03' Network unreachable
* X'04' Host unreachable
* X'05' Connection refused
* X'06' TTL expired
* X'07' Command not supported
* X'08' Address type not supported
* X'09' to X'FF' unassigned
```

- RSV 保留字段
- ATYP: 地址类型
- BND.ADDR: 服务器地址
- BND.PORT: 服务器端口

**CMD**

**CONNECT**

CONNECT表示要和目的主机建立TCP连接，在服务器回应中，BND.ADDR包含了关联的IP地址。此处所提供的BND.ADDR通常情况下不同于客户端连接到socks5代理服务器的IP地址，因为有可能代理服务器是一个集群，当然我这里只是一个服务器，所以返回的和代理的IP一样，BND.PORT表示服务器分配的连接到目标主机的端口号，即代理服务器接下来会使用BND.PORT这个端口与目标主机进行TCP通信。

**BIND**
BIND请求被用在那些需要客户机接收到服务器连接的协议中。FTP就是一个众所周知的例子。在实际应用场景中，一般用不到，这里不再细说。

**UDP ASSOCIATE**

此命令表示需要进行UDP转发，BND.ADDR和CONNECT中的含义一样，而BND.PORT表示服务器提供给客户端的UDP转发端口，接下来客户端的所有UDP都需要往代理的此端口发送。

因为我这次遇到的主要是UDP转发的问题，那么接下就着重分析一下UDP ASSOCIATE。

### UDP ASSOCIATE

当客户端发送UDP ASSOCIATE命名时，代理服务器会返回相应的断端口，如下：

![img](../images/%E7%94%A8%E5%87%A0%E7%A7%8D%E8%AF%AD%E8%A8%80%E5%AE%9E%E7%8E%B0socks%20server.assets/socks5_3.png)

服务器响应如下：

![img](../images/%E7%94%A8%E5%87%A0%E7%A7%8D%E8%AF%AD%E8%A8%80%E5%AE%9E%E7%8E%B0socks%20server.assets/socks5_4.png)

那么，客户端知道服务器地址以后，是如何发送到代理服务器呢？

一个UDP数据报如下：

```
+----+------+------+----------+----------+----------+
|RSV | FRAG | ATYP | DST.ADDR | DST.PORT |　　DATA　|
+----+------+------+----------+----------+----------+
|　2  |　 1　| 　1　 | Variable | 　2　　　 | Variable |
+----+------+------+----------+----------+----------+
```

- RSV 占两个字节 即 0x0000
- FRAG Current fragment number
- ATYP 目的地址类型
- DST.ADDR 目的地址
- DST.PORT 目的端口
- DATA 真正的数据

![img](../images/%E7%94%A8%E5%87%A0%E7%A7%8D%E8%AF%AD%E8%A8%80%E5%AE%9E%E7%8E%B0socks%20server.assets/socks5_5.png)

如此，客户端开始不断的发送UDP数据到代理服务器，代理服务器接收到数据后，又会如何呢？

![img](../images/%E7%94%A8%E5%87%A0%E7%A7%8D%E8%AF%AD%E8%A8%80%E5%AE%9E%E7%8E%B0socks%20server.assets/socks5_6.png)

我们可以看到，客户端与代理之间的数据要比代理与目的主机之间的数据大10个字节，而这10个字节正是socks5协议头。

完整的UDP转发流程为：

![img](../images/%E7%94%A8%E5%87%A0%E7%A7%8D%E8%AF%AD%E8%A8%80%E5%AE%9E%E7%8E%B0socks%20server.assets/socks5_7.jpg)

现在，大家是不是对socks5有了一个全面的认识呢！



https://i-meto.com/pipe-demo/