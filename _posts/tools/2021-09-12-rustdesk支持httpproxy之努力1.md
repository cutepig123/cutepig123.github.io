# 背景

由于某些原因，一定要经过一个http proxy才能上得到网，并且只能连接443端口。可是rustdesk不支持http proxy啊。即使用某些工具比如sockscap64发现还是不行，为啥呢，因为rustdesk还是需要udp，而http proxy是不支持udp的

当然有某些招数是可以的，比如搞个vpn，或者某些-软件。但这样的不好处是整个流程又依赖于多个软件，不符合俺心目中的简单原则啊。俺最希望的是这个软件本身就能支持httpproxy那有多好

# 俺的思路

server：先把udp搞掉，然后搞成只有一个tcp端口，这样就能直接过httpproxy了

现在的成果：在底层入手，修改udp.rs，用tcp（用redis的pub/sub功能）来mock相关udp的功能

udp send to dest addr：mock成pub一个消息到dest addr channel

udp recv from addr：mock成sub到自己的addr channel

代码：

[Commits · cutepig123/rustdesk · GitHub](https://github.com/cutepig123/rustdesk/commits/feature/bypasshttpproxy)

[Commits · cutepig123/rustdesk-server-demo · GitHub](https://github.com/cutepig123/rustdesk-server-demo/commits/feature/bypasshttpproxy)

发现了几个不好的东西

- new redis mode needs base64 encode
- new redis mode cannot bind to 0.0.0.0 as it need to be clear for pub/sub mode -》这个问题比较严重，做不到透明mock的效果了
- 测试的时候发现客户端有时候连不上，不知道啥原因

# 结论

看来要做好还是最好研究一下代码流程，从根源上改进可能会更好吧



# rust

折腾rust的数据类型先转换都搞了好久。这就是类型系统太复杂的坏处。。

```rust
fn main() {
    println!("Hello, world!");
    // v -> b64 -> bytes
    let v = vec![1u8,2,3];
    let b64 = base64::encode(&v[..]);
    let b = bytes::Bytes::from(b64);
    // bytes -> b64 -> v
    let b64 = base64::decode(&b[..]).unwrap();
    let v2 = Vec::from(&b64[..]);
    //print!("v {:?} b {:?} v2 {:?}", v, b, v2);
}
```
